KnowSync-AI 🤖
AI Chatbot with Smart Document Search
KnowSync-AI is an advanced chatbot powered by LangChain and Groq AI, designed for seamless Q&A and intelligent PDF-based document retrieval. It can answer general questions and extract relevant information from uploaded PDFs using Retrieval-Augmented Generation (RAG).

🚀 Features
✔️ Conversational AI – Get instant answers from an AI chatbot.
✔️ Smart PDF Search – Upload PDFs and ask questions directly.
✔️ Memory Retention – Stores chat history for seamless interactions.
✔️ Multi-Model Support – Uses Llama 3.3 70B and Gemma 2-9B for responses.
✔️ Secure API Handling – Environment variables for API key storage.
✔️ Streamlit UI – Simple and user-friendly interface.

🛠️ Tech Stack
Python – Core language.

Streamlit – UI for chatbot and document search.

LangChain – AI prompt processing and retrieval.

Groq AI (Llama 3.3 70B, Gemma 2-9B) – AI models for response generation.

FAISS – Vector store for efficient document retrieval.

OpenAI API (Optional) – Can be integrated for alternative models.

PyPDF – Extracts text from PDFs for search.

📂 Project Structure
bash
Copy
Edit
KnowSync-AI/
│-- Chatbot.py                 # Main chatbot (General AI Q&A)
│-- pages/
│   ├── Smart PDF Assistant.py  # PDF-based AI search (RAG functionality)
│-- requirements.txt            # Dependencies
│-- .gitignore                  # Ignored files (venv, .env)
│-- .env                        # API keys (not included in GitHub)
│-- README.md                   # Project documentation
🔧 Installation & Setup
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/ArsalanArain20/KnowSync-AI.git
cd KnowSync-AI
2️⃣ Create a Virtual Environment
sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
3️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up API Keys
Create a .env file in the project directory and add:

sh
Copy
Edit
GROQ_API_KEY = 'your-groq-api-key'
OPENAI_API_KEY = 'your-openai-api-key'  # If using OpenAI
▶️ Running the Chatbot
To start the general AI chatbot:

sh
Copy
Edit
streamlit run Chatbot.py
To use PDF-based AI search (RAG retrieval):

sh
Copy
Edit
streamlit run pages/Smart\ PDF\ Assistant.py
📖 How to Use
🤖 AI Chatbot Mode (General Q&A)
Start Chatbot.py to chat with the AI.

Ask any question, and it will provide concise, structured answers.

📄 Smart PDF Search (RAG Mode)
Start Smart PDF Assistant.py to enable document-based AI search.

Upload a PDF file and ask questions related to its content.

The AI will extract relevant answers from the document.

🛠️ Future Enhancements
🔹 Multi-PDF Search – Query multiple PDFs at once.
🔹 Voice Input & Output – Speech-to-text and text-to-speech features.
🔹 Chatbot Personalization – Train on custom datasets for industry-specific use.
🔹 Cloud Deployment – Deploy on AWS/GCP for online access.

🤝 Contributing
Want to improve KnowSync-AI?
Fork the repo, make changes, and submit a pull request.

📜 License
This project is open-source and available under the MIT License.

🌟 Star this repo if you find it useful! 🚀
✅ Changes from Previous Version:
✔️ Added PDF-Based AI Search (RAG)
✔️ Updated Project Structure
✔️ Clearer Setup Instructions