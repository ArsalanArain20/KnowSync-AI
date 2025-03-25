import streamlit as st  
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS 
from langchain_groq import ChatGroq
import tempfile
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.set_page_config(page_title="PDF Search", layout="wide")
st.header("📄 PDF-Based AI Search")

@st.cache_resource
def get_vector_store(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()

    vectorstore = FAISS.from_documents(texts, embeddings)
    return vectorstore

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

vector_store = None
if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_pdf_path = temp_file.name
    st.success(f"✅ File uploaded: {uploaded_file.name}")

    vector_store = get_vector_store(temp_pdf_path)

user_input = st.chat_input('Ask a question from the PDF...')

if user_input and vector_store:
    st.chat_message('user').markdown(user_input)

    Model = ChatGroq(
        model="gemma2-9b-it",
        temperature=0.3,
        api_key=os.getenv("GROQ_API_KEY")
    )

    retrieval_prompt = ChatPromptTemplate.from_template("""
        You are an AI assistant specialized in retrieving accurate answers from a given document.  
        Use only the provided document as your source and do not make up information.  
        Answer concisely and provide references if applicable.  

        User Question: {user_prompt}
    """)

    chain = RetrievalQA.from_chain_type(
        llm=Model,
        retriever=vector_store.as_retriever(search_kwargs={'k': 3}),
        return_source_documents=True
    )

    result = chain.invoke({'query': user_input})
    response_text = result.get("result", "⚠️ No response received!")

    st.chat_message('assistant').markdown(response_text)
