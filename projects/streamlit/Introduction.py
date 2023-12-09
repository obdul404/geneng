# import the streamlit library
import streamlit as st
 
# give a title to our app
st.title('Welcome to Streamlit Tutorial')
st.subheader('Install streamlit package')
st.code('pip install streamlit')
st.subheader('Create app.py and run it')
st.code('streamlit run app.py')

st.header("Code")
st.code('''st.write('Hello World')''')
st.header("Result")
st.write('Hello World')

