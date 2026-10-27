🤖 Q&A Chatbot

A simple conversational chatbot built using Python, Streamlit, LangChain, and Groq.

✨ Features

* Interactive chat interface
* Maintains conversation history during the current Streamlit session
* Clear Chat button to reset the conversation
* Uses a Groq-hosted language model through LangChain

🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Groq API

📁 Project Structure

qna-chatbot/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md

🚀 Getting Started

1. Clone the repository

git clone https://github.com/DivyanshuJain2006/qna-chatbot.git
cd qna-chatbot

2. Create a virtual environment

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Configure your API key

Create a .env file in the project directory and add your Groq API key:

GROQ_API_KEY=your_groq_api_key

Replace the placeholder with your actual API key.

Important: Never upload your .env file or API key to GitHub.

5. Run the application

streamlit run app.py

📚 Learning Goals

This project was built while learning how to create conversational AI applications using LangChain, Streamlit, and Groq.

🔮 Future Improvements

* Add API error handling
* Improve the chat interface
* Add persistent conversation storage
* Add support for configurable models