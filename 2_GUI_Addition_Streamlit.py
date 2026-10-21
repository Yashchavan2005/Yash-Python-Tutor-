# ============================================================
# Project Name : Yash Python Tutor
# Author       : Yash Chavan
# Description  : AI Python Tutor using Groq and Streamlit
# ============================================================

import streamlit as st
from groq import Groq


# ============================================================
# Step 1 : Configure GUI
# ============================================================

st.set_page_config(
    page_title="Yash Python Tutor",
    page_icon="🐍",
    layout="wide"
)


# ============================================================
# Step 2 : Configure Groq AI
# ============================================================

try:
    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )
except (KeyError, FileNotFoundError):
    st.error("Groq API Key not found in Streamlit Secrets.")
    st.stop()


# ============================================================
# Step 3 : Add CSS Styling
# ============================================================

st.markdown("""
<style>

/* Main Background */
.stApp {
    background-color: #0f172a;
    color: #ffffff;
}

/* Main Content */
.main .block-container {
    padding-top: 2rem;
}

/* Dashboard Title */
.title {
    text-align: center;
    color: #a78bfa;
    font-size: 42px;
    font-weight: bold;
}

/* Student Caption */
.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 18px;
    margin-top: 8px;
}

/* Sidebar Background */
[data-testid="stSidebar"] {
    background-color: #1e293b;
}

/* Sidebar Text */
[data-testid="stSidebar"] * {
    color: #ffffff;
}

/* Chat Messages */
[data-testid="stChatMessage"] {
    background-color: #1e293b;
    color: #ffffff;
    border-radius: 12px;
    padding: 12px;
    border: 1px solid #334155;
}

/* Chat Input */
[data-testid="stChatInput"] {
    background-color: #1e293b;
    border: 1px solid #8b5cf6;
    border-radius: 12px;
}

/* Chat Input Text */
[data-testid="stChatInput"] textarea {
    color: #ffffff;
}

/* Buttons */
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

/* Button Hover */
div.stButton > button:hover {
    background-color: #6d28d9;
    color: #ffffff;
    border: 1px solid #a78bfa;
}

/* Divider */
hr {
    border-color: #475569;
}

/* Information Boxes */
[data-testid="stAlert"] {
    background-color: #1e293b;
    color: #ffffff;
    border-radius: 10px;
}

/* Spinner */
.stSpinner {
    color: #a78bfa;
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
    '<div class="subtitle">Student: Yash Chavan</div>',
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# Step 5 : Initialize Chat History
# ============================================================

SYSTEM_MESSAGE = {
    "role": "system",
    "content": (
        "You are Yash Python Tutor, an expert Python programming teacher. "

        "LANGUAGE RULES: "
        "If the user asks in English, answer entirely in English. "
        "If the user asks in Marathi, answer in Marathi. "
        "Never answer in Hindi. "
        "Do not translate the answer into another language unless requested. "
        "If the user mixes English and Marathi, respond mainly in the "
        "language used by the user. "
        "Keep Python keywords, code, and technical terms in English "
        "where appropriate. "

        "TEACHING RULES: "
        "Explain Python concepts step by step for beginners. "
        "Provide correct Python code examples whenever useful. "
        "Explain errors clearly and help users debug their code. "
        "Keep answers simple, clear, and easy to understand."
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

    st.info("Groq AI: llama-3.1-8b-instant")

    st.subheader("📚 Python Topics")

    st.markdown("""
    - Python Basics
    - Variables and Data Types
    - Operators
    - Conditional Statements
    - Loops
    - Functions
    - Lists and Tuples
    - Dictionaries and Sets
    - Object-Oriented Programming
    - Exception Handling
    - File Handling
    - NumPy and Pandas
    - Machine Learning
    """)

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
        "Ask your Python programming questions below."
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
# Step 10 : Generate AI Response using Groq
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

                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=st.session_state.messages,
                    temperature=0.5,
                    max_tokens=2048
                )

                answer = response.choices[0].message.content

                if not answer:
                    answer = "No response received from AI."

            st.markdown(answer)

        # Save AI Response
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as error:

        st.error(
            "Could not get a Groq AI response. "
            "Please check your API configuration."
        )

        st.caption(f"Error type: {type(error).__name__}")
