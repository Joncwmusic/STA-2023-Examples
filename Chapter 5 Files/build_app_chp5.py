import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly"
random.seed(300)
import build_probability_rules_addition as bpra
import build_probability_rules_multiplication as bprm
import build_combinations_and_permutations as bcp
import build_calc_notes_chp5 as bcn5


#### Build Streamlit page
st.set_page_config(
    page_title="Chapter 5 Notes"
)

st.title("Chapter 5 Summary")

tab1, tab2, tab3, tab4 = st.tabs(["Probability Rules", "Multiplication and Conditional Probability"
                                           ,"Permutations and Combinations", "Calculator Tutorial"])

with tab1:
    bpra.build_probability_rules_addition()
with tab2:
    bprm.build_probability_rules_multiplication()
with tab3:
    bcp.build_combination_permutation()
with tab4:
    bcn5.build_calculator_notes()