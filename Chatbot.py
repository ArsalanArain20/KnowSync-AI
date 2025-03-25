# Import Packages
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
import os

# Load environment variables
load_dotenv()
st.set_page_config(page_title="AI Chatbot Assistant", page_icon="🤖")
st.header("🤖 NeuraBot - Ask Me Anything! 💬")

# Setup a session state variable to hold chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history before new input is processed
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
user_input = st.chat_input("Ask from AI")

# Define AI model
Model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
    api_key=os.getenv("GROQ_API_KEY"),
)

if user_input:
    # Append user input to chat history before generating response
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Standard chatbot response (without retrieval)
    general_prompt = ChatPromptTemplate.from_template("""
        You are a knowledgeable AI assistant. Provide accurate, concise, and well-structured answers.  
        Avoid unnecessary introductions and directly answer the question.  

        User Question: {user_prompt}
    """)
    
    parser = StrOutputParser()
    chain = general_prompt | Model | parser
    result = chain.invoke({"user_prompt": user_input})

    # Ensure result is always a string
    response_text = result if isinstance(result, str) else result.get("result", "⚠️ No response received!")

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(response_text)

    # Append AI response to chat history
    st.session_state["messages"].append({"role": "assistant", "content": response_text})
