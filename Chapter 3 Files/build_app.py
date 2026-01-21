import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly"
random.seed(300)
import build_central_tendency as bct

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Measures of Central Tendency", "Measures of Spread", "Grouped Data", "Outliers", "Five Number Summary"])


#### Build Streamlit page
st.set_page_config(
    page_title="Chapter 2 Notes"
)

with tab1:
    bct.build_central_tendency_tab()
with tab2:
    pass
with tab3:
    pass
with tab4:
    pass
with tab5:
    pass