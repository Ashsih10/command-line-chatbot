from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPEN_API_KEY")
)

conversation = [
    {
        "role" : "system",
        "content" : "you are helpful ai assistant."
    }
]

while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        break

    conversation.append({
        "role" : "user",
        "content" : user_input 
    })

    response = client.responses.create(
        model = os.getenv("OPENAI_MODEL"),
        input = conversation
    )

    answer = response.output_text

    print("AI :", answer)

    conversation.append({
        "role" : "assistant"
        "content" " answer"
    })