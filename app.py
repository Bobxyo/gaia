import streamlit as st
import requests
import os

KEY = os.environ.get("KEY", None)

st.set_page_config(page_title="Chat with OpenAI GPT3", page_icon=":robot:", layout="wide")

def chat_with_openai(prompt):
    model_engine = "text-davinci-003"
    prompt = (f"User: {prompt}" + "\n")
    headers = {
      'Content-Type': 'application/json',
      'Authorization': f'Bearer {KEY}'
    }

    response = requests.post(
      f"https://api.openai.com/v1/engines/{model_engine}/jobs",
      headers=headers,
      json={
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.5,
      }
    ).json()

    message = response['choices'][0]['text']
    return message

def main():
    st.title("Chat with OpenAI's GPT-3")
    history = []
    while True:
        user_input = st.text_input("You:")
        if user_input == "exit":
            break
        if user_input:
            response = chat_with_openai(user_input)
            history.append(f"User: {user_input}")
            history.append(f"GPT-3: {response}")
            st.write("GPT-3:", response)
    st.write("History of this session:", history)

if __name__ == "__main__":
    main()
