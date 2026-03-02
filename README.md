# Local-AI-Agent

FILENAME: README.txt
AUTHOR: Reg Gonzalez
CONTACT: regmckie@gmail.com
DATE: 3/1/2026

------------------------------------------------------------------------------------------------------------------------------------------

PROJECT DESCRIPTION:

This project builds a local AI agent. For this, we'll use Ollama, Langchain, and ChromaBD, the latter of which is used as our vector search database because we are going to be using retrieval augmented generation (RAG). RAG essentially brings in relevant information from our source file, in this case a CSV file, for our model. This program builds an AI agent that acts as an expert about different movies. You can ask it film-related questions and it will answer by giving you the most relevant answers it can find in the dataset.

------------------------------------------------------------------------------------------------------------------------------------------

FILE DESCRIPTIONS:

main.py:
This file models in our language model (llama3.2 from Ollama), creates a prompt for the model (i.e., telling it it's an expert on movies and will be answering movie-related questions, invokes the chain that combines multiple things together to run our LLM, and continually asks the user to type in a question that it will answer (the user should type in "q" if they want to quit the program).

vectorSearch.py:
This file provides the logic for embedding documents and looking them up (i.e., vectorizing). Vector store is a database; it's going to be hosted locally in our computer using ChromaDB. Using vectorization allows you to look up relevant information to pass to the model. The model then uses that data to give us relevant replies. This file reads in the CSV file for the movie descriptions, creates the embeddings using the mxbai-embed-large model, and creates a location to store our vector db (if none exists).
