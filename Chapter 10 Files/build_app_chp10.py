import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly"
random.seed(300)
import build_hypothesis_language as bhl
import build_hypothesis_prop as bhp
import build_hypothesis_mean as bhm
import build_calc_notes_chp10 as bcn10

#### Build Streamlit page
st.set_page_config(
    page_title="Chapter 10 Notes"
)

st.title("Chapter 10 Summary")

tab1, tab2, tab3, tab4 = st.tabs(["Language of Hypothesis Testing"
                                , "Hypothesis Testing for Proportions"
                                , "Hypothesis Testing for Means"
                                , "Calculator"])
with tab1:
    bhl.build_hypothesis_language()
with tab2:
    try:
        bhp.build_hypothesis_prop()
    except:
        st.markdown("Your page is in another castle")
with tab3:
    try:
        bhm.build_hypothesis_mean()
    except:
        st.markdown("Your page is in another castle")
with tab4:
    try:
        bcn10.build_calculator_notes()
    except:
        st.markdown("Your page is in another castle")