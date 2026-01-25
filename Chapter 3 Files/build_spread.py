import math

import streamlit as st
import pandas as pd
import plotly.express as px
import build_central_tendency as bct


def get_range(numlist):
    return max(numlist) - min(numlist)


def get_variance(numlist):
    if len(numlist) == 0:
        st.write("The list provided is not valid for calculating the variance or standard deviation")
        return None
    sum_error = 0
    for item in numlist:
        sum_error = sum_error + (item - bct.get_arithmetic_mean(numlist))**2
    return sum_error/len(numlist)


def get_standard_deviation(numlist):
    var = get_variance(numlist)
    return math.sqrt(var)


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

    st.text("0")


    example_series = pd.Series(example_data, name = "data")
    example_mean_series = pd.Series([example_series.mean() for i in example_data], name='mean')
    example_diff_series = pd.Series([x - example_series.mean() for x in example_data], name='differences')
    example_square_series = pd.Series([(x - example_series.mean())**2 for x in example_data])
    example_df= pd.DataFrame({'data':example_series, 'mean':example_mean_series, 'differences':example_diff_series
                             , 'square_diff':example_square_series})

    st.dataframe(example_df)

    st.write(example_square_series.sum()/len(example_data))

    st.header("Variance and Standard Deviation")
    st.text("The mode just refers to the most often observation. If there is no duplicate data points, we say the data "
            "set has no mode.")

    # st.header("Example")
    # st.text("So let's look at a specific data set.")
    # st.dataframe(example_data)
    #
    # numerator_list = []
    # denominator = str(len(example_data))
    # for idx, num in enumerate(example_data):
    #     if idx < len(example_data) - 1:
    #         numerator_list.append(str(num))
    #         numerator_list.append('+')
    #     else:
    #         numerator_list.append(str(num))
    # mean_latex_string = r"\dfrac{" + "".join(numerator_list) + "}{" + denominator + "} = " + str(bct.get_arithmetic_mean(example_data))
    #
    #
    # st.header("Now You Try")
    # st.text("input your dataset here (make sure to separate each number with a comma:")
    # user_data_string = st.text_input("Your Data", "Input your number list here")
    #
    # try:
    #     user_data_list = bct.string_to_list(user_data_string)
    #
    #     user_numerator_list = []
    #     user_denominator = str(len(user_data_list))
    #     for idx, num in enumerate(user_data_list):
    #         if idx < len(user_data_list) - 1:
    #             user_numerator_list.append(str(num))
    #             user_numerator_list.append('+')
    #         else:
    #             user_numerator_list.append(str(num))
    #     user_mean_latex_string = r"\dfrac{" + "".join(user_numerator_list) + "}{" + user_denominator + "} = " + str(
    #         bct.get_arithmetic_mean(user_data_list))
    #
    #     st.text("Mean: ")
    #     st.latex(user_mean_latex_string)
    #
    #     st.text("Median: " + str(bct.get_median(user_data_list)))
    #
    #     st.text("Mode: " + str(bct.get_mode(user_data_list)))
    # except:
    #     st.text("It seems the number list you've input is invalid. Please input a comma separated number list.")
