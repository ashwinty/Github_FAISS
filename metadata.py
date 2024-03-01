import json
import os
from llama_index.core import Document
from llama_index.core.schema import MetadataMode

# Function to create Llama index document from JSON entry
def create_llama_document(entry):
    metadata = {
        "id": entry['id'],
        "name": entry['name'],
        "date": entry['date'],
        "court": entry['court'],
        "link": entry['link']
    }
    document = Document(
        text=entry['content'],
        metadata=metadata,
        metadata_separator="::",
        metadata_template="{key}=>{value}",
        text_template="Metadata: {metadata_str}\n-----\nContent: {content}",
    )
    return document.get_content(metadata_mode=MetadataMode.LLM)

# Read JSON file
with open('final_all_cases.json', 'r') as file:
    data = json.load(file)

# Create a folder to save the documents
output_folder = 'llama_documents'
os.makedirs(output_folder, exist_ok=True)

# Iterate over each entry/document in JSON
for entry in data:
    llama_document = create_llama_document(entry)
    # Name the file based on the document's ID
    file_name = os.path.join(output_folder, f"llama_document_{entry['id']}.txt")
    # Write the Llama index document to the file
    with open(file_name, 'w') as output_file:
        output_file.write(llama_document)
