import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Multipage App!")

st.sidebar.success("Select a demo above.")
st.write("Here's a valid directory structure for a multipage app:")
st.code("""
Home.py # This is the file you run with "streamlit run"
└─── pages/
  └─── About.py # This is a page
  └─── 2_Page_two.py # This is another page
  └─── 3_😎_three.py # So is this
""")