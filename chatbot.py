
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env")

# Initialize Groq client
client = Groq(api_key=api_key)

# Conversation history
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]

print("\nGroq AI Chatbot")
print("Type 'exit' to quit.")
print("-" * 30)

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break

    if not user_input:
        continue

    messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages,
            temperature=0.7,
            max_tokens=1024
        )

        bot_reply = response.choices[0].message.content

        print(f"\nBot: {bot_reply}")

        messages.append({
            "role": "assistant",
            "content": bot_reply
        })

    except Exception as e:
        print(f"\nError: {e}")
        messages.pop()
