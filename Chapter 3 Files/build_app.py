import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly"
random.seed(300)
import build_central_tendency as bct
import build_spread as bst
import build_position_outliers as bpo

tab1, tab2, tab3 = st.tabs(["Measures of Central Tendency", "Measures of Spread", "Outliers and Position"])


#### Build Streamlit page
st.set_page_config(
    page_title="Chapter 3 Notes"
)


with tab1:
    st.title("Chapter 3 Summary")
    bct.build_central_tendency_tab()
with tab2:
    st.title("Chapter 3 Summary")
    bst.build_spread_tab()
with tab3:
    st.title("Chapter 3 Summary")
    bpo.build_position_outliers()