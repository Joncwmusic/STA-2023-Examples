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
    normal_x_vals = [x / 20 - 5 for x in range(200)]
    x_vals = [x / 20 for x in range(100)]

    normal_example = [normpdf(mu=0, sigma=1, x=i) for i in normal_x_vals]

    normal_df = pd.DataFrame({"x_vals": normal_x_vals, "y_vals": normal_example})

    # add continuous distributions
    fig_normal = px.line(data_frame=normal_df, x="x_vals", y="y_vals", title="Normal Distribution")

    fig_normal.add_shape(type="line", x0=1, y0=0,
                                x1=1, y1=0.24, line=dict(color="Red", width=2, dash="dot"))

    st.header("How to Sample Distribution on your TI 83 and TI 84")

    st.subheader("Calculate Area under a bell curve:")
    st.markdown(r"A lot of questions will ask you to find $Pr(\bar{x} < x_0)$ which is the area under the curve for the"
                r" distribution of the sample mean (to the left of $x_0$). The function you'll use in your calculator "
                r"is `normalcdf()`which takes 4 inputs, namely: a Lower Bound, Upper Bound, Mean, and Standard "
                r"Deviation which we'll substitute with standard error ($\sigma_{\hat{p}}$ and $\sigma_{\bar{x}}$).")

    st.subheader("Step 1")
    step1col1_area, step1col2_area = st.columns(2)
    with step1col1_area:
        st.markdown("First you need to press *2ND* and then *VARS* on your calculator. This will take you to the "
                    "distribution menu. There you will find the functions `normalcdf` and `normalpdf`. `normalcdf` "
                    "will get you the area under the curve while `normalpdf` will give you the height at the point. "
                    "In our class we will 99% of the time encounter problems that require `normalcdf`. If a question "
                    "asks you to find $Pr(X=x_0)$, it's 0 for continuous distributions like normal distribution. "
                    "Do not use `normalpdf` like you would otherwise do with binomial distribution.")
    with step1col2_area:
        st.image("screenshots/07 distr menu.png")

    st.subheader("Step 2")
    step2col1_area, step2col2_area = st.columns(2)
    with step2col1_area:
        st.markdown(r"When you select `normalcdf` it will likely give you a screen where you can choose your inputs. "
                    r"That is, an upper bound, a lower bound, your mean, $\mu$, and your standard deviation $\sigma$. ")
        st.markdown(r""" 
                * If you're finding $Pr(X < x_0)$ you'll plug in: 
                    * `lower:` negative big number
                    * `upper:` $x_0$
                    * $\mu$: the mean 
                    * $\sigma$: the standard deviation
                    """)
        st.markdown(r""" 
                * If you're finding $Pr(X > x_0)$ you'll plug in: 
                    * `lower:` $x_0$
                    * `upper:` big number
                    * $\mu$: the mean 
                    * $\sigma$: the standard deviation
                    """)
        st.markdown(r""" 
                        * If you're finding $Pr(x_1 < X < x_2)$ you'll plug in: 
                            * `lower:` $x_1$
                            * `upper:` $x_2$
                            * $\mu$: the mean 
                            * $\sigma$: the standard deviation
                            """)
    with step2col2_area:
        st.image("screenshots/07 normalcdf screen.png")
        st.image("screenshots/07 normalcdf popped.png")

    st.subheader("Step 3")
    step3col1_area, step3col2_area = st.columns(2)
    with step3col1_area:
        st.markdown("Once you input your values, you can select paste and it will populate your home screen with the "
                    "function and the inputs automagically. From there you simply press enter and the result will be "
                    "a value between 0 and 1. (After all, it is a probability.)")
    with step3col2_area:
        st.image("screenshots/07 normalcdf pasted.png")
        st.image("screenshots/07 normalcdf result.png")

    st.subheader("REMINDER")
    step4col1_area, step4col2_area = st.columns(2)
    with step4col1_area:
        st.markdown("Remember `normalcdf` and `normalpdf` will return different values. The cumulative function will "
                    "return the area under the curve between your upper and lower bounds. In contrast the probability "
                    "density function will return the height of the graph as plotted.")
    with step4col2_area:
        st.image("screenshots/07 normalcdf screen.png")
        st.image("screenshots/07 normalpdf view.png")

    st.subheader(r"Calculate x values (critical values) if given the area:")
    st.markdown(r"Now you might be wondering how to find an x value given an area. This depends on if you're looking "
                r"at the left, right, or center of the bell curve. Because that changes the inputs to our `invNorm()` "
                r"function on our calculators.")

    st.plotly_chart(fig_normal)

    st.subheader("Step 1")
    step1col1, step1col2 = st.columns(2)
    with step1col1:
        st.markdown("Before we input anything, we need to go to the distribution menu by pressing *2ND* and then *VARS*"
                    " and highlighting `invNorm` before pressing enter.")
    with step1col2:
        st.image("screenshots/07 distr menu.png")

    st.subheader("Step 2")
    step2col1, step2col2 = st.columns(2)
    with step2col1:
        st.markdown(r"You'll see a screen with the inputs `area:`, $\mu$:, and $\sigma$. You may also see an option "
                    r"for selecting LEFT, RIGHT, or CENTER.")
        st.markdown(r"""
        * If you're using a TI84+CE you do not have to adjust invNorm for 1 or 2 tail areas.
        Only use the following if you don't have the LEFT RIGHT CENTER option in your calculator
        * If you're looking for the area on the LEFT tail
            * `area` : the area you're looking for
            * $\mu$ : your mean
            * $\sigma$ : your standard deviation
        * If you're looking for the area on the RIGHT tail
            * `area` : 1 minus the area
            * $\mu$ : your mean
            * $\sigma$ : your standard deviation$
        * If you're looking for the area in the CENTER:
            * `area` : (1 minus the area)/2
            * $\mu$ : your mean
            * $\sigma$ : your standard deviation4
        """)
    with step2col2:
        st.image("screenshots/07 invNorm screen.png")
        st.image("screenshots/07 invNorm popped.png")

    st.subheader("Step 3")
    step3col1, step3col2 = st.columns(2)
    with step3col1:
        st.markdown("From here all you have to do is paste the function and verify it makes sense with the visuals in "
                    "your particular problem.")
    with step3col2:
        st.image("screenshots/07 invNorm pasted.png")
        st.image("screenshots/07 invNorm result.png")

