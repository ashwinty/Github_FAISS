import logging
import sys
import pandas as pd
import faiss
import os
from llama_index.core import SimpleDirectoryReader, load_index_from_storage, VectorStoreIndex, StorageContext

from llama_index.vector_stores.faiss import FaissVectorStore

# Load data for vector searching

documents = SimpleDirectoryReader(input_files=["final_all_cases.json"]).load_data()
os.environ['OPENAI_API_KEY'] = "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"


# """# Embeddings"""

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# load index from disk
vector_store = FaissVectorStore.from_persist_dir("./storage")
storage_context = StorageContext.from_defaults(
    vector_store=vector_store, persist_dir="./storage"
)
index = load_index_from_storage(storage_context=storage_context)

# """# Responses"""

# # # set Logging to DEBUG for more detailed outputs
query_engine = index.as_query_engine()
# query = input("Please enter your query: ")
# response = query_engine.query(query)
# print(response)

# def to_run(query):
#     response = query_engine.query(query)
#     return(response)

def extract_keywords(query):
    # You can use any NLP library for keyword extraction
    # Here, we'll use a simple method of splitting the query into words
    keywords = query.lower().split()
    return keywords
def highlight_matching_words(query, text):
    # Highlight matching words in the text using HTML
    highlighted_text = text.replace(query, f"<span style='background-color: yellow; colour : black'>{query}</span>")
    return highlighted_text

def to_run(query):
    # Extract keywords from the query
    keywords = extract_keywords(query)
    query_string = ' '.join(keywords)
    
    # Query the index with the query string
    response = query_engine.query(query_string)
    
    # Initialize an empty list to store formatted responses
    formatted_responses = []
    
    # Loop through each response
    for node in response.__dict__["source_nodes"]:
        # Access metadata and text directly from each node object
        metadata = node.metadata
        text = node.text
        
        # Highlight matching words in the response text
        highlighted_text = highlight_matching_words(query, text)
        
        # Format metadata and highlighted text into a tuple
        formatted_response = ([
            metadata["name"],
            metadata["date"],
            metadata["court"],
            metadata["link"]
        ], highlighted_text)
        
        # Append the formatted response to the list
        formatted_responses.append(formatted_response)
        
    return formatted_responses


# def to_run(query):
    
#     keywords = extract_keywords(query)
#     query_string = ' '.join(keywords)
    
    
#     # Query the index with the query string
#     response = query_engine.query(query_string)
    
#     # Print metadata keys to inspect the structure
#     print("Metadata keys:", response.metadata.keys())
    
#     # Extract metadata from the response
#     document_id = response.metadata.get("id")
#     document_name = response.metadata.get("name")
#     document_date = response.metadata.get("date")
#     document_court = response.metadata.get("court")
#     document_link = response.metadata.get("link")
    
#     # Print metadata along with the response text
#     print(f"Document ID: {document_id}")
#     print(f"Document Name: {document_name}")
#     print(f"Document Date: {document_date}")
#     print(f"Document Court: {document_court}")
#     print(f"Document Link: {document_link}")
#     # print("Response:", response)
    
#     l = []
#     for node in response.__dict__["source_nodes"]:
#     # Access metadata and text directly from each node object
#         metadata = node.metadata
#         text = node.text
    
#     # Create a tuple with metadata and text and append it to the list
#         t = ([
#             metadata["name"],
#             metadata["date"],
#             metadata["court"],
#             metadata["link"]
#         ], text)
#         l.append(t)
        
#     return l