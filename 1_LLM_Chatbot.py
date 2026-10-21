# ============================================================
# Project Name : Yash Python Tutor
# Author       : Yash Chavan
# Date         : 21/10/2026
# Description  : AI-based Python Programming Chatbot using
#                Ollama and the Llama 3.2:1b model.
# ============================================================


from ollama import chat


# ============================================================
# Step 1 : Initialize Chat History
# Function Name : Initialize Messages
# Description   : Store the system instruction that defines
#                 the role and behavior of the AI chatbot.
# Input         : System role and instruction
# Output        : Initialized messages list
# ============================================================

messages = [
    {
        "role": "system",
        "content": (
            "You are Yash Python Tutor, an expert Python "
            "programming teacher. Explain Python concepts "
            "step by step in simple language. "
            "If the user asks in English, answer in English. "
            "If the user asks in Marathi, answer in Marathi. "
            "Never answer in Hindi."
        )
    }
]


# ============================================================
# Step 2 : Display Chatbot Information
# Function Name : Display Welcome Message
# Description   : Display the chatbot name and instructions
#                 when the program starts.
# Input         : None
# Output        : Welcome message displayed on the terminal
# ============================================================

print("=" * 50)
print("           Yash Python Tutor")
print("=" * 50)

print("Welcome! Ask me Python programming questions.")
print("Type 'exit' to stop the chatbot.")


# ============================================================
# Step 3 : Accept User Input
# Function Name : Input Question
# Description   : Continuously accept questions from the user
#                 until the user enters 'exit'.
# Input         : User's question
# Output        : User question stored in the Question variable
# ============================================================

while True:

    print("=" * 50)

    # Accept the user's question and remove extra spaces
    Question = input("\nYou: ").strip()


    # ========================================================
    # Step 4 : Stop the Chatbot
    # Description : Stop program execution when the user
    #               enters 'exit'.
    # Input       : 'exit'
    # Output      : Thank-you message and program termination
    # ========================================================

    if Question.lower() == "exit":

        print("\nThank you for using Yash Python Tutor!")

        break


    # ========================================================
    # Step 5 : Ignore Empty Input
    # Description : Skip processing if the user enters an
    #               empty line or only spaces.
    # Input       : Empty string
    # Output      : Continue to the next loop iteration
    # ========================================================

    if not Question:

        continue


    # ========================================================
    # Step 6 : Store User Message
    # Description : Append the user's question to the message
    #               history so the AI can use the conversation
    #               context.
    # Input       : User's question
    # Output      : Updated messages list
    # ========================================================

    messages.append(
        {
            "role": "user",
            "content": Question
        }
    )


    # ========================================================
    # Step 7 : Generate AI Response
    # Function Name : chat()
    # Description   : Send the conversation history to the
    #                 Ollama model and generate an answer.
    # Input         : Model name and messages list
    # Output        : AI response returned by Ollama
    # ========================================================

    response = chat(
        model="llama3.2:1b",
        messages=messages
    )


    # ========================================================
    # Step 8 : Extract AI Answer
    # Description : Extract the generated text from the
    #               Ollama response object.
    # Input       : response.message.content
    # Output      : Answer stored in the answer variable
    # ========================================================

    answer = response.message.content


    # ========================================================
    # Step 9 : Display AI Response
    # Description : Print the AI-generated answer on the
    #               terminal.
    # Input       : answer variable
    # Output      : AI answer displayed to the user
    # ========================================================

    print("\nYash Python Tutor:", answer)


    # ========================================================
    # Step 10 : Store AI Response
    # Description  : Append the AI response to the message
    #                history to maintain conversation context.
    # Input        : AI-generated answer
    # Output       : Updated messages list containing both
    #                user questions and AI responses
    # ========================================================

    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
