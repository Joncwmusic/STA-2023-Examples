import hypothesis_test_utils as htu
import streamlit as st
import pandas as pd

def build_2_samp_mean_htest_dep():
    st.header("The Situation")

    st.header("Step by Step")
    st.subheader("Set up the Hypothesis Test")
    col1tail, col2tail, col3tail = st.columns(3)

    with col1tail:
        st.markdown("**Left Tail**")
        st.markdown(r"H_0: \mu_d = 0")
        st.markdown(r"H_0: \mu_d < 0")
    with col2tail:
        st.markdown("**Right Tail**")
        st.markdown(r"H_0: \mu_d = 0")
        st.markdown(r"H_0: \mu_d > 0")
    with col3tail:
        st.markdown("**Two Tail**")
        st.markdown(r"H_0: \mu_d = 0")
        st.markdown(r"H_0: \mu_d /ne 0")

    st.subheader("Determine your alpha")
    st.markdown("Your alpha is usually given by the problem but if it isn't 0.05 is a good rule of thumb unless you "
                "need more or less scrutiny.")

    st.subheader("Compute your Test Statistic")

    st.subheader("Compute the p value")

    st.subheader("Make a Conclusion")