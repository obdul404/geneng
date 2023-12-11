import time
from openai import OpenAI
from openai.types.beta.assistant import Assistant
from openai.types.beta.thread import Thread
from openai.types.beta.threads.thread_message import ThreadMessage
from openai.types.beta.threads.run import Run
from typing import List
from io import BytesIO

import streamlit as st

st.sidebar.title("Assistants API")

if "client" not in st.session_state:
    st.session_state.client = OpenAI()

assistansList = st.session_state.client.beta.assistants.list()
assistantName = st.sidebar.selectbox("Available Assistants",[m.name for m in assistansList.data])
assistant: Assistant = next((m for m in assistansList.data if m.name == assistantName),None)

st.session_state["openai_model"] = assistant.model
st.subheader(st.session_state["openai_model"].upper())


if "messages" not in st.session_state:
    st.session_state.messages = []

prompt = st.chat_input("Say something")

if prompt:
    
    #Step 2: Create a Thread
    thread: Thread  = st.session_state.client.beta.threads.create()

    #Step 3: Add a Message to a Thread
    message = st.session_state.client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt
    )

    #Step 4: Run the Assistant
    run: Run = st.session_state.client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Please address the user as Hannan. The user has a premium account."
    )

    #Step 5: Check the Run status
    with st.spinner('Generating Response...'):
        while run.status == "queued" or run.status == "in_progress":
            run = st.session_state.client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id,
            )
            time.sleep(0.5)

    #Step 6: Display the Assistant's Response

    messages: list[ThreadMessage] = st.session_state.client.beta.threads.messages.list(
    thread_id=thread.id
    )

    st.session_state.messages = [msg for msg in reversed(messages.data)]

    for message in st.session_state.messages:
        with st.chat_message(message.role):
            for mc in message.content:
                if mc.type == "text":
                    st.markdown(mc.text.value)
                if mc.type == "image_file":
                    fileid = (mc.image_file.file_id)
                    image_data = st.session_state.client.files.content(file_id=fileid)
                    image_data_bytes = image_data.read()
                    with open(f"""./{fileid}.png""", "wb") as file:
                        file.write(image_data_bytes)
                        st.image(f"""./{fileid}.png""")