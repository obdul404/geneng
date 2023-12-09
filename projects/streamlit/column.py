import streamlit as st
from utility import twoTabLayout
def Column():
   col1, col2, col3 = st.columns(3)

   with col1:
      st.header("A cat")
      st.image("https://static.streamlit.io/examples/owl.jpg")

   with col2:
      st.header("A dog")
      st.image("https://static.streamlit.io/examples/owl.jpg")
      
   with col3:
      st.header("An owl")
      st.image("https://static.streamlit.io/examples/owl.jpg")