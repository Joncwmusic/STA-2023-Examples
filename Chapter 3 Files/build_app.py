import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly"
random.seed(300)
import build_central_tendency as bct
import build_spread as bst

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Measures of Central Tendency", "Measures of Spread", "Grouped Data", "Outliers", "Five Number Summary"])


#### Build Streamlit page
st.set_page_config(
    page_title="Chapter 3 Notes"
)

with tab1:
    bct.build_central_tendency_tab()
with tab2:
    bst.build_spread_tab()
with tab3:
    st.title("Section 3")
with tab4:
    st.title("Section 4")
with tab5:
    st.title("Section 5")