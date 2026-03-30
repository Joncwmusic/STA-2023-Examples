import random
import pandas as pd
import streamlit as st
import math
import plotly.express as px
import plotly.io as pio
import kaleido

def normpdf(mu, sigma, x):
    part_1 = 1/(sigma*math.sqrt(2*math.pi))
    part_2 = math.exp(-((x-mu)**2)/(2*sigma**2))
    return part_1 * part_2

def gamma_integrand(t, alpha):
    return (t**(alpha-1))*math.exp(-t)

def area_interval(start_a, end_b, alpha, func):
    area_sum = func(end_b, alpha) + 4*(func((end_b+start_a)/2, alpha)) + func(start_a, alpha)
    avg_area = area_sum*(end_b-start_a)/6
    return avg_area

def gamma_function(alpha, step, nsteps = 1000):
    current_sum = 0
    current_start = 0
    next_point = current_start+step
    for i in range(nsteps):
        temp_sum = area_interval(current_start, next_point, alpha, gamma_integrand)
        current_sum += temp_sum
        current_start = next_point
        next_point += step
    return current_sum


def gamma_dist(x, alpha, beta, step):
    numerator = x**(alpha-1)*math.exp(-beta*x)*beta**alpha
    denominator = gamma_function(alpha, step)
    return numerator/denominator


def exp_distribution(rate_param, x):
    return rate_param*math.exp(-rate_param*x)


def build_calculator_notes():
    st.header("How to get a Confidence Interval: `ZInterval`")
    st.markdown("- You know the population standard deviation")
    st.markdown("- The sample size is greater than 30 (can be less than 30 if the underlying distribution is normal)")
    st.subheader("Step 1")
    col1step1_z, col2step1_z = st.columns(2)
    with col1step1_z:
        st.markdown("content")
    with col2step1_z:
        st.image("screenshots/09 Test Screen.png")
        st.image("screenshots/09 Highlight ZInterval.png")

    st.subheader("Step 2")
    col1step2_z, col2step2_z = st.columns(2)
    with col1step2_z:
        st.markdown("content")
    with col2step2_z:
        st.image("screenshots/09 Default ZInterval Screen.png")
        st.image("screenshots/09 Default ZInterval Screen - Data.png")

    st.subheader("Step 3")
    col1step3_z, col2step3_z = st.columns(2)
    with col1step3_z:
        st.markdown("content")
    with col2step3_z:
        st.image("screenshots/09 TInterval result screen.png")

    # T TEST
    st.header("How to get a Confidence Interval: `TInterval`")
    st.markdown("- You don't know the population standard deviation and instead have the sample standard deviation.")
    st.markdown("- The sample size is less than 30.")
    st.subheader("Step 1")
    col1step1_t, col2step1_t = st.columns(2)
    with col1step1_t:
        st.markdown("content")
    with col2step1_t:
        st.image("screenshots/09 Highlight TInterval.png")

    st.subheader("Step 2")
    col1step2_t, col2step2_t = st.columns(2)
    with col1step2_t:
        st.markdown("content")
    with col2step2_t:
        st.image("screenshots/09 Default TInterval Screen Stats.png")
        st.image("screenshots/09 Default TInterval Screen - Data.png")

    st.subheader("Step 3")
    col1step3_t, col2step3_t = st.columns(2)
    with col1step3_t:
        st.markdown("content")
    with col2step3_t:
        st.image("screenshots/09 ZInterval Result.png")

    # 1 PROP Z TEST
    st.header("How to get a Confidence Interval for a Proportion `1-PropZTest`")
    st.subheader("Step 1")
    col1step1_p, col2step1_p = st.columns(2)
    with col1step1_p:
        st.markdown("content")
    with col2step1_p:
        st.image("screenshots/09 Highlight 1-PropZInt.png")

    st.subheader("Step 2")
    col1step2_p, col2step2_p = st.columns(2)
    with col1step2_p:
        st.markdown("content")
    with col2step2_p:
        st.image("screenshots/09 Default 1-PropZInt Screen.png")
        st.image("screenshots/09 Popped 1-PropZInt.png")

    st.subheader("Step 3")
    col1step3_p, col2step3_p = st.columns(2)
    with col1step3_p:
        st.markdown("content")
    with col2step3_p:
        st.image("screenshots/09 1-PropZInt Result.png")