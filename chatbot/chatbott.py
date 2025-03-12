#pip install google-generativeai

# import os
# import streamlit as st
# import google.generativeai as genai

# # Load API Keyr
# API_KEY = os.getenv("GOOGLE_API_KEY")

# if not API_KEY:
#     st.error("Error: GOOGLE_API_KEY is not set!")
#     st.stop()

# # Configure the Gemini API
# genai.configure(api_key=API_KEY)

# # Select a valid model
# MODEL_NAME = "models/gemini-1.5-pro-latest"

# # Streamlit UI
# st.title("🤖 AI Chatbot using Google Gemini")

# # Chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display previous chat messages
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # User input
# user_input = st.chat_input("Type your message here...")

# if user_input:
#     # Display user message
#     st.session_state.messages.append({"role": "user", "content": user_input})
#     with st.chat_message("user"):
#         st.markdown(user_input)

#     try:
#         # Get AI response
#         model = genai.GenerativeModel(MODEL_NAME)
#         response = model.generate_content(user_input)

#         # Display AI response
#         ai_message = response.text if response else "I'm sorry, I couldn't understand that."
#         st.session_state.messages.append({"role": "assistant", "content": ai_message})
        
#         with st.chat_message("assistant"):
#             st.markdown(ai_message)

#     except Exception as e:
#         st.error(f"Error: {str(e)}")














# import os
# import time
# import streamlit as st
# import google.generativeai as genai
# import PyPDF2

# # Load API Key
# API_KEY = os.getenv("GOOGLE_API_KEY")
# if not API_KEY:
#     st.error("Error: GOOGLE_API_KEY is not set!")
#     st.stop()

# genai.configure(api_key=API_KEY)
# MODEL_NAME = "models/gemini-1.5-pro-latest"

# # Streamlit Dark Mode Fix
# def set_dark_mode():
#     st.markdown(
#         """
#         <style>
#         body { background-color: #121212; color: white; }
#         .stTextInput, .stTextArea, .stButton, .stFileUploader { color: black; }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

# set_dark_mode()

# # UI Layout
# st.title("🤖 AI Chatbot using Google Gemini")
# st.sidebar.title("⚙️ Features")

# # Chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display previous messages
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # File Upload Section
# st.sidebar.subheader("📂 Upload File for Analysis")
# uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type=["pdf"])

# if uploaded_file:
#     pdf_reader = PyPDF2.PdfReader(uploaded_file)
#     text = "\n".join(page.extract_text() for page in pdf_reader.pages if page.extract_text())
#     st.sidebar.text_area("Extracted Text", text[:500] + "..." if len(text) > 500 else text, height=200)
    
#     if st.sidebar.button("Summarize PDF"):
#         try:
#             model = genai.GenerativeModel(MODEL_NAME)
#             response = model.generate_content(f"Summarize this document: {text[:4000]}")
#             summary = response.text.strip()
#             st.subheader("📌 Summary")
#             st.write(summary)
#         except Exception as e:
#             st.error(f"Error: {str(e)}")

# # To-Do List Feature
# st.sidebar.subheader("✅ To-Do List Generator")
# todo_input = st.sidebar.text_area("Enter tasks you want to organize:")

# def format_todo_list(raw_tasks):
#     tasks = raw_tasks.split("\n")
#     formatted = "\n".join([f"- {task.strip()} (Due in 24 hours)" for task in tasks if task.strip()])
#     return formatted

# if st.sidebar.button("Generate To-Do List"):
#     if todo_input:
#         try:
#             model = genai.GenerativeModel(MODEL_NAME)
#             to_do_prompt = f"Organize this into a structured to-do list with deadlines: {todo_input}"
#             response = model.generate_content(to_do_prompt)
#             formatted_tasks = format_todo_list(response.text.strip())
#             st.subheader("📝 To-Do List")
#             st.write(formatted_tasks)
#         except Exception as e:
#             st.error(f"Error: {str(e)}")

# # User Chat Input
# user_input = st.chat_input("Type your message here...")

# if user_input:
#     st.session_state.messages.append({"role": "user", "content": user_input})
#     with st.chat_message("user"):
#         st.markdown(user_input)

#     try:
#         model = genai.GenerativeModel(MODEL_NAME)
#         response = model.generate_content(user_input)
#         ai_message = response.text.strip() if response else "I'm sorry, I couldn't understand that."
#         st.session_state.messages.append({"role": "assistant", "content": ai_message})
#         with st.chat_message("assistant"):
#             st.markdown(ai_message)
#     except Exception as e:
#         st.error(f"Error: {str(e)}")






















import os
import time
import streamlit as st
import google.generativeai as genai
import PyPDF2

# Load API Key
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    st.error("Error: GOOGLE_API_KEY is not set!")
    st.stop()

genai.configure(api_key=API_KEY)
MODEL_NAME = "models/gemini-1.5-pro-latest"

# Streamlit Dark Mode Fix
def set_dark_mode():
    st.markdown(
        """
        <style>
        body { background-color: #121212; color: white; }
        .stTextInput, .stTextArea, .stButton, .stFileUploader { color: black; }
        </style>
        """,
        unsafe_allow_html=True,
    )

set_dark_mode()

# UI Layout
st.title("🤖 AI Chatbot using Google Gemini")
st.sidebar.title("⚙️ Features")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# File Upload Section
st.sidebar.subheader("📂 Upload File for Analysis")
uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = "\n".join(page.extract_text() for page in pdf_reader.pages if page.extract_text())
    st.sidebar.text_area("Extracted Text", text[:500] + "..." if len(text) > 500 else text, height=200)
    
    if st.sidebar.button("Summarize PDF"):
        try:
            model = genai.GenerativeModel(MODEL_NAME)
            response = model.generate_content(f"Summarize this document: {text[:4000]}")
            summary = response.text.strip()
            st.subheader("📌 Summary")
            st.write(summary)
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Smart AI To-Do List Features
st.sidebar.subheader("✅ Smart AI To-Do List Generator")
todo_input = st.sidebar.text_area("Enter tasks you want to organize:")

if st.sidebar.button("Generate Smart To-Do List"):
    if todo_input:
        try:
            model = genai.GenerativeModel(MODEL_NAME)
            to_do_prompt = f"Organize this into a structured to-do list with deadlines, priorities, and dependencies: {todo_input}"
            response = model.generate_content(to_do_prompt)
            formatted_tasks = response.text.strip()
            
            st.subheader("📝 AI-Generated To-Do List")
            st.write(formatted_tasks)
        except Exception as e:
            st.error(f"Error: {str(e)}")

# User Chat Input
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(user_input)
        ai_message = response.text.strip() if response else "I'm sorry, I couldn't understand that."
        st.session_state.messages.append({"role": "assistant", "content": ai_message})
        with st.chat_message("assistant"):
            st.markdown(ai_message)
    except Exception as e:
        st.error(f"Error: {str(e)}")

