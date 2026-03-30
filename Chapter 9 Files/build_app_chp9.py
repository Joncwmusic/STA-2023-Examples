import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly"
random.seed(300)
import build_confidence_interval_mean as bcim
import build_t_distribution as btd
import build_confidence_interval_prop as bcip
import build_calc_notes_chp9 as bcn9

#### Build Streamlit page
st.set_page_config(
    page_title="Chapter 9 Notes"
)

st.title("Chapter 9 Summary")

tab1, tab2, tab3, tab4 = st.tabs(["T Distribution"
                                , "Confidence Intervals: Mean"
                                , "Confidence Intervals: Props"
                                , "Calculator"])
with tab1:
    btd.build_t_distribution()
with tab2:
    bcim.build_confidence_interval_mean()
with tab3:
    try:
        bcip.build_confidence_inteval_prop()
    except:
        st.markdown("Your page is in another castle")
with tab4:
    bcn9.build_calculator_notes()
