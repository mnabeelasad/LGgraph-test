from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"F:\projects for job\branching test\Psychophysiology 8.2 Electrocortical measures.pdf")

data = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap = 20
)

chunks = splitter.split_documents(data)

print(chunks[0].page_content)
