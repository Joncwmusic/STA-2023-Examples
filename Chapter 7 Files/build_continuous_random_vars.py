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

def build_continuous_probability_densities():

    discrete_x_vals = [1, 2, 3, 4, 5]
    normal_x_vals = [x/20 - 5 for x in range(200)]
    x_vals = [x/20 for x in range(100)]

    scatter_vals = {"x_vals":[-2, 1, 4, 10],"y_vals":[-3, 5, -1, 7]}

    uniform_example = [0.2 for i in x_vals]
    discrete_example = [0.18, 0.12, 0.35, 0.22, 0.13]
    normal_example = [normpdf(mu=0, sigma=1, x=i) for i in normal_x_vals]
    exponential_example = [exp_distribution(rate_param=0.5, x=i) for i in x_vals]

    continuous_example_gamma_2_2 = [gamma_dist(i, 2, 2, 0.1) for i in x_vals]
    continuous_example_gamma_5_5 = [gamma_dist(i, 5, 5, 0.1) for i in x_vals]
    continuous_example_gamma_5_10 = [gamma_dist(i, 5, 10, 0.1) for i in x_vals]
    continuous_example_gamma_10_5 = [gamma_dist(i, 10, 5, 0.1) for i in x_vals]

    discrete_df = pd.DataFrame({"x_vals":discrete_x_vals,"y_vals":discrete_example})
    uniform_df = pd.DataFrame({"x_vals":x_vals, "y_vals":uniform_example})
    normal_df = pd.DataFrame({"x_vals":normal_x_vals, "y_vals":normal_example})
    exponential_df = pd.DataFrame({"x_vals":x_vals, "y_vals":exponential_example})

    gamma_2_2_df = pd.DataFrame({"x_vals":x_vals,"y_vals":continuous_example_gamma_2_2})
    gamma_5_5_df = pd.DataFrame({"x_vals": x_vals, "y_vals": continuous_example_gamma_5_5})
    gamma_5_10_df = pd.DataFrame({"x_vals": x_vals, "y_vals": continuous_example_gamma_5_10})
    gamma_10_5_df = pd.DataFrame({"x_vals": x_vals, "y_vals": continuous_example_gamma_10_5})

    fig_discrete = px.bar(data_frame=discrete_df, x = "x_vals", y="y_vals", title = "Discrete Distribution")
    fig_uniform = px.line(data_frame=uniform_df, x="x_vals", y="y_vals", title="Uniform Distribution")
    fig_uniform_point = px.line(data_frame=uniform_df, x="x_vals", y="y_vals", title="Uniform Distribution Pr(X=2.5)")
    fig_uniform_range = px.line(data_frame=uniform_df, x="x_vals", y="y_vals", title="Uniform Distribution Pr(2<X<3)")

    # add vertical lines
    fig_uniform.add_shape(type="line", x0=0,y0=0,
                            x1=0, y1=0.2, line=dict(color="Blue", width=2,dash="dot"))
    fig_uniform.add_shape(type="line", x0=5, y0=0,
                          x1=5, y1=0.2, line=dict(color="Blue", width=2, dash="dot"))
    fig_uniform_point.add_shape(type="line", x0=2.5, y0=0,
                          x1=2.5, y1=0.2, line=dict(color="Red", width=2, dash="dot"))
    fig_uniform_range.add_shape(type="line", x0=2, y0=0,
                          x1=2, y1=0.2, line=dict(color="Red", width=2, dash="dot"))
    fig_uniform_range.add_shape(type="line", x0=3, y0=0,
                          x1=3, y1=0.2, line=dict(color="Red", width=2, dash="dot"))

    # add continuous distributions
    fig_normal = px.line(data_frame=normal_df, x="x_vals", y="y_vals", title="Normal Distribution")
    fig_exponential = px.line(data_frame=exponential_df, x="x_vals", y="y_vals", title = "Exponential Distribution")

    fig_gamma_2_2 = px.line(data_frame=gamma_2_2_df, x="x_vals", y="y_vals", title="Gamma Dist: alpha=2, beta=2")
    fig_gamma_5_5 = px.line(data_frame=gamma_5_5_df, x="x_vals", y="y_vals", title="Gamma Dist: alpha=5, beta=5")
    fig_gamma_5_10 = px.line(data_frame=gamma_5_10_df, x="x_vals", y="y_vals", title="Gamma Dist: alpha=5, beta=10")
    fig_gamma_10_5 = px.line(data_frame=gamma_10_5_df, x="x_vals", y="y_vals", title="Gamma Dist: alpha=10, beta=5")

    # format the streamlit page

    st.header("Continuous Random Variables")

    st.markdown("Let's say you're looking at a dart board contemplating probabilities because you're a weirdo. "
                "Let's also assume your dart is infinitesimally fine where if you hit the center of the board: the "
                "point (0,0) you actually hit EXACTLY (0,0) and not (0.00001, 0.000001). Let's say you're good enough "
                "to GUARANTEE hitting the board but not good enough to get an exact bullseye.")

    st.markdown("You know it's possible to hit anywhere on the dart board but the theoretical probability of hitting "
                "any one point is... 0. Literally you have uncountably many other options to hit besides that point."
                "How do we reconcile this paradox?")

    st.image("screenshots/07 dart board image.png")

    st.markdown("The answer is in translating our discrete mental models of Sample Spaces and Probabilities to a "
                "continuous mental model that looks at probabilities as densities instead of set values.")

    st.markdown("So, let's look at something a little more intuitive of a question. Let's say instead of hitting a "
                "specific point on our theoretical dark board, I ask what is the chance you hit the left region of the "
                "dart board? I think it's pretty intuitive to say you'd probably have a 50% chance of hitting that "
                "side of the board.")

    st.header("Uniform Distribution")
    st.markdown("So let's consider a scenario where you are applying for a job. But you notoriously run late. Let's "
                "also say you're guaranteed to show up somewhere between 0 and 5 minutes late? In this scenario "
                "I want to point out showing up 4 minutes and 1.43 seconds late IS different than 4 minutes and "
                "1.425 seconds late. How would we model those likelihoods? What's the probability of showing up "
                "exactly 2.5 minutes late?")

    st.plotly_chart(fig_uniform, key="plain")
    st.markdown("We can model this behavior with a **Uniform** Distribution. Any time is as likely as any other time "
                "but this leaves another issue: How to do we find exactly probabilities of specific input values?")

    st.plotly_chart(fig_uniform_point, key="with x=x_0")

    st.markdown("That's the neat part, you don't. Instead we ask what is the probability of being within a range of "
                "values and for uniform distributions finding the probability of a range is as finding: ")
    st.markdown(r"$\dfrac{x_2 - x_1}{\text{length of the Sample Space}}$")

    st.markdown("When I say length of the sample space I just mean to total range of possibilities so in other words: "
                "between 0 and 5 in this visual example. So if we want to find the probability of being between "
                "2 and 3 minutes late given we're guaranteed to be up to 5 minutes late we'd put:")
    st.markdown(r"$\dfrac{3-2}{5} = \dfrac{1}{5} = 0.2$")

    st.plotly_chart(fig_uniform_range, key="with x between x_0 and x_1")

    st.markdown("For other distributions it's much more complicated and relies on calculators and calculus. For the "
                "rest of the course we'll primarily be working with **normal distribution.**")

    st.subheader("Some Other examples of Continuous Distributions")
    st.markdown("The following are examples of continuous distributions. Don't be intimated we don't need to go over "
                "these besides normal distribution really BUT they are more common in advanced statistics courses "
                "that involve a baseline understanding of calculus.")

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig_normal, key="with others")
        st.plotly_chart(fig_gamma_2_2)
    with col2:
        st.plotly_chart(fig_gamma_10_5)
        st.plotly_chart(fig_exponential)

    st.header("Connecting Discrete and Continuous Perspectives")

    cont_col, disc_col = st.columns(2)

    with cont_col:
        st.subheader("Continuous Variables")
        st.markdown(r"Continuous random variables are infinitesimal. $Pr(X \leq x_0) = Pr(X<x_0)$")
        st.markdown(r"and $Pr(X=x) = 0$")
        st.plotly_chart(fig_normal, key="compare")
        st.markdown(r"$Pr(X < x_0) = \int_{-\infty}^{x_0}f(x)dx$")

        st.markdown("Probability Rules:")
        st.markdown(r"- $\int_{-\infty}^{\infty} Pr(x) = 1$")
        st.markdown(r"- $Pr(x) \geq 0$ for any $x$")

        st.markdown("Use a table or calculator, you don't need to worry about the calculus symbols!")

    with disc_col:
        st.subheader("Discrete Variables")
        st.markdown("Discrete random variables are 'countable' meaning they deal in whole numbers.")
        st.markdown(r"$Pr(X \leq x_0) = Pr(X < x_0) + Pr(X = x_0)$")
        st.plotly_chart(fig_discrete)
        st.markdown(r"$Pr(X \leq x_n) = \sum_{i=1}^n Pr(X = x_i)$")

        st.markdown("Probability Rules:")
        st.markdown(r"- $\sum Pr(x) = 1$")
        st.markdown(r"- $Pr(x) \geq 0$ for all $x$")






