import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly"
random.seed(300)
import build_sample_mean_dist as bsmd
import build_sample_prop_dist as bspd
import build_calc_notes_chp8 as bcn8

#### Build Streamlit page
st.set_page_config(
    page_title="Chapter 8 Notes"
)

st.title("Chapter 8 Summary")

tab1, tab2, tab3= st.tabs(["Distribution of the Sample Mean", "Distribution of Sample Props", "Calculator"])

with tab1:
        bsmd.build_sample_mean_page()
with tab2:
        bspd.build_sample_prop_page()
with tab3:
    try:
        bcn8.build_calculator_notes()
    except:
        st.markdown("Sorry, your page is in another castle.")
