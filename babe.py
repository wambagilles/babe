import getpass
import os

from langchain.chat_models import init_chat_model
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]


#from langchain_chroma import Chroma
from langchain_community.vectorstores import Chroma
import getpass
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter # Importing text splitter from Langchain

from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")









prompt_template = """
You are an intelligent assistant that answers questions specifically about Gilles and Gabi.
Use only the information provided in the context below to answer the question accurately and concisely.

Context:
{context}

Question: {question}
Answer:
"""

prompt = PromptTemplate(
     input_variables=["context", "question"],
     template=prompt_template
)

loader2 = TextLoader(r"Discussion WhatsApp avec Babe.txt", encoding="utf-8")
loader1 = TextLoader(r"Discussion WhatsApp avec Elisabeth Gabriella Wafo Mamno.txt", encoding="utf-8")


text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

docs = loader1.load()
docs+= loader2.load()
split_docs = text_splitter.split_documents(docs)


# Load a QA chain
qa_chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)

# Ask a question
#query = "who are Gabriella and GM?"
#response = qa_chain.run(input_documents=split_docs, question=query)

#print("Answer:", response)




import streamlit as st

# Assume qa_chain is already initialized elsewhere and available here
# from your_module import qa_chain

st.title("Gilles & Gabi Love QA")

# Upload a text file



# Ask a question
question = st.text_input("Ask a question about Gilles and Gabi:")
if question:
    response = qa_chain.run(input_documents=split_docs, question=question)
    st.markdown("**Question:**")
    st.write(question)
    st.markdown("**Answer:**")
    st.write(response)

