import inspect
import streamlit as st
from column import Column
from container import Container
from empty import Empty
from expander import Expander
from sidebar import Sidebar
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Column", "Container", "Empty","Expander","Sidebar"])

with tab1:
   Column()
   st.code(inspect.getsource(Column))

with tab2:
   Container()
   st.code(inspect.getsource(Container))

with tab3:
   Empty()
   st.code(inspect.getsource(Empty))

with tab4:
   Expander()
   st.code(inspect.getsource(Expander))

with tab5:
   Sidebar()
   st.code(inspect.getsource(Sidebar))