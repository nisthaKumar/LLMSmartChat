# bring in our LLAMA_CLOUD_API_KEY
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex

load_dotenv()

# bring in deps
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader

# set up parser
parser = LlamaParse(
    result_type="markdown"  # "markdown" and "text" are available
)

# use SimpleDirectoryReader to parse our file
file_extractor = {".pdf": parser}
documents = SimpleDirectoryReader(input_files=['handbook.pdf'], file_extractor=file_extractor).load_data()
#print(documents)

index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

# query the engine
query = "What is their vacation policy?"
response = query_engine.query(query)
print(response)