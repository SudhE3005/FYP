import streamlit as st
import streamlit.components.v1 as components

st.title("Mental Heath Chatbot")


messages = st.container(height=300)
if prompt := st.chat_input("Say something"):
    messages.chat_message("user").write(prompt)
    messages.chat_message("ai").write(f"Echo: {prompt}")