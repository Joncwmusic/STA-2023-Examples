import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly"
random.seed(300)
import build_normal_distribution as bnd
import build_continuous_random_vars as bcrv

#### Build Streamlit page
st.set_page_config(
    page_title="Chapter 6 Notes"
)

st.title("Chapter 6 Summary")

tab1, tab2, tab3= st.tabs(["Discrete Distributions", "Binomial Distribution", "Calculator"])

with tab1:
    bcrv.build_continuous_probability_densities()
with tab2:
    bb.build_binomial_distribution()
with tab3:
    st.write("Your page is in another castle.")
