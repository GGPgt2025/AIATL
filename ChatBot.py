import requests
from langchain.document_loaders import HTMLTextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# Fetch the content of the URL
url = "https://www.sec.gov/ix?doc=/Archives/edgar/data/320193/000032019323000106/aapl-20230930.htm"
response = requests.get(url)
html_content = response.text

# Load content from the URL using HTMLTextLoader
loader = HTMLTextLoader(html_content)
documents = loader.load()

# Text splitting
text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=10)
texts = text_splitter.split_documents(documents)

# Embeddings
persist_directory = "./storage"
embeddings = OpenAIEmbeddings()
vectordb = Chroma.from_documents(documents=texts, embedding=embeddings, persist_directory=persist_directory)
vectordb.persist()

# Chatting with PDF documents
retriever = vectordb.as_retriever()
llm = ChatOpenAI(model_name='gpt-4')
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

while True:
    user_input = input("Enter a query: ")
    if user_input == "exit":
        break

    query = f"###Prompt {user_input}"
    try:
        llm_response = qa(query)
        print(llm_response["result"])
    except Exception as err:
        print('Exception occurred. Please try again', str(err))



# #LangChain for PDF

# #Using pdf uploader to pass in 10k financial pdf
# import os
# from langchain.document_loaders import PyMuPDFLoader

# os.environ['OPENAI_API_KEY'] = 'ENTER YOUR API KEY'

# loader = PyMuPDFLoader("blank.pdf")
# documents = loader.load()


# #Text-splitters
# from langchain.text_splitter import RecursiveCharacterTextSplitter

# text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=10)
# texts = text_splitter.split_documents(documents)


# #Embeddings
# from langchain.vectorstores import Chroma
# from langchain.embeddings import OpenAIEmbeddings

# persist_directory = "./storage"
# embeddings = OpenAIEmbeddings()
# vectordb = Chroma.from_documents(documents=texts, 
#                                  embedding=embeddings,
#                                  persist_directory=persist_directory)
# vectordb.persist()

# #Chatting w/ pdf documents
# from langchain.chat_models import ChatOpenAI
# from langchain.chains import RetrievalQA

# retriever = vectordb.as_retriever()
# llm = ChatOpenAI(model_name='gpt-4')
# qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
# while True:
#         user_input = input("Enter a query: ")
#         if user_input == "exit":
#             break

#         query = f"###Prompt {user_input}"
#         try:
#             llm_response = qa(query)
#             print(llm_response["result"])
#         except Exception as err:
#             print('Exception occurred. Please try again', str(err))
