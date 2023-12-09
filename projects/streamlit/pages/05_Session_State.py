import streamlit as st
from utility import twoTabLayout

def fun1():
    import streamlit as st

    st.title('Counter Example')
    count = 0

    increment = st.button('Increment',1)
    if increment:
        count += 1

    st.write('Count = ', count)
def fun2():
    import streamlit as st

    st.title('Counter Example')
    if 'count' not in st.session_state:
        st.session_state.count = 0

    increment = st.button('Increment',2)
    if increment:
        st.session_state.count += 1

    st.write('Count = ', st.session_state.count)

def fun3():
    import streamlit as st

    st.title('Counter Example using Callbacks')
    if 'count' not in st.session_state:
        st.session_state.count = 0

    def increment_counter():
        st.session_state.count += 1

    st.button('Increment', on_click=increment_counter,key=3)

    st.write('Count = ', st.session_state.count)

def fun4():
    import streamlit as st

    st.title('Counter Example using Callbacks with args')
    if 'count' not in st.session_state:
        st.session_state.count = 0

    increment_value = st.number_input('Enter a value', value=0, step=1)

    def increment_counter(increment_value):
        st.session_state.count += increment_value

    increment = st.button('Increment', on_click=increment_counter, key=4,
        args=(increment_value, ))

    st.write('Count = ', st.session_state.count)

tab1, tab2, tab3, tab4 = st.tabs(["Counter without session", "Counter","Counter Callbacks", "Counter Callbacks Args"])

with tab1:
    twoTabLayout(fun1)
with tab2:
    twoTabLayout(fun2)
with tab3:
    twoTabLayout(fun3)
with tab4:
    twoTabLayout(fun4)
