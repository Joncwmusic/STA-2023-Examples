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
import build_calc_notes as bcn


st.title("Chapter 3 Summary")


tab1, tab2, tab3, tab4 = st.tabs(["Measures of Central Tendency", "Measures of Spread", "Outliers and Position", "Calculator Tutorial"])


#### Build Streamlit page
st.set_page_config(
    page_title="Chapter 3 Notes"
)


with tab1:
    bct.build_central_tendency_tab()
with tab2:
    bst.build_spread_tab()
with tab3:
    bpo.build_position_outliers()
with tab4:
    bcn.build_calculator_notes()