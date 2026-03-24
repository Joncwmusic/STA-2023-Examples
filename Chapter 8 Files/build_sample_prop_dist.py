import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
import math


def build_sample_prop_page():

    population_proportion_data = [random.choice([1, 1, 0, 0, 0]) for i in range(1000)]

    prop_sample_dict = {}
    for sample_count in range(1, 100):
        sample_list = []
        for i in range(42):
            sample_list.append(random.choice(population_proportion_data))
        prop_sample_dict["sample_number_" + str(sample_count)] = sample_list

    sample_prop_mean_dict = {i:[sum(prop_sample_dict[i])/len(prop_sample_dict[i])] for i in prop_sample_dict.keys()}

    sample_prop_mean_df = pd.DataFrame(sample_prop_mean_dict)
    sample_prop_df = pd.DataFrame(prop_sample_dict)
    fig_sample_prop = px.histogram(sample_prop_mean_dict)

    st.header("Distribution of a Sample Proportion")

    st.dataframe(sample_prop_df)
    st.dataframe(sample_prop_mean_df)
    st.plotly_chart(fig_sample_prop)

    st.subheader("Can we assume normality?")
    st.markdown("$np(1-p) \geq 10$")

    st.subheader("Mean and Standard Deviation of the sample proportion")

    st.markdown(r"$\mu_{\hat{p}} = p$")
    st.markdown(r"$\sigma_{\hat{p}} = \sqrt{\dfrac{p(1-p)}{n}}$")

    st.subheader("Comparing to the Sample Mean")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(r"Sample Mean $\mu$ and $\sigma$")
        st.markdown(r"$\mu_{\bar{x}} = \mu$")
        st.markdown(r"$\sigma_{\bar{x}} = \dfrac{\sigma}{\sqrt{n}}$")
    with col2:
        st.subheader(r"Sample Prop. $\mu$ and $\sigma$")
        st.markdown(r"$\mu_{\hat{p}} = p$")
        st.markdown(r"$\sigma_{\hat{p}} = \sqrt{\dfrac{p(1-p)}{n}}$")
