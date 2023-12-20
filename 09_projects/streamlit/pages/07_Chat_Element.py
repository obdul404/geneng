import inspect
import streamlit as st
from chat_input import ChatInput
from chat_message import ChatMessage

page_names_to_funcs = {

    "Chat Input": ChatInput,
    "Chat Message": ChatMessage
}

demo_name = st.sidebar.selectbox("Chat Element", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
