from utility import twoTabLayout
import streamlit as st
def Empty():
    import time

    with st.empty():
        for seconds in range(10):
            st.write(f"⏳ {seconds} seconds have passed")
            time.sleep(1)
    st.write("✔️ 10 seconds over!")