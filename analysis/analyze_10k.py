import requests
from langchain.document_loaders import UnstructuredHTMLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# Function to fetch the 10-K filing data
def fetch_10k_data(symbol):
    # Fetch the latest 10-K filing URL using the Edgar API
    edgar_api_url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={symbol}&type=10-K&dateb=&owner=exclude&count=1"
    try:
        edgar_api_response = requests.get(edgar_api_url)
        edgar_api_response.raise_for_status()  # Raise an HTTPError for bad responses
        edgar_api_data = edgar_api_response.json()
    except requests.exceptions.RequestException as req_err:
        print(f"Error during request to Edgar API: {req_err}")
        return None
    except ValueError as json_err:
        print(f"Error decoding JSON from Edgar API response: {json_err}")
        return None

    # Print the entire Edgar API response for inspection
    print(edgar_api_data)

    # Check if the response contains filing details
    if 'filings' in edgar_api_data and 'filings' in edgar_api_data['filings']:
        latest_filing = edgar_api_data['filings']['filings'][0]
        filing_url = latest_filing['href']

        # Fetch the content of the latest 10-K filing
        try:
            response = requests.get(filing_url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.text
        except requests.exceptions.RequestException as req_err:
            print(f"Error during request to fetch 10-K filing: {req_err}")
            return None
    else:
        print(f"No filing details found in the Edgar API response for symbol {symbol}.")
        return None
        
# Function to analyze 10-K
def analyze_10k(html_content):

    # Load content from the URL using UnstructuredHTMLTextLoader
    loader = UnstructuredHTMLLoader(html_content)
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

