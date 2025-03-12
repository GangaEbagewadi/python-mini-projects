<h1>🤖 AI Chatbot with Smart To-Do List & PDF Summarization</h1>

"🚀 A Streamlit-powered AI chatbot using Google Gemini API with features like a Smart To-Do List and PDF Summarization."
____________________________________________________________________________________________________________________________________________________________________
📌 Features

✅ AI Chatbot powered by Google Gemini API

✅ Smart To-Do List Generator

✅ PDF Summarization (Extracts and summarizes text from PDFs)

✅ User-Friendly Chat Interface
____________________________________________________________________________________________________________________________________________________________________
📸 Screenshots

Find output screenshots in the output-screenshot folder.
____________________________________________________________________________________________________________________________________________________________________
🔑 Setting Up Google Gemini API Key

1️⃣ Get API Key from Google AI Studio

Go to Google AI Studio and sign in.

Navigate to API Keys in the sidebar.

Click Generate API Key and copy it.

2️⃣ Store API Key in Your System

Open PowerShell and run:

cd "your_project_folder_path_here"

$env:GOOGLE_API_KEY = "your_actual_api_key"

echo $env:GOOGLE_API_KEY   # Check if API Key is stored
____________________________________________________________________________________________________________________________________________________________________
⚡ Installation & Usage

🔹 Clone the Repository

git clone https://github.com/GangaEbagewadi/python-mini-project.git

cd python-mini-project
____________________________________________________________________________________________________________________________________________________________________
🔹 Install Dependencies

pip install -r requirements.txt
______________________________________________________________________________________________________________________________________________________________
🔹 Run the Application

streamlit run chatbott.py
____________________________________________________________________________________________________________________________________________________________________
🔥 How It Works

The AI Chatbot interacts with users using Google Gemini API.

PDF Summarization extracts and summarizes text from uploaded PDF files.

The Smart To-Do List organizes tasks with priorities, deadlines, and dependencies.
____________________________________________________________________________________________________________________________________________________________________
🚀 Future Enhancements

✅ Add speech-to-text support

✅ Improve UI styling for a better experience

✅ Save chat history to a database
____________________________________________________________________________________________________________________________________________________________________
📜 License

This project is open-source. Feel free to modify and improve it! 🎉
