import os
from langchain_community.document_loaders import FireCrawlLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain_community.embeddings import GPT4AllEmbeddings

model_name = "all-MiniLM-L6-v2.gguf2.f16.gguf"
gpt4all_kwargs = {'allow_download': 'True'}

def createVectorDB(urls: list, chunkSize: int, chunkOverlap: int, apiKey: str):
    # Scrape through specified URLs    
    #TODO
    docs = [FireCrawlLoader(api_key=apiKey, url=url, mode="scrape")]

    # Split documentss 
    #TODO
    TEXTSPLITTER = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=chunkSize,
        chunk_overlap=chunkOverlap
    )
    docs_split_by_chunks = TEXTSPLITTER.split_documents(docs_list)

    # Split documents by chunks
    #TODO
    docs_filtered=[]
    for dov in docs_split_by_chunks:

    # Filter out complex metadata and ensure proper document formatting
    #TODO
    
    # Add to vectorDB and save as retriever as a variable
    #TODO

    raise NotImplementedError