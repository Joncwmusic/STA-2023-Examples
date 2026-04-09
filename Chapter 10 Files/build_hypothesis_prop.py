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

def build_hypothesis_prop():
    hypothesis_test_outcomes = {
        "Decision": ["Reject Null","Do Not Reject Null"],
        "Null is True": ["Type I Error", "Correct"],
        "Null is Not True": ["Correct", "Type II Error"],
    }

    # normal line data
    x_values_full = [i/50 for i in range(-200, 200)]
    x_values_left = [i / 50 for i in range(-200, -50)]
    x_values_right = [i / 50 for i in range(50, 200)]

    normal_full_line = [normpdf(mu=0, sigma=1, x=i) for i in x_values_full]
    normal_left_area = [normpdf(mu=0, sigma=1, x=i) for i in x_values_left]
    normal_right_area = [normpdf(mu=0, sigma=1, x=i) for i in x_values_right]
    normal_both_area = [normpdf(mu=0, sigma=1, x=i) if (i > 2 or i < -2) else 0 for i in x_values_full ]

    normal_full_line_df = pd.DataFrame({"x_val":x_values_full,"y_val":normal_full_line})
    normal_left_area_df = pd.DataFrame({"x_val": x_values_left, "y_val": normal_left_area})
    normal_right_area_df = pd.DataFrame({"x_val": x_values_right, "y_val": normal_right_area})
    normal_both_tail_df = pd.DataFrame({"x_val": x_values_full, "y_val": normal_both_area})

    normal_line_fig_right = px.line(data_frame=normal_full_line_df, x="x_val", y="y_val")
    normal_line_fig_right.add_scatter(x=normal_right_area_df['x_val']
                                     , y=normal_right_area_df['y_val']
                                     , fill='tozeroy', showlegend=False)
    normal_line_fig_left = px.line(data_frame=normal_full_line_df, x="x_val", y="y_val")
    normal_line_fig_left.add_scatter(x=normal_left_area_df['x_val']
                                , y=normal_left_area_df['y_val']
                                , fill='tozeroy', showlegend=False)
    normal_line_fig_both = px.line(data_frame=normal_full_line_df, x="x_val", y="y_val")
    normal_line_fig_both.add_scatter(x=normal_both_tail_df['x_val']
                                     , y=normal_both_tail_df['y_val']
                                     , fill='tozeroy', showlegend=False)

    st.header("What is a Hypothesis and How Do We Test It?")
    st.markdown("A Hypothesis is a statement about a parameter of a population. Some examples include: ")
    st.markdown(r"""
    * The average height of all students on a college campus is 68 inches.
    * The proportion of college educated students that want stricter gun laws is 58%
    * The average home price in Florida is 439000
    """)
    st.markdown("Now you could believe these statements and take them at face value but you're a skeptical researcher "
                "who wants to verify these facts. The problem is you have no money or resources to collect all of this "
                "information. What are you to do without the finances to ask every homeowner in florida to get the true"
                "average?")
    st.markdown("You *CAN* get a sample. But it won't be perfect. So we then have to *INFER* based on what we collect "
                "and define a threshold to determine if we should accept the statistical statement or not. Those "
                "thresholds are based on your sample size and more or less the likelihood of you just getting a bad "
                "sample if we assume the original statement is true.")

    st.subheader("The Type of Hypothesis Tests")
    st.markdown("Every hypothesis is framed around 2 statements. The first is the null hypothesis $H_0$. This is the "
                "statement you're trying to challenge. You assume this statement is true before collecting and "
                "analyzing your sample. The second is the alternative hypothesis to challenge the original claim $H_1$."
                " This will always challenge the null hypothesis depending on the context.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("2 Tail Tests")
        st.markdown(r"$H_0: \mu = \mu_0$")
        st.markdown(r"$H_1: \mu \neq \mu_0$")
        st.plotly_chart(normal_line_fig_both)
    with col2:
        st.markdown("Left Tail Tests")
        st.markdown(r"$H_0: \mu = \mu_0$")
        st.markdown(r"$H_1: \mu < \mu_0$")
        st.plotly_chart(normal_line_fig_left)
    with col3:
        st.markdown("Right Tail Tests")
        st.markdown(r"$H_0: \mu = \mu_0$")
        st.markdown(r"$H_1: \mu > \mu_0$")
        st.plotly_chart(normal_line_fig_right)

    st.header("Type I rand Type II Errors")
    st.markdown("When determining the outcome of a hypothesis test we have 4 options for how to conclude the test:")

    st.table(hypothesis_test_outcomes)

    st.markdown(r"""* We can be correct, which is when we reject the null hypothesis when it is false OR when we don't 
        reject the null when it is true.
        * Meanwhile if we reject a true null hypothesis then we have a Type I Error
        * Likewise if we fail to reject a false null hypothesis we have a Type II Error
    """)

    st.markdown(r"As it turns out this $\alpha$ value is just the probability of a Type I Error. In other words the "
                r"significance level is the probability of rejecting a true $H_0$")
    st.markdown(r"$\alpha = Pr(\text{Type I Error})$")

    st.markdown(r"""
       One Tail Critical Value Z Scores:

       - 90% Confidence $z_{\alpha} = z_{0.1} = 1.28$
       - 95% Confidence $z_{\alpha} = z_{0.05} = 1.645$
       - 99% Confidence $z_{\alpha} = z_{0.01} = 2.32$

       Two Tail Critical Value Z Scores:

       - 90% Confidence $z_{\alpha / 2} = z_{0.05} = 1.645$
       - 95% Confidence $z_{\alpha / 2} = z_{0.025} = 1.96$
       - 99% Confidence $z_{\alpha / 2} = z_{0.005} = 2.576$
       """)

    st.header("P Value Approach")

    st.markdown(r"$t_0 = \dfrac{\bar{x} - \mu}{\dfrac{s}{\sqrt{n}}}$")

    st.markdown(r"$Pr(t > t_0)$")
    st.markdown(r"$Pr(t > t_0)$")
    st.markdown(r"$Pr(t > |t_0|)$")

    st.markdown(r"""
       Critical Value P Values:

       - 90% Confidence $\alpha = 0.1$
       - 95% Confidence $\alpha = 0.05$
       - 99% Confidence $\alpha = 0.01$
       """)

    st.header("Outlining the Methods:")

    st.subheader("Method 1: The Classical Approach")

    st.markdown(r"""
        * Identify the null and alternative hypotheses and significance level (default to 0.05 if not given in a problem)
        * Compute the test statistic $z_0$ i.e. the z score for the sample mean or proportion
        * Compute $z_\alpha$ AKA the critical value to compare the test statistic to determine if you should reject $H_0$
        """)

    st.subheader("Method 2: The P Value Approach")

    st.markdown(r"""
        * Identify the null and alternative hypotheses and significance level (default to 0.05 if not given in a problem)
        * Compute the test statistic $z_0$ i.e. the z score for the sample mean or proportion
        * Compute the probability of having your test statistic ($Pr(z>z_0)$, $Pr(z<z_0)$, or $2Pr(z>|z_0|)$ depending
        on the type of test.
        """)

    st.subheader("Method 3: Confidence Interval Approach (Only for 2 Tail)")

    st.markdown(r"""
        * Use the data you have to compute a confidence interval
        * If the null hypothesis suggests the mean or proportion is outside your confidence interval, then
        reject the null hypothesis
        """)

    st.markdown("I'd like to point out that you could use a confidence interval for 1 tail tests BUT we won't be "
                "covering it in our course as we've only looked at symmetrical confidence intervals.")