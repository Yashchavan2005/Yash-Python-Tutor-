# ============================================================
# Project Name : Yash Python Tutor
# Author       : Yash Chavan
# Description  : AI Python Tutor using Ollama and Streamlit
# ============================================================

import streamlit as st
from ollama import Client


# ============================================================
# Step 1 : Configure GUI
# ============================================================

st.set_page_config(
    page_title="Yash Python Tutor",
    page_icon="🐍",
    layout="wide"
)


# ============================================================
# Step 2 : Connect to Ollama
# ============================================================

client = Client(
    host="http://localhost:11434"
)


# ============================================================
# Step 3 : Add CSS Styling
# ============================================================

st.markdown("""
<style>

.stApp {
    background-color: #0f172a;
    color: #ffffff;
}

.main .block-container {
    padding-top: 2rem;
}

.title {
    text-align: center;
    color: #a78bfa;
    font-size: 42px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 18px;
    margin-top: 8px;
}

[data-testid="stSidebar"] {
    background-color: #1e293b;
}

[data-testid="stSidebar"] * {
    color: #ffffff;
}

[data-testid="stChatMessage"] {
    background-color: #1e293b;
    color: #ffffff;
    border-radius: 12px;
    padding: 12px;
    border: 1px solid #334155;
}

[data-testid="stChatInput"] {
    background-color: #1e293b;
    border: 1px solid #8b5cf6;
    border-radius: 12px;
}

[data-testid="stChatInput"] textarea {
    color: #ffffff;
}

div.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 45px;
    font-weight: bold;
    background-color: #7c3aed;
    color: #ffffff;
    border: none;
    transition: 0.3s;
}

div.stButton > button:hover {
    background-color: #6d28d9;
    color: #ffffff;
    border: 1px solid #a78bfa;
}

hr {
    border-color: #475569;
}

[data-testid="stAlert"] {
    background-color: #1e293b;
    color: #ffffff;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# Step 4 : Display Dashboard Title
# ============================================================

st.markdown(
    '<div class="title">🐍 Yash Python Tutor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Powered Python Learning Assistant</div>',
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# Step 5 : Initialize Chat History
# ============================================================

SYSTEM_MESSAGE = {
    "role": "system",
    "content": (
        "You are Yash Python Tutor, an expert Python teacher. "
        "Teach Python programming to beginners. "
        "If the user asks in English, respond entirely in English. "
        "If the user asks in Marathi, respond in Marathi. "
        "Never respond in Hindi. "
        "If the user mixes English and Marathi, respond mainly "
        "in the language used by the user. "
        "Explain concepts step by step using simple language. "
        "Provide correct Python code examples when useful. "
        "Explain errors and help debug code clearly. "
        "Keep answers relevant to the user's question."
    )
}

if "messages" not in st.session_state:
    st.session_state.messages = [SYSTEM_MESSAGE.copy()]


# ============================================================
# Step 6 : Create Sidebar
# ============================================================

with st.sidebar:

    st.title("⚙️ Dashboard")

    st.write("Welcome to Yash Python Tutor!")

    st.divider()

    st.subheader("🤖 AI Model")

    st.info("Ollama: llama3.2:1b")

    st.subheader("📚 Python Topics")

    topics = [
        "Python Basics",
        "Variables and Data Types",
        "Operators",
        "Conditional Statements",
        "Loops",
        "Functions",
        "Lists and Tuples",
        "Dictionaries and Sets",
        "Object-Oriented Programming",
        "Exception Handling",
        "File Handling",
        "NumPy and Pandas",
        "Machine Learning"
    ]

    for topic in topics:
        st.markdown(f"- {topic}")

    st.divider()

    if st.button("🧹 Clear Chat"):

        st.session_state.messages = [SYSTEM_MESSAGE.copy()]

        st.rerun()

    st.caption("Developed by Yash Chavan")


# ============================================================
# Step 7 : Display Welcome Message
# ============================================================

if len(st.session_state.messages) == 1:

    st.info(
        "👋 Welcome to Yash Python Tutor!\n\n"
        "Ask any Python programming question below."
    )


# ============================================================
# Step 8 : Display Chat History
# ============================================================

for message in st.session_state.messages:

    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ============================================================
# Step 9 : Accept User Question
# ============================================================

Question = st.chat_input(
    "💬 Ask your Python question here..."
)


# ============================================================
# Step 10 : Generate AI Response
# ============================================================

if Question:

    # Display User Question
    with st.chat_message("user"):
        st.markdown(Question)

    # Save User Question
    st.session_state.messages.append({
        "role": "user",
        "content": Question
    })

    try:

        # Generate AI Response
        with st.chat_message("assistant"):

            with st.spinner(
                "🤖 Yash Python Tutor is thinking..."
            ):

                response = client.chat(
                    model="llama3.2:1b",
                    messages=st.session_state.messages,
                    options={
                        "temperature": 0.2,
                        "num_predict": 300
                    }
                )

                answer = response.message.content.strip()

            st.markdown(answer)

        # Save AI Response
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as error:

        st.error("❌ Ollama connection failed!")

        st.code(
            f"Error Type: {type(error).__name__}\n"
            f"Error Details: {error}"
        )

        st.info(
            "Check whether Ollama is running and "
            "the llama3.2:1b model is installed."
        )

