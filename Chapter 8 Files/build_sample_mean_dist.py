import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
import math


def normpdf(mu, sigma, x):
    part_1 = 1/(sigma*math.sqrt(2*math.pi))
    part_2 = math.exp(-((x-mu)**2)/(2*sigma**2))
    return part_1 * part_2


def build_sample_mean_page():
    # Building out the data and samples
    normal_dist = [round(random.gauss(mu = 100, sigma=15),2) for i in range(1000)]
    nonnormal_dist = [random.choice([round(random.gauss(mu = 155, sigma = 6), 2),
                      round(random.gauss(mu=175, sigma=7), 2)]) for i in range(1000)]

    x_values = [40 + i/5 for i in range(600)]
    theory_norm_curve = [2000*normpdf(mu=100, sigma=15, x=i) for i in x_values]

    normal_samples_dict = {}
    for sample_count in range(1, 101):
        sample_list = []
        for i in range(10):
            sample_list.append(random.choice(normal_dist))
        normal_samples_dict["sample_number_" + str(sample_count)] = sample_list

    sample_mean_dict = {i:[sum(normal_samples_dict[i])/len(normal_samples_dict[i])] for i in normal_samples_dict.keys()}

    nonnormal_samples_dict = {}
    for sample_count in range(1, 101):
        sample_list = []
        for i in range(10):
            sample_list.append(random.choice(nonnormal_dist))
        nonnormal_samples_dict["sample_number_" + str(sample_count)] = sample_list

    nonnorm_sample_mean_dict = {i:[sum(nonnormal_samples_dict[i])/len(nonnormal_samples_dict[i])]
                           for i in nonnormal_samples_dict}

    normal_pop_df = pd.DataFrame({"IQ": normal_dist})
    nonnormal_pop_df = pd.DataFrame({"Height(cm)":nonnormal_dist})
    theory_norm_df = pd.DataFrame({"x": x_values, "normal(x)": theory_norm_curve})

    samples_df = pd.DataFrame(normal_samples_dict)
    sample_mean_df = pd.DataFrame(sample_mean_dict)
    nonnorm_sample_df = pd.DataFrame(nonnormal_samples_dict)
    nonnorm_sample_mean_df = pd.DataFrame(nonnorm_sample_mean_dict)

    # building out the graphs and visuals
    fig_normal_pop = px.histogram(normal_pop_df)
    fig_theory_norm = px.line(data_frame=theory_norm_df, x="x", y="normal(x)")
    fig_theory_norm.add_traces(
        fig_normal_pop.data[0]
    )

    fig_nonnormal_pop = px.histogram(nonnormal_pop_df)

    fig_sample_mean = px.histogram(sample_mean_dict)

    fig_nonnormal_sample_mean = px.histogram(nonnorm_sample_mean_dict)

    # building and formatting the page
    st.header("Sampling from a Population")
    st.markdown("")

    col1, col2 = st.columns(2)
    with col1:
        st.dataframe(normal_pop_df)
    with col2:
        st.plotly_chart(fig_theory_norm)

    st.header("Distribution of a Sample Statistic")

    st.subheader("Distribution of the Sample Mean")

    st.dataframe(samples_df)
    st.dataframe(sample_mean_df)

    st.plotly_chart(fig_sample_mean)

    st.header("What if the Underlying Distribution is Not Normal?")
    st.plotly_chart(fig_nonnormal_pop)
    st.dataframe(nonnorm_sample_df)
    st.dataframe(nonnorm_sample_mean_df)
    st.plotly_chart(fig_nonnormal_sample_mean)

    st.subheader("Central Limit Theorem")
    st.markdown("As it turns out, as your sample size becomes bigger, the distribution of the sample mean for your "
                "population will approach normality over time.")