import openai
import streamlit as st

KEY = "" # Add your OpenAI API key here

# Authenticate to OpenAI API
openai.api_key = KEY

# Create a function to generate answers using the ChatGPT model
def generate_answer(model, prompt):
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

# Define the main Streamlit app
def main():
    st.title("ChatGPT")
    model = "text-davinci-003"
    history = []
    prompt = st.text_input("Ask a Question:")

    if prompt:
        history.append(("User", prompt))
        answer = generate_answer(model, prompt)
        history.append(("ChatGPT", answer))
        st.write("Answer: ", answer)
        st.write("History:", history)

if __name__ == "__main__":
    main()
