import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
import math
import plotly.graph_objects as go


def normpdf(mu, sigma, x):
    part_1 = 1 / (sigma * math.sqrt(2 * math.pi))
    part_2 = math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
    return part_1 * part_2


def gamma_integrand(t, alpha):
    return (t ** (alpha - 1)) * math.exp(-t)


def area_interval_gamma(start_a, end_b, alpha, func):
    area_sum = func(end_b, alpha) + 4 * (func((end_b + start_a) / 2, alpha)) + func(start_a, alpha)
    avg_area = area_sum * (end_b - start_a) / 6
    return avg_area


def area_interval(start_a, end_b, mu, sigma, func):
    area_sum = func(mu, sigma, end_b) + 4 * (func(mu, sigma, (end_b + start_a) / 2)) + func(mu, sigma, start_a)
    avg_area = area_sum * (end_b - start_a) / 6
    return avg_area


def normalcdf(lb, up, mu=0, sigma=1, precision=0.1, nsteps=1000):
    current_sum = 0
    current_start = 0
    next_point = current_start + precision
    for i in range(nsteps):
        temp_sum = area_interval(current_start, next_point, mu, sigma, normpdf)
        current_sum += temp_sum
        current_start = next_point
        next_point += precision
    return current_sum


def gamma_function(alpha, step=0.1, nsteps=1000):
    current_sum = 0
    current_start = 0
    next_point = current_start + step
    for i in range(nsteps):
        temp_sum = area_interval_gamma(current_start, next_point, alpha, gamma_integrand)
        current_sum += temp_sum
        current_start = next_point
        next_point += step
    return current_sum


def invNorm(area, mu=0, sigma=1, lcr="LEFT", precision=0.01):
    current_sum = 0
    if area > 1 or area < -1:
        raise ValueError("Invalid value for area. Must be between 0 and 1")
    if lcr == "LEFT":
        current_step = -10
        while current_sum < area:
            current_sum += precision * normpdf(mu, sigma, current_step)
            current_step += precision
        return current_step
    elif lcr == "RIGHT":
        current_step = -10
        while current_sum < area:
            current_sum += precision * normpdf(mu, sigma, current_step)
            current_step -= precision
        return current_step
    elif lcr == "CENTER":
        current_step_L = 0
        current_step_R = 0
        while current_sum < area:
            current_sum += precision * normpdf(mu, sigma, current_step_L)
            current_sum += precision * normpdf(mu, sigma, current_step_R)
            current_step_L -= precision
            current_step_R += precision
        return current_step_L, current_step_R
    else:
        raise ValueError("Invalid value for lcr parameter. Values are LEFT, RIGHT, or CENTER")


def t_distribution(x, df):
    numerator_part_1 = gamma_function((df + 1) / 2)
    denominator_part_1 = math.sqrt(df * math.pi) * gamma_function(df / 2)
    base_part_2 = 1 + x ** 2 / df
    exponent_part_2 = -(df + 1) / 2
    part_1 = numerator_part_1 / denominator_part_1
    part_2 = base_part_2 ** exponent_part_2
    print(numerator_part_1, denominator_part_1, " Divide these to get: ", part_1)
    print(base_part_2, exponent_part_2, " Raise to the power to get: ", part_2)
    print("Current_Values, (" + str(x) + "," + str(part_1 * part_2) + ")")
    return part_1 * part_2


def invT(area, df=30, lcr="LEFT", precision=0.01):
    current_sum = 0
    if area > 1 or area < -1:
        raise ValueError("Invalid value for area. Must be between 0 and 1")
    if lcr == "LEFT":
        current_step = -10
        while current_sum < area:
            current_sum += precision * t_distribution(current_step, df)
            current_step += precision
        return current_step
    elif lcr == "RIGHT":
        current_step = -10
        while current_sum < area:
            current_sum += precision * t_distribution(current_step, df)
            current_step -= precision
        return current_step
    elif lcr == "CENTER":
        current_step_L = 0
        current_step_R = 0
        while current_sum < area:
            current_sum += precision * t_distribution(current_step_L, df)
            current_sum += precision * t_distribution(current_step_R, df)
            current_step_L -= precision
            current_step_R += precision
        return current_step_L, current_step_R
    else:
        raise ValueError("Invalid value for lcr parameter. Values are LEFT, RIGHT, or CENTER")



def build_t_distribution():
    x_vals = [i / 20 for i in range(-100, 100)]
    t_dist_3 = [t_distribution(i, 3) for i in x_vals]
    t_dist_8 = [t_distribution(i, 8) for i in x_vals]
    t_dist_15 = [t_distribution(i, 15) for i in x_vals]
    norm_dist_0_1 = [normpdf(0, 1, i) for i in x_vals]

    norm_0_1_df = pd.DataFrame({"x_vals": x_vals, "y_vals": norm_dist_0_1, "dist": ["normal" for i in x_vals]})
    t_3_df = pd.DataFrame({"x_vals": x_vals, "y_vals": t_dist_3, "dist": ["df=3" for i in x_vals]})
    t_8_df = pd.DataFrame({"x_vals": x_vals, "y_vals": t_dist_8, "dist": ["df=8" for i in x_vals]})
    t_15_df = pd.DataFrame({"x_vals": x_vals, "y_vals": t_dist_15, "dist": ["df=15" for i in x_vals]})

    all_dist_df = pd.concat([norm_0_1_df, t_3_df, t_8_df, t_15_df])

    color_map_for_normal_vs_t = {"normal": "0000ff", "df=3": "ff0000", "df=8": "bb1111", "df=15": "992222"}

    fig_norm_0_1_solo = px.line(data_frame=norm_0_1_df, x="x_vals", y="y_vals", title="standard normal plot")
    fig_norm_0_1 = px.line(data_frame=norm_0_1_df, x="x_vals", y="y_vals"
                           , color_discrete_map=color_map_for_normal_vs_t, title="normal plot vs. t distributions")

    fig_all_dist = px.line(data_frame=all_dist_df, x="x_vals", y="y_vals", color="dist")

    st.header("Why the t Distribution?")
    st.markdown("When the underlying data is non normal the distribution of the sample mean still isn't normal for "
                "small sample sizes (generally n<30). In addition to that, when estimating population parameters like "
                "the mean, we don't usually have access to the population standard deviation. So, the standard error "
                "from chapter 8 is well... different.")
    st.markdown(r"instead of the distribution of "
                r"$\sigma_{\bar{x}} = \dfrac{\sigma}{\sqrt{n}}$ "
                r"we have to sub in with our sample standard deviation "
                r"$\dfrac{s}{\sqrt{n}}$. I won't go into the details but you can intuit that sample standard deviation "
                r"$s$ is always a little higher than $\sigma$ which would imply a slightly different distribution to "
                r"use for something like a confidence interval to estimate the mean.")
    st.header("Properties of t Distribution")
    st.markdown(r"""
    - The t distribution is actually a series of different distributions depending on the sample size (degrees of 
    freedom = sample size - 1).
    - t distributions are centered at $\mu$ = 0 and are symmetrical and bell shaped.
    - The tails of a t-distribution are thicker than that of a normal distribution.
    - As the degrees of freedom increases it approaches a normal distribution.
    - The total area under the curve(s) is 1 just like any other continuous distribution.
    - As $t \rightarrow \pm \infty$, $y \rightarrow 0$
    """)

    st.subheader("t Distribution at Various Degrees of Freedom (df)")
    st.plotly_chart(fig_all_dist)
