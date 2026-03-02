import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random


def build_calculator_notes():
    st.header("How to Compute Summary Statistics on your TI 83 and TI 84")

    st.subheader("Calculate Mean, Median, and Standard Deviation")
    st.markdown("These all fall out of a few button presses on your calculator")

    st.subheader("Step 1")
    step1col1, step1col2 = st.columns(2)
    with step1col1:
        st.markdown("Find the **STAT** button on your calculator which will take you to this screen.")
    with step1col2:
        st.image("screenshots/Stat - Edit - Screen.png")

    st.subheader("Step 2")
    step2col1, step2col2 = st.columns(2)
    with step2col1:
        st.markdown("From there select 'Edit...' which will allow you to input lists of data")
    with step2col2:
        st.image("screenshots/Edit List Screen Empty.png")

    st.subheader("Step 3")
    step3col1, step3col2 = st.columns(2)
    with step3col1:
        st.markdown("Populate the list L1 with you data. If data already exists you can clear the list with the "
                    "**clear** button while highlighting the list name.")
    with step3col2:
        st.image("screenshots/Edit List Screen only L1.png")

    st.subheader("Step 4")
    step4col1, step4col2 = st.columns(2)
    with step4col1:
        st.markdown("Hit **2nd** **mode** (or quit) to exit the interface. Nothing has happened yet. Now, go to stat "
                    "again and select the CALC in the menu")
    with step4col2:
        st.image("screenshots/Stat - Calc - Screen.png")

    st.subheader("Step 5")
    step5col1, step5col2 = st.columns(2)
    with step5col1:
        st.markdown("Select **1 Var Stats** and make sure The List option has L1 and the FreqList is empty (That's"
                    "important for grouped data)")
    with step5col2:
        st.image("screenshots/1 Var Stats Screen.png")

    st.subheader("Step 6")
    step6col1, step6col2 = st.columns(2)
    with step6col1:
        st.markdown(r"Hit Calculate and observe that all the summary statistics for the list are now displayed. "
                    r"It shows the mean: $\bar{x}$, the sample standard deviation: $Sx$, and the population standard "
                    r"deviation: $\sigma x$. If you scroll down in the display it also shows the median, labelled "
                    r"'Med'.")
        st.markdown("Pay attention to the fact that it also displays MinX, MaxX, Q1 and Q3. The difference between "
                    "MaxX and MinX is the range and the difference between Q3 and Q1 is the Interquartile Range (IQR)")
    with step6col2:
        st.image("screenshots/Complete 1VarStats Screen Pt1.png")
        st.image("screenshots/Complete 1VarStats Screen Pt2.png")

    st.subheader("Calculating Weighted Mean and Standard Deviation")
    st.markdown("For weighted and grouped data the weights/frequencies are important for getting accurate summary "
                "statistics. The way to calculate these on your calculator is largely the same with some important "
                "differences.")

    st.subheader("Change 1")
    change1col1, change2col2 = st.columns(2)
    with change1col1:
        st.markdown("Instead of just inputting L1 you'll need to input L2 as well. This L2 will act as our weights.")
    with change2col2:
        st.image("screenshots/Edit List Screen L1 and L2.png")

    st.subheader("Change 2")
    change1col1, change2col2 = st.columns(2)
    with change1col1:
        st.markdown("When you navigate to the 1Var Stats Screen, you should see an option for FreqList where you will "
                    "input L2.")
    with change2col2:
        st.image("screenshots/1 Var Stats Screen with FreqList L2.png")
