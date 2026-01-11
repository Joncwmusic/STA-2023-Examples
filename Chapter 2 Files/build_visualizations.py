import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly"
import build_qualitative_tab as bqual
import build_quantitative_tab as bquant


tab1, tab2, tab3 = st.tabs(["Visualizing Qualitative Data", "Visualizing Quantitative Data", "Misleading Visualizations"])

#### Build Streamlit page

with tab1:
    bqual.build_qualitative_tab()
with tab2:
    bquant.build_quantitative_tab()