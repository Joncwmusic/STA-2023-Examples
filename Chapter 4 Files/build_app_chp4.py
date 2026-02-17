import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly"
random.seed(300)
import build_correlation as bc
# import build_linear_regression as blr
# import build_contigency_tables as bct
# import build_nonlinear_regression as bnr
# import build_multilinear_regression as bmr



#### Build Streamlit page
st.set_page_config(
    page_title="Chapter 4 Notes"
)

st.title("Chapter 4 Summary")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Correlation", "Regression", "Contingency Diagrams", "NonLinear Regression", "More than 2 Variables"])


with tab1:
    bc.build_correlation()
# with tab2:
#     # blr.build_linear_regression()
# with tab3:
#     # bct.build_contigency_tables()
# with tab4:
#     # bnr.build_nonlinear_regression()
# with tab5:
#     # bmr.build_multilinear_regression()