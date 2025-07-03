# MediBuddy
🩺 MediBuddy
MediBuddy is an AI-powered web application that transforms complex medical documents into clear, patient-friendly summaries.
Features:
a. Upload clinical notes, discharge summaries, or research papers (PDF)
b. Automatically generate simple summaries covering diseases, symptoms, medications, and advice
c. Download summaries as text files for easy sharing or reference
d. Built using Streamlit for the frontend and LangChain, Groq LLM, Hugging Face embeddings, and FAISS for backend retrieval and summarization

# Tech Stack
Frontend: Streamlit
Backend: LangChain, Groq LLM (llama-3.3-70b-versatile)
Embeddings: Hugging Face (all-MiniLM-L6-v2)
Vector DB: FAISS

# Installation
a. Clone the repository
b. Create a virtual environment
c. Install required dependencies
d. Set up environment variables
   Create a .env file in the project root directory and add your Groq API key
e. Then:
   Open the local URL shown in your terminal (usually http://localhost:8501)
   Upload a PDF medical report or paper
   Click Generate Summary
   View or download your AI-generated, patient-friendly summary
