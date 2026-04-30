import random
import pandas as pd
import streamlit as st
import math
import plotly.express as px
import plotly.io as pio


def normpdf(mu, sigma, x):
    part_1 = 1 / (sigma * math.sqrt(2 * math.pi))
    part_2 = math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
    return part_1 * part_2


def gamma_integrand(t, alpha):
    return (t ** (alpha - 1)) * math.exp(-t)


def area_interval(start_a, end_b, alpha, func):
    area_sum = func(end_b, alpha) + 4 * (func((end_b + start_a) / 2, alpha)) + func(start_a, alpha)
    avg_area = area_sum * (end_b - start_a) / 6
    return avg_area


def gamma_function(alpha, step, nsteps=1000):
    current_sum = 0
    current_start = 0
    next_point = current_start + step
    for i in range(nsteps):
        temp_sum = area_interval(current_start, next_point, alpha, gamma_integrand)
        current_sum += temp_sum
        current_start = next_point
        next_point += step
    return current_sum


def gamma_dist(x, alpha, beta, step):
    numerator = x ** (alpha - 1) * math.exp(-beta * x) * beta ** alpha
    denominator = gamma_function(alpha, step)
    return numerator / denominator


def exp_distribution(rate_param, x):
    return rate_param * math.exp(-rate_param * x)


def build_calculator_notes():
    # 2 Prop Test
    st.header("Using `2-PropZTest` and `2-SampTTest`")

    st.subheader("Step 1 - `2-SampTTest`")
    col1step1_t, col2step1_t = st.columns(2)
    with col1step1_t:
        st.markdown(r"Press *STAT* then navigate to the **TESTS** menu and you'll see `2-SampTTest`.")
        st.markdown("Highlight `2-SampTTest` press **ENTER** to fill in the necessary parameters.")
    with col2step1_t:
        st.image("screenshots/11 Stat Test Highlight 2-SampTTest.png")

    st.subheader("Step 2 - `2-SampTTest`")
    st.markdown("Now you'll a see a screen to fill in your paramters. There are two options for this. You can "
                "either (1) enter your data into `L1` and `L2` and use the data input or (2) input the means and "
                "sample standard deviations, and sample sizes directly with the stats input:")
    col1step2_t, col2step2_t = st.columns(2)
    with col1step2_t:
        st.markdown(r"""
                * For the Stats input you fill in:
                    * The sample means $\bar{x}_1$ and $\bar{x}_2$ from your sample
                    * The sample standard deviation: `Sx1` and `Sx2`
                    * The sample size: `n1` and `n2`
                    * For our course select `No` for the `pooled` option
                    * Lastly, the type of test:
                        * 2Tail: $ \neq \mu_0$
                        * Left Tail: $ <\mu_0$
                        * Right: Tail $ > \mu_0$
                    """)

        st.markdown(r"""
                * For the Data Input you need to fill in:
                    * `List1` and `List2` with the lists holding your data (maybe `L1` and `L2`)
                    * `Freq1` and `Freq2` are frequencies for weighted data, we can default this to 1 for our course
                    * For our course select `No` for the `pooled` option
                    * Then, the type of test:
                        * 2Tail: $ \neq \mu_2$
                        * Left Tail: $ <\mu_2$
                        * Right: Tail $ > \mu_2$)
                """)
    with col2step2_t:
        st.subheader("Stats Input")
        st.image("screenshots/11 2-SampTTest Stats Screen.png")
        st.subheader("Data Input")
        st.image("screenshots/11 2-SampTTest Data Screen.png")

    st.subheader("Step 3 - `2-SampTTest`")
    col1step3_t, col2step3_t = st.columns(2)
    with col1step3_t:
        st.markdown(r" When you press calculate you should see a screen that has the critical value `t`, the p value, "
                    r"`p`, and summary statistics $\bar{x}_1$, $\bar{x}_2$, `Sx1`, `Sx2`, `n1`, and `n2` respectively.")
    with col2step3_t:
        st.image("screenshots/11 2-SampTTest Result Screen.png")


    st.subheader("Step 1 - `2-PropZTest`")
    col1step1_p, col2step1_p = st.columns(2)
    with col1step1_p:
        st.markdown(r"Press *STAT* then navigate to the **TESTS** menu and you'll see `2-PropZTest`.")
        st.markdown("Highlight `2-PropZTest` press **ENTER** to fill in the necessary parameters.")
    with col2step1_p:
        st.image("screenshots/11 Stat Test Highlight 2-PropZTest.png")

    st.subheader("Step 2 - `2-PropZTest`")
    col1step2_p, col2step2_p = st.columns(2)
    with col1step2_p:
        st.markdown(r"""
                        * For the input you will need to fill in:
                            * `x1` and `x2`, The number of successes or 'yes votes' in each group.
                            * The sample sizes: `n1` and `n2`
                            * And lastly, the type of test:
                                * 2Tail: $ \neq p_2$
                                * Left Tail: $ < p_2$
                                * Right: Tail $ > p_2$
                            """)
    with col2step2_p:
        st.image("screenshots/11 2-PropZTest Input Screen.png")

    st.subheader("Step 3 - `2-PropZTest`")
    col1step3_p, col2step3_p = st.columns(2)
    with col1step3_p:
        st.markdown(r" When you press calculate you should see a screen that has the critical value `z`, the p value, "
                    r"`p`, and point estimates for each proportion as well as the pooled proportion: $\hat{p}_1$, "
                    r"$\hat{p}_2$, and $\hat{p}$ (pooled) and then `n1` and `n2`, respectively.")
    with col2step3_p:
        st.image("screenshots/11 2-PropZTest Result Screen.png")