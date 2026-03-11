import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly"
random.seed(300)
import build_discrete_distributions as dd
import build_binomial_distribution as bb

#### Build Streamlit page
st.set_page_config(
    page_title="Chapter 6 Notes"
)

st.title("Chapter 6 Summary")

tab1, tab2, tab3= st.tabs(["Discrete Distributions", "Binomial Distribution", "Calculator"])

with tab1:
    dd.build_discrete_probaility_distributions()
with tab2:
    bb.build_binomial_distribution()
with tab3:
    st.write("Your page is in another castle.")
