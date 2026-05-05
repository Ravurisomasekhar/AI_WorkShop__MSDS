from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings

# Load PDF
loader = PyPDFLoader("tender.pdf")
docs = loader.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = splitter.split_documents(docs)

# Embeddings
embedding = OllamaEmbeddings(model="nomic-embed-text")

# Store in DB
db = Chroma.from_documents(
    chunks,
    embedding,
    persist_directory="./chroma_db"
)

print("Vector DB created successfully!")