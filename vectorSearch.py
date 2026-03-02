# FILENAME: vectorSearch.py
# AUTHOR:   Reg Gonzalez
# CONTACT:  regmckie@gmail.com
# DATE:     3/1/2026
#
# FILE DESCRIPTION:
# This file provides logic for embedding documents and looking them up (e.g., vectorizing).
# Vector store is a database; it's going to be hosted locally on our computer using ChromaDB.
# Using vectorization allows you to look up relevant information to pass to the model.
# The model then uses that data to give us relevant replies.


from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd


df = pd.read_csv("IMDB-Movie-Data.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chroma_langchain_db"  # Location to store our vector db
add_documents = not os.path.exists(db_location)  # Check whether the path exists so that we don't have to redo it everytime we run this code

if add_documents:
    documents = []
    ids = []  # Storing this b/c when we create this data in the vector store, we need a list of docs & associated IDs

    for counter, row in df.iterrows():
        document = Document(
            page_content = row["Title"] + " " + row["Genre"] + " " + row["Description"],  # The actual information you want to query on
            metadata = {"rank": row["Rank"]},  # Info to grab along, but won't be stuff you query on
            id=str(counter)
        )
        ids.append(str(counter))
        documents.append(document)

vector_store = Chroma(
    collection_name = "movie_descriptions",
    persist_directory = db_location,  # Done so that we don't need to keep regenerating the Chroma db
    embedding_function = embeddings
)

# Only doing this if the db_location didn't exist. If it did already exist, we wouldn't need to add the docs again.
if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)

retriever = vector_store.as_retriever(
    search_kwargs = {"k": 5}  # Look up 5 relevant reviews and pass them to the LLM
)
