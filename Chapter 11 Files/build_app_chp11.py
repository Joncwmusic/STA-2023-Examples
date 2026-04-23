import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly"
random.seed(300)
import build_one_to_two as bott
import build_2_prop_htest as b2pht
import build_2_samp_mean_htest_dep as b2smh_dep
import build_2_samp_mean_htest_indep as b2smh_indep
import build_calc_notes_chp_11 as bcn11

#### Build Streamlit page
st.set_page_config(
    page_title="Chapter 11 Notes"
)

st.title("Chapter 11 Summary")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["1 Sample to 2 Samples"
                                , "2 Proportions"
                                , "2 Means (Dependent)"
                                , "2 Means (Independent)"
                                , "Calculator"])
with tab1:
    try:
        bott.build_one_to_two()
    except:
        st.markdown("Your page is in another castle")
with tab2:
    try:
        b2pht.build_2_prop_htest()
    except:
        st.markdown("Your page is in another castle")
with tab3:
    try:
        b2smh_dep.build_2_samp_mean_htest_dep()
    except:
        st.markdown("Your page is in another castle")
with tab4:
    try:
        b2smh_indep.build_2_samp_mean_htest_indep()
    except:
        st.markdown("Your page is in another castle")
with tab5:
    try:
        bcn11.build_calculator_notes()
    except:
        st.markdown("Your page is in another castle")