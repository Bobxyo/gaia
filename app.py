import streamlit as st
import openai
import os

# 隐藏 API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# 设置标题
st.title("OpenAI 文章生成器")

# 获取用户输入
prompt = st.text_input("请输入提示")
min_length = st.number_input("最小文章字数", min_value=1, max_value=1000, value=100)

# 如果有输入，则调用 OpenAI API 生成文章
if prompt:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    article = response["choices"][0]["text"].strip()
    if len(article) >= min_length:
        st.write("文章：", article)
    else:
        st.write("很抱歉，文章长度过短。")
