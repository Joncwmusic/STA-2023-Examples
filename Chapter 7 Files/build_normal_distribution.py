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
    dataset_norm_standard_left_tail_ex1 = [normpdf(0, 1, 0.1 * i) for i in range(-40, -20)]
    dataset_norm_standard_right_tail_ex1 = [normpdf(0, 1, 0.1 * i) for i in range(-20, 40)]
    dataset_norm_standard_left_tail_ex2 = [normpdf(0, 1, 0.1 * i) for i in range(-40, 20)]
    dataset_norm_standard_right_tail_ex2 = [normpdf(0, 1, 0.1 * i) for i in range(20, 40)]

    df_coinflip_more = pd.DataFrame({"Num Heads": range(21), "Pr(x)": dataset_coinflip_more})
    df_norm_binomial = pd.DataFrame({"X": [0.1*i for i in range(200)], "Norm(X)":dataset_norm_binomial_compare})
    df_change_sigma = pd.DataFrame({"X": [0.1*i for i in range(-40,40)]
                                    , "Norm(X)":dataset_norm_change_sigma
                                    , "Color":["Red" for i in range(-40,40)]})
    df_change_mu = pd.DataFrame({"X": [0.1*i for i in range(-40,40)]
                                    , "Norm(X)":dataset_norm_change_mu
                                    , "Color":["Red" for i in range(-40,40)]})
    df_normal_standard = pd.DataFrame(({"X": [0.1*i for i in range(-40,40)]
                                    , "Norm(X)":dataset_norm_standard
                                    , "Color":["Blue" for i in range(-40,40)]}))

    df_left_tail_ex1 = pd.DataFrame(({"X": [0.1*i for i in range(-40,-20)], "Norm(X)":dataset_norm_standard_left_tail_ex1}))
    df_right_tail_ex1 = pd.DataFrame(({"X": [0.1*i for i in range(-20,40)], "Norm(X)":dataset_norm_standard_right_tail_ex1}))
    df_left_tail_ex2 = pd.DataFrame(({"X": [0.1*i for i in range(-40,20)], "Norm(X)":dataset_norm_standard_left_tail_ex2}))
    df_right_tail_ex2 = pd.DataFrame(({"X": [0.1*i for i in range(20,40)], "Norm(X)":dataset_norm_standard_right_tail_ex2}))

    ax_more = px.bar(data_frame=df_coinflip_more, x="Num Heads", y="Pr(x)")
    ax_norm_binomial = px.line(data_frame=df_norm_binomial, x="X", y="Norm(X)")
    ax_norm_mean = px.line(data_frame=df_normal_standard, x= "X", y="Norm(X)", title = "Centered on Mean")
    ax_norm_inflection = px.line(data_frame=df_normal_standard, x="X", y="Norm(X)", title="Inflection points")
    ax_norm_empirical = px.line(data_frame=df_normal_standard, x="X", y="Norm(X)", title= "Empirical Rule")
    ax_norm_standard = px.line(data_frame=df_normal_standard, x="X", y="Norm(X)", title="Standard Normal Curve")
    ax_norm_change_mu = px.line(data_frame=df_change_mu, x="X", y="Norm(X)", title="Translation by changing mu")
    ax_norm_change_sigma = px.line(data_frame=df_change_sigma, x="X", y="Norm(X)", title="Dilation by changing sigma")
    ax_left_tail_ex_1 = px.area(data_frame=df_left_tail_ex1, x="X", y="Norm(X)", title = "Area Left Tail")
    ax_right_tail_ex_1 = px.area(data_frame=df_right_tail_ex1, x="X", y="Norm(X)", title="Area Right Tail")
    ax_left_tail_ex_2 = px.area(data_frame=df_left_tail_ex2, x="X", y="Norm(X)", title="Area Left Tail")
    ax_right_tail_ex_2 = px.area(data_frame=df_right_tail_ex2, x="X", y="Norm(X)", title="Area Right Tail")

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
    trace_mu_change = ax_norm_standard.data[0]
    trace_mu_change.line = dict(color="red", width=2, dash="dot")

    trace_sigma_change = ax_norm_standard.data[0]
    trace_sigma_change.line = dict(color="red", width=2, dash="dot")

    ax_norm_change_mu.add_trace(trace_mu_change)
    ax_norm_change_sigma.add_trace(trace_sigma_change)

    # add full bell to area charts
    ax_right_tail_ex_1.add_traces(ax_norm_standard.data)
    ax_left_tail_ex_1.add_traces(ax_norm_standard.data)
    ax_right_tail_ex_2.add_traces(ax_norm_standard.data)
    ax_left_tail_ex_2.add_traces(ax_norm_standard.data)

    st.header("Why So Normal?")
    st.markdown("So there's a connection between binomial distribution which was covered in chapter 6 and this normal "
              "bell-shaped thing. It's as simple as this: When you increase the number of trials the shape of the "
              "discrete probability distribution gets closer and closer to a bell shape. And in fact you can "
              "generally approximate sufficiently large binomial experiments and their probabilities to a normal "
              "distribution with mean = np and variance being np(1-p).")
    st.plotly_chart(ax_more)

    st.markdown("In general, normal distributions occur in several measurements we observe just by happenstance. So "
                "it'd be good to go over some characteristics of these distributions.")

    st.header("Characteristics of Normal Distribution.")

    col1viz1, col2_viz1 = st.columns(2)
    with col1viz1:
        st.markdown("- Normal Distribution is symmetrical around the mean (which is also the median and the mode).")
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

    st.markdown("Now not every normally distributed metric has the same mean or standard deviation BUT we can define "
                "a standard normal curve by default. The **STANDARD** normal curve has mean 0 and standard deviation "
                "of 1. Seems simple enough. Now let's take a look at what happens when we manipulate mu and sigma.")
    st.plotly_chart(ax_norm_change_mu)

    st.markdown("Notice how when we change mu the curve moves left and right.")
    st.plotly_chart(ax_norm_change_sigma)
    st.markdown("Notice that when sigma changes the curve gets... more flat. That's because the area under the curve "
                "is STILL 1 but the **spread** is more so naturally it would flatten itself to get a higher.")

    st.header("Z-Score and finding probabilities")
    st.markdown("If you remember from earlier in the semester, we said you can standardize your data by finding the "
                "Z score for your data points which will transform your dataset to have an average of 0 and standard "
                "deviation of 1. It's like changing your bell curve to fit the standard normal curve.")

    st.markdown(r"$Z = \dfrac{x-\mu}{\sigma}$")

    st.subheader("Area Under the Curve")
    st.markdown("In order to find probabilities for normally distributed probabilities, you need to find the area "
                "under the curve. That's much easier said than done. BUT you can use either A) empirical rule, B) "
                "your calculator or C) if you're still in the stone age, a Z table.")

    st.subheader("Empirical Rule")
    st.markdown("If you know empirical rule you might be able to estimate probability if you're estimating "
                "probabilities. For example if you have a dataset with IQ scores with mean 100 and standard "
                "deviation 15 and you score 130 because you're a genius. You can calculate the z score which "
                "is (130-100)/15 which equals 2 and say 95% of IQ scores fit between 70 and 130. This means 5% "
                "exist outside of that range and you're on the upper half so you're about in the top 2.5% ")
    st.markdown("i.e $Pr(X>130) = Pr(Z>2) = 0.025$")

    st.subheader("Using your Calculator")
    st.markdown("Your calculator has a function normcdf() which takes in 4 inputs: a lower bound, an upper bound, "
                "mean, and standard deviation. So if you're doing the same example with IQs then a score of 130. "
                "You can even translate the problem to a Z score and use mu=0 and sigma=1 and get the same answer. ")
    st.markdown("So, Pr(X>130) = normalcdf(130, big number, 100, 15) OR Pr(Z>2) = normalcdf(2, big number, 0, 1)")

    st.subheader("Using a Z Table")
    st.markdown("Okay same scenario but when using a z table you'd first convert your data into z scores then you'd "
                "lookup the z value in the table and that will return the probability. Each table online is a little"
                "difference but otherwise is very intuitive if you're in a pinch and don't feel like dusting off the "
                "TI84 you haven't used all semester.")

    st.image("screenshots/07 z table example")


    st.header("Visualizing probabilities")

    col1tail, col2tail = st.columns(2)

    with col1tail:
        st.plotly_chart(ax_left_tail_ex_1)
        st.markdown(r"$Pr(Z < 2)$")
        st.plotly_chart(ax_left_tail_ex_2)
        st.markdown(r"$Pr(Z < -2)$")
    with col2tail:
        st.plotly_chart(ax_right_tail_ex_1)
        st.markdown(r"$Pr(Z > 2)$")
        st.plotly_chart(ax_right_tail_ex_2)
        st.markdown(r"$Pr(Z > -2)$")


