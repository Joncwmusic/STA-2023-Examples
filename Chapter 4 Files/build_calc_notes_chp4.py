import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random


def build_calculator_notes():
    st.header("How to Regression on you TI 83 and TI 84")

    st.subheader("Calculate $r$, $R^2$, $b_0$, and $b_1$")
    st.markdown("Basically everything you need to know about regression.")

    st.subheader("Step 0")
    step0col1, step0col2 = st.columns(2)
    with step0col1:
        st.markdown("Hit **2nd** and then the **0** button to enter the catalog menu and scroll down until you see "
                    "an option called DiagnosticsOn. If you don't do this step you won't actually see all the "
                    "regression metrics that matter.")
    with step0col2:
        st.image("screenshots/04 Catalog Screen.png")
        st.image("screenshots/04 DiagnosticsOn Screen.png")

    st.subheader("Step 1")
    step1col1, step1col2 = st.columns(2)
    with step1col1:
        st.markdown("Find the **STAT** button on your calculator which will take you to this screen.")
    with step1col2:
        st.image("screenshots/Stat - Edit - Screen.png")

    st.subheader("Step 2")
    step2col1, step2col2 = st.columns(2)
    with step2col1:
        st.markdown("From there select 'Edit...' which will allow you to input lists of data. We want input our data "
                    "into L1 and L2 which should have our x values and our y values, respectively.")
    with step2col2:
        st.image("screenshots/04 Regression L1 and L2 Populated.png")

    st.subheader("Step 3")
    step3col1, step3col2 = st.columns(2)
    with step3col1:
        st.markdown("Go back to **STAT** and highlight CALC and find LinReg in the calc menu. This is where you'll "
                    "input your lists. Once you hit enter it will give you values for "
                    "$a$, (which is the slope, $b_1$), $b$ (which is the y intercept, $b_0$),"
                    " the correlation coefficient $r$ and the coefficient of determination $R^2$")
    with step3col2:
        st.image("screenshots/Stat - Calc - Screen.png")
        st.image("screenshots/04 Linreg Screen.png")

    st.subheader("Step 4")
    step4col1, step4col2 = st.columns(2)
    with step4col1:
        st.markdown("Your regression metrics should populate on screen after hitting enter on the LinReg input "
                    "screen from the prior step.")
    with step4col2:
        st.image("screenshots/04 LinReg Results Screen.png")



