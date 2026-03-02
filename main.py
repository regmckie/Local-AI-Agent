# FILENAME: main.py
# AUTHOR:   Reg Gonzalez
# CONTACT:  regmckie@gmail.com
# DATE:     3/1/2026
#
# FILE DESCRIPTION:
# The goal of this program is to build a local AI agent. For this, we'll use Ollama, Langchain, and ChromaDB,
# the latter of which is used as our vector search database because we are going to be using retrieval augmented generation
# (RAG) for this app. RAG essentially brings in relevant information from a source file, in this case a CSV, for our model.
# This program builds an AI agent that acts as an expert about different movies. You can ask it film-related questions,
# and it will answer by giving you the most relevant answers it can find in the dataset.


# Langchain is a framework that makes it easier to work with LLMs
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vectorSearch import retriever


model = OllamaLLM(model="llama3.2")

template = """
You are an expert in answering questions about different movies.

Here are some relevant descriptions: {descriptions}

Here to the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

# Invokes the entire chain that combines multiple things together to run our LLM
chain = prompt | model

while True:
    print("\n\n-------------------------------------------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question == "q":
        break
    descriptions = retriever.invoke(question)  # Use the user's question and retrieve relevant docs to answer it
    result = chain.invoke({"descriptions": descriptions, "question": question})
    print(result)