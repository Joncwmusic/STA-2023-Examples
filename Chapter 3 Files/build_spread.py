import math

import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px
import build_central_tendency as bct

import util_functions as uf

def build_spread_tab():
    example_data = [4, 7, 10, 12, 12, 12, 15, 16, 17, 17, 18, 19, 20, 21, 25]

    st.title("Measures of Spread")

    st.header("Getting to know our data")
    st.text("Let's take a quick look at our data which is the same data as the other set. Wowzers.")
    st.dataframe(example_data)

    st.header("Range")
    st.text("One of the simplest ways to figure out how much spread exists in a set of data is to measure the range "
            "which is as simple as taking the max value and the min value and subtracting them. The problem with this"
            "particular measure of spead is that it is very susceptible to changes from outliers "
            "and so we should probably consider a more robust way to measure spread.")

    st.header("Incorporating the Mean")
    st.text("So a natural question is ask is probably 'What else can we do to incorporate all of our data?' "
            "Maybe if we compare each datapoint to the mean we can get another way to see the spread of our data."
            "and then we can add add it all up and get...")

    example_series = pd.Series(example_data, name="data")
    example_mean_series = pd.Series([example_series.mean() for i in example_data], name='mean')
    example_diff_series = pd.Series([x - example_series.mean() for x in example_data], name='differences')
    example_square_series = pd.Series([(x - example_series.mean()) ** 2 for x in example_data])

    example_df = pd.DataFrame(
        {'data (x_i)': example_data, 'mean (mu)': example_mean_series, 'differences (x_i - mu)': example_diff_series})
    example_total_df = pd.DataFrame({'data (x_i)': [example_series.sum()], 'mean (mu)': [example_mean_series.sum()]
                                        , 'differences (x_i - mu)': [example_diff_series.sum()]})

    st.dataframe(example_df)
    st.dataframe(example_total_df)

    st.text("0... and as it turns out if we just sum differences we will always get 0 no matter what. So what is one "
            "to do to keep the deviations without them cancelling? The answer is to square all the values. And "
            "when we add those values and divide by the number of data points we get something called the Variance "
            "which is denoted with a sigma squared. If we take the square root of that value we get the standard "
            "deviation.")

    st.header("Calculating Standard Deviation By Hand.")
    example_df_with_square = pd.DataFrame(
        {'data (x_i)': example_data, 'mean (mu)': example_mean_series, 'differences (x_i - mu)': example_diff_series
            , 'square_diff ((x_i-mu)^2)': example_square_series})
    example_total_df_with_square = pd.DataFrame({'data (x_i)': [example_series.sum()], 'mean (mu)': [example_mean_series.sum()]
                                        , 'differences (x_i - mu)': [example_diff_series.sum()],
                                     'square_diff ((x_i-mu)^2)': [example_square_series.sum()]})

    st.dataframe(example_df_with_square)
    st.dataframe(example_total_df_with_square)

    st.latex(r'''\sigma = \sqrt{\dfrac{\sum (x_i - \mu ) ^2}{N}} = \sqrt{\dfrac{432}{15}} \approx 5.55''')
    st.latex(r'''\sigma = \sqrt{\dfrac{\sum (x_i - \mu ) ^2}{N-1}} = \sqrt{\dfrac{432}{15-1}} \approx 5.76''')


    st.header("Variance vs. Standard Deviation")
    st.text("The difference between variance and standard deviation is literally a square. At the end of the "
            "calculation, if we remove the step of taking the square root, we have the variance which is denoted "
            "with a sigma squared (or s squared for sample variance).")

    st.header("Grouped Data")

    st.text("When dealing with grouped data we just apply the following formula:")

    st.latex(r"""\sigma = \sqrt{\dfrac{\sum (x_i - \mu )^2 f_i}{\sum f_i}}""")

    st.text("Each column represents a different step including finding the mean, finding the differences from the mean,"
            " squaring each difference and then multiplying the frequencies before adding them up and ultimately "
            "dividing by the sum of frequencies and taking the square root.")

    grouped_data_sd = {"class": ["0-49.99", "50-99.99", "100-149.99", "150-199.99", "200-249.99", "250-299.99"]
        , "midpoint": [25, 75, 125, 175, 225, 275], "frequency": [5, 9, 12, 15, 5, 2]
        , "mean":[137.5, 137.5, 137.5, 137.5, 137.5, 137.5]}

    grouped_total_sd = {"class": ["Total"], "midpoint": [np.nan], "frequency": [48]
        , "mean":[137.5], "x_i-mu":["na"] ,"(x_i-mu)^2":["na"], "(x_i-mu)^2)*f_i":[197500]}

    grouped_total_sd_df = pd.DataFrame(grouped_total_sd)

    grouped_data_sd_df = pd.DataFrame(grouped_data_sd)
    grouped_data_sd_df["x_i-mu"] = grouped_data_sd_df["midpoint"] - grouped_data_sd_df["mean"]
    grouped_data_sd_df["(x_i-mu)^2"] = grouped_data_sd_df["x_i-mu"]**2
    grouped_data_sd_df["(x_i-mu)^2)*f_i"] = grouped_data_sd_df["(x_i-mu)^2"] * grouped_data_sd_df["frequency"]

    st.dataframe(grouped_data_sd_df)
    st.dataframe(grouped_total_sd_df)

    st.markdown(r"""
    
    $$\sigma = \sqrt{\dfrac{\sum (x_i - \mu )^2 f_i}{\sum f_i}}$$
    
    $$\sqrt{\dfrac{(12656.25)(5)+(3906.25)(9)+(156.25)(12)+(1406.25)(15)+(7656.25)(5)+(18906.25)(2)}{5+9+12+15+5+2}}$$
    
    $$\sqrt{\dfrac{197500}{48}} \approx \sqrt{4114} \approx 64.1$$""")

    st.text("Keep in mind the variance is that 4114 figure under the square root.")

    st.header("Formulas")
    st.markdown(r"""

    Population Mean and Standard Deviation:

    $$\mu = \dfrac{\sum x_i}{N} \hspace{50pt} \sigma = \sqrt{\dfrac{\sum (x_i - \mu ) ^2}{N}}$$

    Sample Mean and Standard Deviation:

    $$\bar{x} = \dfrac{\sum x_i}{N} \hspace{50pt} s = \sqrt{\dfrac{\sum (x_i - \bar{x}) ^2}{N -1}}$$

    Grouped Data Population Mean and Standard Deviation:

    $$ \mu = \dfrac{\sum x_i f_i}{\sum f_i} \hspace{50pt} \sigma = \sqrt{\dfrac{\sum (x_i - \mu ) ^2f_i}{\sum f_i}}$$

    Grouped Data Sample Mean and Standard Deviation:

    $$ \bar{x} = \dfrac{\sum x_i f_i}{\sum f_i} \hspace{50pt} s = \sqrt{\dfrac{\sum (x_i - \bar{x} ) ^2f_i}{(\sum f_i) -1}}$$

    Weighted Mean:

    $$\dfrac{\sum x_i w_i}{\sum w_i}$$

    z-score for Data from Population and Sample:

    $$z=\dfrac{x-\mu}{\sigma} \hspace{50pt} z=\dfrac{x-\bar{x}}{s}$$""")
