import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random


def build_calculator_notes():
    st.header("How to Regression on you TI 83 and TI 84")

    st.subheader("Calculate nPr, nCr, and Factorial!")
    st.markdown("Basically everything you need to know about calculating permutations and combinations.")


    st.subheader("Step 1")
    step1col1, step1col2 = st.columns(2)
    with step1col1:
        st.markdown("Enter the first number (only number if just computing factorial) and find the math button and "
                    "you'll see a screen that looks like this. You want to go to the PROB tab. On some calculators, "
                    "it'll just be PRB.")
    with step1col2:
        st.image("screenshots/05 Math screen.png")

    st.subheader("Step 2")
    step2col1, step2col2 = st.columns(2)
    with step2col1:
        st.markdown("On the PROB/PRB screen you'll see nPr, nCr, and ! all as options which you can scroll down and "
                    "select depending on which option you're looking to use for your problem.")
    with step2col2:
        st.image("screenshots/05 prob menu.png")

    st.subheader("Step 3")
    step3col1, step3col2 = st.columns(2)
    with step3col1:
        st.markdown("Plug in your second number if your using the permutations or combinations. For factorial you just "
                    "a single number input. Then hit enter. Each of those results should look something like the "
                    "screens to the right.")
    with step3col2:
        st.subheader("nCr")
        st.image("screenshots/05 Factorial calc result.png")


