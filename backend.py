import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_groq.chat_models import ChatGroq
from langchain.chains import RetrievalQA

# ✅ Load environment variables from .env
load_dotenv()

def generate_summary(pdf_path, model="llama-3.3-70b-versatile"):
    # 🔐 Load Groq API key from .env
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("❌ GROQ_API_KEY not found in .env file.")
    
    os.environ["GROQ_API_KEY"] = groq_api_key

    # 📄 Load PDF content
    loader = PyMuPDFLoader(pdf_path)
    docs = loader.load()
    if not docs:
        raise ValueError("❌ PDF is empty or unreadable.")

    # ✂ Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)
    if not chunks:
        raise ValueError("❌ No text chunks generated from PDF.")

    # 🧠 Generate embeddings
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # 📦 Store in FAISS vector DB
    vectorstore = FAISS.from_documents(chunks, embedding)
    retriever = vectorstore.as_retriever()

    # 🤖 Set up Groq LLM
    llm = ChatGroq(model=model, temperature=0.3)

    # 🔗 Build RAG chain
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    # ❓ Query
    query = (
        "Summarize this medical document in patient-friendly language. "
        "Include disease, symptoms, medications, and advice."
    )
    response = qa_chain.invoke(query)

    return response["result"]