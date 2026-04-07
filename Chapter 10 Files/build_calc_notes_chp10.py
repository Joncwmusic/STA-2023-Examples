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
        st.markdown(r"Press *STAT* then navigate to the **TESTS** you'll see a menu that starts with `Z-Test` (Don't "
                    r"worry about that option, that's chapter 10). Instead scroll down until you see `ZInterval`.")
        st.markdown("Once you highlight `ZInterval` press **ENTER** to fill in the necessary parameters.")
    with col2step1_z:
        st.image("screenshots/09 Test Screen.png")
        st.image("screenshots/09 Highlight ZInterval.png")

    st.subheader("Step 2")
    col1step2_z, col2step2_z = st.columns(2)
    with col1step2_z:
        st.markdown("There are two options to inputting your parameters:")
        st.markdown(r"""
        * You can enter $\bar{x}$ and $\sigma$ directly along with sample size and confidence level. If you're not given
        a confidence level in your problem, assume the confidence level is 95%.
        * You can input the data from a sample into L_1 and it will calculate $\bar{x}$ for you, when constructing the 
        confidence interval but you still have to provide your own $\sigma$ since it is based on population. Otherwise, 
        use the TInterval Option Outlined below.
        """)
    with col2step2_z:
        st.image("screenshots/09 Default ZInterval Screen.png")
        st.image("screenshots/09 Default ZInterval Screen - Data.png")

    st.subheader("Step 3")
    col1step3_z, col2step3_z = st.columns(2)
    with col1step3_z:
        st.markdown(r"Now it's just a matter of pressing **Calculate** and you will see a screen with your lower bound "
                    r"and upper bound in parentheses as well as your $\bar{x}$ and $n$")
    with col2step3_z:
        st.image("screenshots/09 ZInterval Result.png")

    # T TEST
    st.header("How to get a Confidence Interval: `TInterval`")
    st.markdown("- You don't know the population standard deviation and instead have the sample standard deviation.")
    st.markdown("- The sample size is less than 30.")
    st.subheader("Step 1")
    col1step1_t, col2step1_t = st.columns(2)
    with col1step1_t:
        st.markdown(r"Press *STAT* then navigate to the **TESTS** and scroll down until you see `TInterval`.")
        st.markdown("Once you highlight `TInterval` press **ENTER** to fill in the necessary parameters.")
    with col2step1_t:
        st.image("screenshots/09 Highlight TInterval.png")

    st.subheader("Step 2")
    col1step2_t, col2step2_t = st.columns(2)
    with col1step2_t:
        st.markdown("Once again there are two options to inputting your parameters:")
        st.markdown(r"""
                * You can enter $\bar{x}$ and $s$, the sample standard deviation, along with sample size and confidence 
                level. If you're not given a confidence level in your problem, assume the confidence level is 95%.
                * You can input the data from a sample into L_1 and it will calculate $\bar{x}$ for you, when constructing the 
                confidence interval but you still have to provide your own $\sigma$ since it is based on population. Otherwise, 
                use the TInterval Option Outlined below.
                """)
    with col2step2_t:
        st.image("screenshots/09 Default TInterval Screen Stats.png")
        st.image("screenshots/09 Default TInterval Screen - Data.png")

    st.subheader("Step 3")
    col1step3_t, col2step3_t = st.columns(2)
    with col1step3_t:
        st.markdown("When you press calculate you should see an interval just like with `ZInterval` which shows "
                    "the mean, sample standard deviation, and the sample size.")
    with col2step3_t:
        st.image("screenshots/09 TInterval result screen.png")

    # 1 PROP Z TEST
    st.header("How to get a Confidence Interval for a Proportion `1-PropZTest`")
    st.subheader("Step 1")
    col1step1_p, col2step1_p = st.columns(2)
    with col1step1_p:
        st.markdown(r"Press *STAT* then navigate to the **TESTS** and scroll down until you see `1-PropZTest`.")
        st.markdown("Once you highlight `1-PropZTest` press **ENTER** to fill in the necessary parameters.")
    with col2step1_p:
        st.image("screenshots/09 Highlight 1-PropZInt.png")

    st.subheader("Step 2")
    col1step2_p, col2step2_p = st.columns(2)
    with col1step2_p:
        st.markdown("In this case you NEED an $x$ and $n$. Remember $n$ is the sample size and $x$"
                    "is the number of 'successes' so to speak for your proportion. Then fill out the Confidence Level.")
    with col2step2_p:
        st.image("screenshots/09 Default 1-PropZInt Screen.png")
        st.image("screenshots/09 Popped 1-PropZInt.png")

    st.subheader("Step 3")
    col1step3_p, col2step3_p = st.columns(2)
    with col1step3_p:
        st.markdown("When you press calculate you should see an interval just like with `ZInterval`  and `TInterval` "
                    "which shows the proportion estimate and the sample size.")
    with col2step3_p:
        st.image("screenshots/09 1-PropZInt Result.png")