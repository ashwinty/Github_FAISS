import logging
import sys
import pandas as pd

from llama_index import (
    SimpleDirectoryReader,
    load_index_from_storage,
    VectorStoreIndex,
    StorageContext,
)

from llama_index.vector_stores.faiss import FaissVectorStore


# Load documents from CSV file

df = pd.read_csv('/Users/ashwintyagi/Downloads/faiss/output.csv')

# Load data for vector searching

documents = SimpleDirectoryReader(input_files=["output.csv"]).load_data()

# Commented out IPython magic to ensure Python compatibility.
# os.environ['OPENAI_API_KEY'] = ""

# """# Embeddings"""

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# # dimensions of text-ada-embedding-002
# d = 1536
# faiss_index = faiss.IndexFlatL2(d)

# vector_store = FaissVectorStore(faiss_index=faiss_index)
# storage_context = StorageContext.from_defaults(vector_store=vector_store)
# index = VectorStoreIndex.from_documents(
#     documents, storage_context=storage_context
# )

# # save index to disk
# index.storage_context.persist()

# # load index from disk
vector_store = FaissVectorStore.from_persist_dir("./storage")
storage_context = StorageContext.from_defaults(
    vector_store=vector_store, persist_dir="./storage"
)
index = load_index_from_storage(storage_context=storage_context)

"""# Responses"""

# set Logging to DEBUG for more detailed outputs
query_engine = index.as_query_engine()
# query = input("Please enter your query: ")


def to_run(query):
    response = query_engine.query(query)
    return(response)
