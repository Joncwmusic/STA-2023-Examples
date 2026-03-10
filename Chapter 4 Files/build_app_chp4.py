import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly"
random.seed(300)
import build_correlation as bc
import build_linear_regression as blr
import build_contingency_tables as bct
import build_residual_analysis as bra
import build_calc_notes_chp4 as bcn4



#### Build Streamlit page
st.set_page_config(
    page_title="Chapter 4 Notes"
)

st.title("Chapter 4 Summary")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Correlation", "Regression","Regression Evaluation", "Contingency Diagrams", "Calculator"])


with tab1:
    bc.build_correlation()
with tab2:
    blr.build_linear_regression()
with tab3:
    bra.build_residual_analysis()
with tab4:
    bct.build_contingency_tables()
with tab5:
    bcn4.build_calculator_notes()
