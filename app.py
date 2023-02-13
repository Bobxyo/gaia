import os
import streamlit as st
import requests

KEY = os.getenv("OPENAI_KEY")

def get_response(prompt):
    response = requests.post("https://api.openai.com/v1/engines/text-davinci-002/completions",
                             headers={"Content-Type": "application/json", "Authorization": f"Bearer {KEY}"},
                             json={"prompt": prompt, "max_tokens": 1024, "n": 1, "stop": None, "temperature": 0.5}).json()

    return response["choices"][0]["text"]

st.title("Chat with OpenAI")

conversation = []

input_text = st.text_input("Ask me anything!")

if input_text:
    response = get_response(input_text)
    conversation.append(f"You: {input_text}")
    conversation.append(f"OpenAI: {response}")

st.text("\n".join(conversation))
