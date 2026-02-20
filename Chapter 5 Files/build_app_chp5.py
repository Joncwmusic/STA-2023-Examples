import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly"
random.seed(300)
import build_probability_rules_addition as bpra
import build_probability_rules_multiplication as bprm
import build_combinations_and_permutations as bcap
import build_conditional_probability as bcp


#### Build Streamlit page
st.set_page_config(
    page_title="Chapter 5 Notes"
)

st.title("Chapter 5 Summary")

tab1, tab2, tab3, tab4 = st.tabs(["Probability Rules", "Multiplication and Independence","Permutations and Combinations", "Conditional Probability"])


with tab1:
    st.write("Your page is in another castle")
with tab2:
    st.write("Your page is in another castle")
with tab3:
    st.write("Your page is in another castle")
with tab4:
    st.write("Your page is in another castle")
# with tab5:
#     # bmr.build_multilinear_regression()