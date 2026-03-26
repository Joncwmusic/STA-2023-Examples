import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
import math


def build_sample_prop_page():

    population_proportion_data = [random.choice([1, 1, 0, 0, 0]) for i in range(10000)]

    pop_prop_ones = [i for i in population_proportion_data if i == 1]
    pop_prop_zeros = [i for i in population_proportion_data if i == 0]

    pop_prop_data_df = pd.DataFrame({"Response": ["Yes", "No"],"Count": [len(pop_prop_ones), len(pop_prop_zeros)]})

    prop_sample_dict = {}
    for sample_count in range(1, 100):
        sample_list = []
        for i in range(42):
            sample_list.append(random.choice(population_proportion_data))
        prop_sample_dict["sample_number_" + str(sample_count)] = sample_list

    sample_prop_mean_dict = {i: [sum(prop_sample_dict[i])/len(prop_sample_dict[i])] for i in prop_sample_dict.keys()}

    sample_prop_mean_df = pd.DataFrame(sample_prop_mean_dict)
    sample_prop_df = pd.DataFrame(prop_sample_dict)
    fig_sample_prop = px.histogram(sample_prop_mean_dict)
    fig_pop_prop_data = px.bar(pop_prop_data_df, x="Response", y="Count")

    st.header("Distribution of a Sample Proportion")

    st.markdown("So now let's consider instead of measurements like height or test scores we get a binary Yes or No "
                "from every person we observe in a study.")

    col1prop, col2prop = st.columns(2)
    with col1prop:
        st.dataframe(pop_prop_data_df)
    with col2prop:
        st.plotly_chart(fig_pop_prop_data)

    st.markdown("Just like the mean, we can sample a random group of people from this particular population and collect"
                r" their Yes's and No's. The sample will have an estimated proportion noted by a $\hat{p}$")

    st.subheader("Sampling the 1s and 0s from the total population")
    st.dataframe(sample_prop_df)
    st.dataframe(sample_prop_mean_df)
    st.plotly_chart(fig_sample_prop)

    st.markdown("So it looks like the proportion averages somewhere around 0.4 and appears bell shaped...")

    st.subheader("Can we just assume normality?")

    st.markdown("A good question one might ask is if the distribution of the sample proportion is in any way shape or "
                "form considered normal just like the mean. As it turns out... yes. But under the following condition:")
    st.markdown("$np(1-p) \geq 10$")
    st.markdown("So as long as the product of the proportion, its compliment, and the sample size is greater than 10 "
                "we can more or less assume the sample proportions will be normally distributed.")

    st.subheader("Mean and Standard Deviation of the sample proportion")
    st.markdown("The next natural question is what are the mean and standard deviation of the distribution for the "
                "sample proportion? Turns out the formulas are:")
    st.markdown(r"$\mu_{\hat{p}} = p$")
    st.markdown(r"$\sigma_{\hat{p}} = \sqrt{\dfrac{p(1-p)}{n}}$")

    st.subheader("Comparing to the Sample Mean")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(r"Sample Mean $\mu$ and $\sigma$")
        st.markdown(r"$\mu_{\bar{x}} = \mu$")
        st.markdown(r"$\sigma_{\bar{x}} = \dfrac{\sigma}{\sqrt{n}}$")
        st.markdown(r"Normal enough if $n>30$")
    with col2:
        st.subheader(r"Sample Prop. $\mu$ and $\sigma$")
        st.markdown(r"$\mu_{\hat{p}} = p$")
        st.markdown(r"$\sigma_{\hat{p}} = \sqrt{\dfrac{p(1-p)}{n}}$")
        st.markdown(r"Normal enough if $np(1-p) \geq 10$")