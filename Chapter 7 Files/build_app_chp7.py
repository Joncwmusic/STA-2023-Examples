import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly"
random.seed(300)
import build_normal_distribution as bnd
import build_continuous_random_vars as bcrv
import build_calc_notes_chp7 as bcn7

#### Build Streamlit page
st.set_page_config(
    page_title="Chapter 7 Notes"
)

st.title("Chapter 7 Summary")

tab1, tab2, tab3= st.tabs(["Continuous Distributions", "Normal Distribution", "Calculator"])

with tab1:
    bcrv.build_continuous_probability_densities()
with tab2:
    bnd.build_normal_distribution()
with tab3:
    bcn7.build_calculator_notes()
