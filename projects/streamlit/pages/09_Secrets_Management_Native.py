import streamlit as st
from utility import twoTabLayout
# Everything is accessible via the st.secrets dict:

def code():
    st.write("DB username:", st.secrets["db_username"])
    st.write("DB password:", st.secrets["db_password"])

    # And the root-level secrets are also accessible as environment variables:

    import os

    st.write(
        "Has environment variables been set:",
        os.environ["db_username"] == st.secrets["db_username"],
    )
twoTabLayout(code)