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
    # T TEST
    st.header("How to Hypothesis Test: `T-Test` vs. `Z-Test`")
    st.markdown("You use `T-Test` when:")
    st.markdown("- You don't know the population standard deviation and instead have the sample standard deviation.")
    st.markdown("- The sample size is less than 30.")
    st.markdown("you should take note if the sample size is greater than 30 the t-distribution is 'effectively' the "
                "normal distribution and you can use `Z-Test` in this circumstance, but when in doubt use `T-Test`")

    st.subheader("Step 1")
    col1step1_t, col2step1_t = st.columns(2)
    with col1step1_t:
        st.markdown(r"Press *STAT* then navigate to the **TESTS** menu and you'll see `Z-Test` and `T-Test`.")
        st.markdown("Highlight `T-Test` press **ENTER** to fill in the necessary parameters.")
    with col2step1_t:
        st.image("screenshots/10 Tests Screen.png")

    st.subheader("Step 2")
    col1step2_t, col2step2_t = st.columns(2)
    with col1step2_t:
        st.markdown("There are two options for inputting your parameters:")
        st.markdown(r"""
                * For the Stats input you fill in:
                    * The assumed mean the null hypothesis is asserting $\mu_{0}$
                    * The sample mean $\bar{x}$ from your sample
                    * The sample standard deviation: `Sx
                    * The sample size: `n`
                    * Lastly, the type of test:
                        * 2Tail: $ \neq \mu_0$
                        * Left Tail: $ <\mu_0$
                        * Right: Tail $ > \mu_0$
                    """)
                        
        st.markdown(r"""
                * For the Data Input you need to fill in:
                    * The assumed mean the null hypothesis is asserting $\mu_{0}$
                    * `List` for the list holding your data
                    * The Frequency List (for weighted data) for us, we can default this to 1
                    * Then, the type of test:
                        * 2Tail: $ \neq \mu_0$
                        * Left Tail: $ <\mu_0$
                        * Right: Tail $ > \mu_0$)
                """)
    with col2step2_t:
        st.subheader("Stats Input")
        st.image("screenshots/10 T-Test Stats Input Blank.png")
        st.image("screenshots/10 T-Test Stats Input Popped.png")
        st.subheader("Data Input")
        st.image("screenshots/10 T-Test Data Input Blank.png")

    st.subheader("Step 3")
    col1step3_t, col2step3_t = st.columns(2)
    with col1step3_t:
        st.markdown(r" When you press calculate you should see a screen that has the critical value `t`, the p value, "
                    r"`p`, and summary statistics $\bar{x}$, `Sx`, and `n` respectively.")
    with col2step3_t:
        st.image("screenshots/10 T-Test Result Screen.png")

    # 1 PROP Z TEST
    st.header("Hyp. Test for Proportions: `1-PropZTest`")
    st.subheader("Step 1")
    col1step1_p, col2step1_p = st.columns(2)
    with col1step1_p:
        st.markdown(r"Press *STAT* then navigate to the **TESTS** menu and you'll see `1-PropZTest`.")
        st.markdown("Highlight `1-PropZTest` press **ENTER** to fill in the necessary parameters.")
    with col2step1_p:
        st.image("screenshots/10 Tests Screen.png")

    st.subheader("Step 2")
    col1step2_p, col2step2_p = st.columns(2)
    with col1step2_p:
        st.markdown(r"""
                        * For the input you will need to fill in:
                            * The assumed proportion the null hypothesis is asserting $p_{0}$
                            * The number of successes or 'yes votes' in your proportion.
                            * The sample size: `n`
                            * Lastly, the type of test:
                                * 2Tail: $ \neq p_0$
                                * Left Tail: $ < p_0$
                                * Right: Tail $ > p_0$
                            """)
    with col2step2_p:
        st.image("screenshots/10 1-PropZTest Input Blank.png")
        st.image("screenshots/10 1-PropZTest Input Popped.png")

    st.subheader("Step 3")
    col1step3_p, col2step3_p = st.columns(2)
    with col1step3_p:
        st.markdown(r" When you press calculate you should see a screen that has the critical value `z`, the p value, "
                    r"`p`, and summary statistics $\hat{p}$ and `n` respectively.")
    with col2step3_p:
        st.image("screenshots/10 1-PropZTest Result.png")