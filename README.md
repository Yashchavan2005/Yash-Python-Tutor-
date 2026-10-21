# 🐍 Yash Python Tutor

### AI-Powered Python Learning Chatbot using Ollama and Streamlit

## 📌 Project Overview

**Yash Python Tutor** is an AI-powered Python learning chatbot developed using Python, Ollama, and Streamlit.

The project helps students learn Python programming by asking questions and receiving AI-generated explanations. It provides a terminal-based chatbot and a web-based dashboard.

The chatbot uses the **Llama 3.2:1B** language model through Ollama to generate responses.

## 🎯 Project Objectives

* Help beginners learn Python programming.
* Provide explanations of Python concepts.
* Answer programming questions using an AI language model.
* Support English and Marathi responses.
* Provide a user-friendly Streamlit dashboard.
* Maintain conversation history during a session.
* Help users understand Python errors and programming concepts.

## ✨ Features

* 🤖 AI-powered Python chatbot
* 🐍 Python programming assistance
* 🌐 English and Marathi language instructions
* 💬 Interactive terminal-based chatbot
* 🖥️ Streamlit web dashboard
* 🧠 Conversation context using message history
* 🎨 Custom dashboard styling
* 🧹 Clear Chat functionality
* 📚 Python learning topics
* ⚡ Local AI inference using Ollama

## 🛠️ Technologies Used

| Technology   | Purpose                       |
| ------------ | ----------------------------- |
| Python       | Core programming language     |
| Ollama       | Runs the local language model |
| Llama 3.2:1B | Generates AI responses        |
| Streamlit    | Builds the web dashboard      |
| Git          | Version control               |
| GitHub       | Source code hosting           |

## 📂 Project Structure

```text
Yash_Python_Tutor/
│
├── 1_LLM_Chatbot.py
├── 2_GUI_Addition_Streamlit.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── screenshots/
    └── dashboard.png
```

### File Description

* **`1_LLM_Chatbot.py`** — Runs the AI chatbot in the terminal.
* **`2_GUI_Addition_Streamlit.py`** — Runs the interactive Streamlit dashboard.
* **`README.md`** — Contains project documentation and setup instructions.
* **`requirements.txt`** — Lists the required Python packages.
* **`.gitignore`** — Specifies files and folders Git should ignore.
* **`screenshots/`** — Stores screenshots of the application.

## ⚙️ Prerequisites

Before running the project, install the following:

1. Python
2. Ollama
3. Llama 3.2:1B model
4. Required Python libraries

Check Python:

```bash
python --version
```

Check Ollama:

```bash
ollama --version
```

## 📥 Installation

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### Step 2: Open the Project Folder

```bash
cd Yash_Python_Tutor
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

**Windows CMD:**

```bash
.venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 6: Download the Ollama Model

First, ensure Ollama is installed and running.

Then execute:

```bash
ollama pull llama3.2:1b
```

Check whether the model is available:

```bash
ollama list
```

## 🚀 How to Run the Project

### Option 1: Terminal Chatbot

Run:

```bash
python 1_LLM_Chatbot.py
```

Example:

```text
==================================================
           Yash Python Tutor
==================================================
Welcome! Ask me Python programming questions.
Type 'exit' to stop the chatbot.

You: What is a Python variable?

Yash Python Tutor: A variable is a name used to store a value
in Python.
```

To stop the chatbot, type:

```text
exit
```

### Option 2: Streamlit Web Dashboard

Run:

```bash
python -m streamlit run 2_GUI_Addition_Streamlit.py
```

Streamlit will open the application in your browser.

You can enter Python questions in the chat interface and view the AI-generated responses.

## 📚 Python Topics

The chatbot can help with topics such as:

* Python Basics
* Variables and Data Types
* Operators
* Conditional Statements
* Loops
* Functions
* Lists and Tuples
* Dictionaries and Sets
* Object-Oriented Programming
* Exception Handling
* File Handling
* NumPy and Pandas
* Machine Learning

The quality and accuracy of answers depend on the language model and the question asked.

## 🧠 How It Works

1. The user enters a Python programming question.
2. Python stores the question in the conversation history.
3. The application sends the messages to Ollama.
4. The Llama 3.2:1B model generates a response.
5. The application displays the response to the user.
6. The conversation history is updated for subsequent questions.
