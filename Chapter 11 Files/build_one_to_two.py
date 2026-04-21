import pandas as pd
import streamlit as st
import math
import random
import graphviz

def build_one_to_two():
    st.header("The Workflow:")
    st.subheader("Mean or Proportion")
    st.markdown("When thinking about which hypothesis test to use you need to determine first, what type of claim you "
                "are even challenging. the first is which parameter is under dispute? Is it a mean, proportion, a "
                "standard deviation? Luckily standard deviation is outside the scope of this course so you just have "
                r"to decide between mean $\mu$ and proportion $p$.")

    st.markdown("Remember that **means** are calculated from things you measure for each subject in your sample. Think "
                "height, GPA, hours of doom scrolling, or number of lectures attended.")

    st.markdown("Remember that **proportions** are calculated from yes or no responses. Think approval ratings of your "
                "least favorite politician, or whether or not your neighbor uses solar panels.")

    st.subheader("One parameter or two parameters")

    st.markdown("the next thing to determine after determining what kind of data you have is thinking about whether "
                "you are comparing 2 datasets or just using one against a specific claim.")

    col1_onevtwo, col2_onevtwo = st.columns(2)
    with col1_onevtwo:
        st.subheader("2 Sample Language")
        st.markdown("*Group A has height 172.1cm and Group B has height 169.7cm*")
        st.markdown("*A sample of programmers and a sample of physics majors both take a calculus test*")
        st.markdown("*Before and after taking a drug participants had their Cholesterol Measured*")
    with col2_onevtwo:
        st.subheader("1 Sample Language")
        st.markdown("*The average height based on a sample of 14 students is 171.4cm*")
        st.markdown("*A sample of physicists take a calculus exam and score 92% on average*")
        st.markdown("*A sample of participants are asked if they experienced headaches while taking the drug.*")

    st.subheader("Independent vs. Dependent")

    st.header("Proportions")
    col1prop, col2prop = st.columns(2)

    with col1prop:
        st.subheader("1 Sample")
        st.markdown(r"$H_0: p = p_0$")
        st.markdown(r"$H_1: p \ne p_0$")
    with col2prop:
        st.subheader("2 Sample")
        st.markdown(r"$H_0: p_1 = p_2$")
        st.markdown(r"$H_1: p_1 \ne p_2$")

    st.header("Means")
    col1mean, col2mean, col3mean = st.columns(3)

    with col1mean:
        st.subheader("1 Sample")
        st.markdown(r"$H_0: \mu = \mu_0$")
        st.markdown(r"$H_1: \mu \ne \mu_0$")
    with col2mean:
        st.subheader("2 Sample Dep.")
        st.markdown(r"$H_0: \mu_d = 0$")
        st.markdown(r"$H_1: \mu_d \ne 0$")
    with col3mean:
        st.subheader("3 Sample Indep.")
        st.markdown(r"$H_0: \mu_1 = \mu_2$")
        st.markdown(r"$H_1: \mu_1 \ne \mu_2$")
