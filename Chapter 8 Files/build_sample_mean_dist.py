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

    x_vals = [i*0.02 for i in range(-200, 200)]
    generic_normal = [normpdf(0, 1,i) for i in x_vals]
    sample_mean_normal_n36 = [normpdf(0, 1/6,i) for i in x_vals]
    sample_mean_normal_n100 = [normpdf(0, 1/10,i) for i in x_vals]

    generic_norm_df = pd.DataFrame({"x_vals": x_vals, "y_vals":generic_normal})
    sample_norm_df_n36 = pd.DataFrame({"x_vals": x_vals, "y_vals": sample_mean_normal_n36})
    sample_norm_df_n100 = pd.DataFrame({"x_vals": x_vals, "y_vals": sample_mean_normal_n100})

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
    fig_theory_norm.add_traces(fig_normal_pop.data[0])

    fig_nonnormal_pop = px.histogram(nonnormal_pop_df)

    fig_sample_mean = px.histogram(sample_mean_dict)

    fig_nonnormal_sample_mean = px.histogram(nonnorm_sample_mean_dict)

    fig_generic_norm = px.line(data_frame=generic_norm_df, x="x_vals", y="y_vals", title="Standard Normal (n=1)")
    fig_sample_norm_n36 = px.line(data_frame=sample_norm_df_n36, x="x_vals", y="y_vals", title="n = 36")
    fig_sample_norm_n100 = px.line(data_frame=sample_norm_df_n100, x="x_vals", y="y_vals", title="n = 100")

    # building and formatting the page
    st.header("Sampling from a Population")
    st.markdown("So let's suppose we're looking at some population data. There's just one problem. It's really "
                "expensive to get summary statistics of a population. Especially when those populations may have "
                "hundreds, if not thousands, of subjects to observe and analyze. What a nightmare. This takes us "
                "right back to the beginning of the course: sampling. But of course, our samples could be wrong. It "
                "wouldn't exactly be ethical or practical to make massive decisions on behalf of an organization "
                "without measurably quantifying the potential error.")

    col1, col2 = st.columns(2)
    with col1:
        st.dataframe(normal_pop_df)
    with col2:
        st.plotly_chart(fig_theory_norm)

    st.header("Distribution of a Sample Statistic")
    st.markdown("Now let's suppose we're trying to estimate the mean of the population above. We might want to gather "
                "some samples. Not just one sample because that's be too unreliable. What if instead we gathered like "
                "100 samples from the population and then marked their means?")

    st.subheader("Distribution of the Sample Mean")

    st.dataframe(samples_df)
    st.dataframe(sample_mean_df)

    st.markdown("Okay that was a lot of work but let's collect all those means and put it into a histogram and see "
                "what exactly those means look like.")

    st.plotly_chart(fig_sample_mean)

    st.markdown("Wowzers! It looks like the means from the sample form a rough bell shape. Neato. As it turns out, the "
                "distribution of the sample mean being vaguely normal is no coincidence. Spoiler alert, the underlying "
                "data doesn't have to be normal to see this.")

    st.header("What if the Underlying Distribution is Not Normal?")

    st.markdown("This time, I have a bunch of non normal data. If anything it kind of looks like 2 bell curves smashed "
                "together into a big distribution. Because that's what I did. So what should the distribution of the "
                "mean actually look like? Well let's repeat our sampling methodology from above and look at the "
                "distribution of the sample mean.")

    st.plotly_chart(fig_nonnormal_pop)

    st.subheader("Non normal samples and averages")
    st.dataframe(nonnorm_sample_df)
    st.dataframe(nonnorm_sample_mean_df)

    st.plotly_chart(fig_nonnormal_sample_mean)
    st.markdown("Would you look at that? It doesn't have two bump like the original data. If anything it looks like "
                "just another bell curve. That's kind of surprising result and lends itself to one of the most "
                "important theorems in statistics.")

    st.subheader("Central Limit Theorem")


    col1CLT, col2CLT = st.columns(2)
    with col1CLT:
        st.markdown(" ")
        st.markdown(" ")
        st.markdown("As it turns out, as your sample size becomes bigger, the distribution of the sample mean for your "
                    "population will approach normality over time. And the mean and standard deviation of the sample mean "
                    "can be calculated by the following:")

        st.markdown(r"$\mu_{\bar{x}} = \mu$")
        st.markdown(r"$\sigma_{\bar{x}} = \dfrac{\sigma}{\sqrt{n}}$")

        st.markdown("It should be noted that as n gets larger the standard deviation of the distribution of the sample "
                    "mean should be getting smaller implying a more concentrated distribution of the sample mean. Each "
                    "of the charts to the right is a standard normal distribution with a standard deviation reflecting "
                    "the sample size.")
    with col2CLT:
        st.plotly_chart(figure_or_data=fig_generic_norm, height=300)
        st.plotly_chart(figure_or_data=fig_sample_norm_n36, height=300)
        st.plotly_chart(figure_or_data=fig_sample_norm_n100, height=300)

