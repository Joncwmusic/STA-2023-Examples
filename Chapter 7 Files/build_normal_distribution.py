import math
import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
import plotly.graph_objs as go

def factorial(n):
    product = 1
    for i in range(n):
        product *= i + 1
    return product

def binompdf(n, p, x):
    prob = factorial(n)/(factorial(n-x)*factorial(x)) * p**x*(1-p)**(n-x)
    return prob

def binomcdf(n, p, x):
    sum = 0
    for i in range(x+1):
        sum += binompdf(n, p, i)
    return sum

def normpdf(mu, sigma, x):
    part_1 = 1/(sigma*math.sqrt(2*math.pi))
    part_2 = math.exp(-((x-mu)**2)/(2*sigma**2))
    return part_1 * part_2


def build_normal_distribution():

    dataset_coinflip_more = [binompdf(20, 0.5, i) for i in range(21)]
    dataset_norm_binomial_compare = [normpdf(10,math.sqrt(5),0.1*i) for i in range(200)]
    dataset_norm_standard = [normpdf(0, 1, 0.1 * i) for i in range(-40,40)]
    dataset_norm_change_sigma = [normpdf(0, 2, 0.1 * i) for i in range(-40,40)]
    dataset_norm_change_mu = [normpdf(2, 1, 0.1 * i) for i in range(-40,40)]

    df_coinflip_more = pd.DataFrame({"Num Heads": range(21), "Pr(x)": dataset_coinflip_more})
    df_norm_binomial = pd.DataFrame({"X": [0.1*i for i in range(200)], "Norm(X)":dataset_norm_binomial_compare})
    df_change_sigma = pd.DataFrame({"X": [0.1*i for i in range(-40,40)], "Norm(X)":dataset_norm_change_sigma})
    df_change_mu = pd.DataFrame({"X": [0.1*i for i in range(-40,40)], "Norm(X)":dataset_norm_change_mu})
    df_normal_standard = pd.DataFrame(({"X": [0.1*i for i in range(-40,40)], "Norm(X)":dataset_norm_standard}))


    ax_more = px.bar(data_frame=df_coinflip_more, x="Num Heads", y="Pr(x)")
    ax_norm_binomial = px.line(data_frame=df_norm_binomial, x="X", y="Norm(X)")
    ax_norm_mean = px.line(data_frame=df_normal_standard, x= "X", y="Norm(X)", title = "Centered on Mean")
    ax_norm_inflection = px.line(data_frame=df_normal_standard, x="X", y="Norm(X)", title="Inflection points")
    ax_norm_empirical = px.line(data_frame=df_normal_standard, x="X", y="Norm(X)", title= "Empirical Rule")
    ax_norm_standard = px.line(data_frame=df_normal_standard, x="X", y="Norm(X)",title="Standard Normal Curve")
    ax_norm_change_mu = px.line(data_frame=df_change_mu, x="X", y="Norm(X)", title = "Translation by changing mu")
    ax_norm_change_sigma = px.line(data_frame=df_change_sigma, x="X", y="Norm(X)", title = "Dilation by changing sigma")

    # connect binomial and normal distribution
    ax_more.add_traces(ax_norm_binomial.data)

    # add vertical line visuals
    ax_norm_mean.add_shape(type="line", x0=0, y0=0,
                                 x1=0, y1=0.4, line=dict(color="Blue", width=2, dash="dot"))

    ax_norm_inflection.add_shape(type="line", x0=-1, y0=0,
                                x1=-1, y1=0.4, line=dict(color="Red", width=2, dash="dot"))
    ax_norm_inflection.add_shape(type="line", x0=1, y0=0,
                           x1=1, y1=0.4, line=dict(color="Red", width=2, dash="dot"))

    ax_norm_empirical.add_shape(type="line", x0=-3, y0=0,
                                x1=-3, y1=0.4, line=dict(color="Red", width=2, dash="dot"))
    ax_norm_empirical.add_shape(type="line", x0=-2, y0=0,
                                x1=-2, y1=0.4, line=dict(color="Yellow", width=2, dash="dot"))
    ax_norm_empirical.add_shape(type="line", x0=-1, y0=0,
                                x1=-1, y1=0.4, line=dict(color="Green", width=2, dash="dot"))
    ax_norm_empirical.add_shape(type="line", x0=1, y0=0,
                                x1=1, y1=0.4, line=dict(color="Green", width=2, dash="dot"))
    ax_norm_empirical.add_shape(type="line", x0=2, y0=0,
                                x1=2, y1=0.4, line=dict(color="Yellow", width=2, dash="dot"))
    ax_norm_empirical.add_shape(type="line", x0=3, y0=0,
                                x1=3, y1=0.4, line=dict(color="Red", width=2, dash="dot"))

    # connect normal distribution with transformations
    ax_norm_change_mu.add_traces(ax_norm_standard.data)
    ax_norm_change_sigma.add_traces(ax_norm_standard.data)

    st.header("Why So Normal?")
    st.plotly_chart(ax_more)

    st.header("Characteristics of Normal")

    col1viz1, col2_viz1 = st.columns(2)
    with col1viz1:
        st.markdown(" - Normal Distribution is symmetrical around the mean (which is also the median and the mode).")
        st.markdown("- As you move left or right ont he normal curve towards infinity it will always approach but never"
                    " touch the x axis. i.e. ")
        st.markdown("- The area under the curve of a normal distribution is 1, i.e. when you 'sum' the probabilities "
                    "you should get the entire distribution. ")
        st.markdown(r"$x \rightarrow \pm \infty \Rightarrow y \rightarrow 0$")
    with col2_viz1:
        st.plotly_chart(ax_norm_mean, height = 350)


    col1viz2, col2_viz2 = st.columns(2)
    with col1viz2:
        st.markdown(r" - Normal Distributions have inflection points one standard deviation away from the mean at "
                    r"$\mu-\sigma$ and $\mu + \sigma$.")
    with col2_viz2:
        st.plotly_chart(ax_norm_inflection, height = 350)

    col1viz3, col2_viz3 = st.columns(2)
    with col1viz3:
        st.markdown(" - **The Empirical Rule:** 68% of data lives within 1 standard deviation, 95% lives within 2 "
                    "standard deviations, and 99.7% lives within 3 standard deviations.")
    with col2_viz3:
        st.plotly_chart(ax_norm_empirical, height = 350)

    st.header("Standardizing the Normal Curve")
    st.plotly_chart(ax_norm_change_sigma)
    st.plotly_chart(ax_norm_change_mu)

    st.header("Z-Score and finding probabilities")