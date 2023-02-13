import os
import streamlit as st
import openai

# Hide API Key
API_KEY = os.getenv("KEY")
openai.api_key = API_KEY

# Set up chat history
history = []

def chat(model, prompt):
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    history.append(f"Me: {prompt}")
    history.append(f"ChatGPT: {message}")
    return message

# Create the Streamlit app
st.set_page_config(page_title="ChatGPT", page_icon=":robot:", layout="wide")
st.title("ChatGPT")

model = "text-davinci-003"
prompt = st.text_input("Enter your message:")

if st.button("Submit"):
    response = chat(model, prompt)
    st.write("ChatGPT: ", response)

# Show chat history
if len(history) > 0:
    st.header("Chat History:")
    for h in history:
        st.write(h)
