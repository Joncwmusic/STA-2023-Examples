import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random


def build_calculator_notes():
    st.header("How to Probability Distribution on your TI 83 and TI 84")

    st.subheader("Caluclate mean and standard deviation")
    st.markdown("The steps for calculating mean and standard deviation are the same as calculating mean and standard "
                "deviation for weighted data which can be found in the chapter 3 notes.")

    st.subheader("Calculate Binomial Probabilities (binompdf and binomcdf)")
    st.markdown("Basically everything you need to know about calculating permutations and combinations.")


    st.subheader("Step 1")
    step1col1, step1col2 = st.columns(2)
    with step1col1:
        st.markdown("From your home page hit 2nd and then the VARS button to get to the 'distr' menu. You'll see "
                    "options like normcdf, invNorm, etc. but what we care about for this chapter is 'binompdf' and "
                    "'binomcdf' The difference between the two is that binompdf is the probability of getting exactly "
                    "the number of successes we care about and binomcdf is the CUMULATIVE distribution which gives us "
                    "the probability of getting less than or equal to the value we care about.")
    with step1col2:
        st.image("screenshots/06 distr menu.png")
        st.image("screenshots/06 binompdf and binomcdf.png")

    st.subheader("Step 2")
    step2col1, step2col2 = st.columns(2)
    with step2col1:
        st.markdown("No matter which one you select (pdf vs. cdf) the inputs are the same exactly the same. n is your "
                    "number of trials. p is your probability of success. and x value is the number of successes you "
                    "want based on the problem you are solving. In this case I have 12 trials, a success probability of"
                    " 0.57, and the number of successes I care about is 4.")
        st.markdown("WARNING: If you're using an older TI83 it won't give you this menu and you'll have to paste the "
                    "parameters manually. which is shown in the next step.")
    with step2col2:
        st.image("screenshots/06 binom menu blank.png")
        st.image("screenshots/06 binom menu popped.png")

    st.subheader("Step 3")
    step3col1, step3col2 = st.columns(2)
    with step3col1:
        st.markdown("Again, if you have a TI83 it'll take you directly to this screen without the inputs. You have to "
                    "put them in the order of n, p, then x. Otherwise, if you have the TI84+ CE with the fancy display "
                    "you'll the screen populated with your paramters and can just press ENTER.")
    with step3col2:
        st.image("screenshots/06 binom pasted into home calc screen.png")
        st.image("screenshots/06 binompdf result.png")

    st.subheader("REMINDER")
    step4col1, step4col2 = st.columns(2)
    with step4col1:
        st.markdown("Remember binomcdf and binompdf will return different values, you need to know the difference.")
    with step4col2:
        st.image("screenshots/06 binompdf vs binomcdf.png")


