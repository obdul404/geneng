import inspect
import streamlit as st

def twoTabLayout(code):
    tab1, tab2 = st.tabs(["Code", "Output"])
    with tab1:
        # Get the full source code of the function
        full_source = inspect.getsource(code)

        # Split the source into lines and remove the first line (function signature)
        function_body_lines = full_source.splitlines()[1:]

        # Join the lines back into a single string  
        function_body = '\n'.join(function_body_lines)

        # Optionally, you can strip leading whitespace to align the code to the left
        function_body = '\n'.join(line.strip() for line in function_body_lines)
        
        st.code(full_source,language="python")

    with tab2:
        code()

def twoColumnLayout(code):
    col1, col2 = st.columns([2,1])
    with col1:
        st.code(inspect.getsource(code),language="python")
    with col2:
        code()