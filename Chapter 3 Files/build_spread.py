import streamlit as st
import pandas as pd
import plotly.express as px
import build_central_tendency as bct

def get_range(numlist):
    return max(numlist) - min(numlist)
def get_variance(numlist):
    sum_error = 0
    for item in numlist:
        sum_error = sum_error + (item - bct.get_arithmetic_mean(numlist))**2


def get_standard_deviation():
    return None


def build_spread_tab():
    example_data = [4, 7, 10, 12, 12, 12, 15, 16, 17, 17, 18, 19, 20, 21, 25]

    st.title("Measures of Spread")
    st.header("Arithmetic Mean (Average)")
    st.text("The arithmetic mean is a simple sum of all the data points after which you just have to divide that "
            "sum by the number of data points to get your final number. Regardless of if you're measuring the mean "
            "of a sample or a population, it is calculated the same way.")

    st.header("Median")
    st.text("To find the median of a data set you just need to first SORT the data and then pick the middle number. "
            "If the number of items in the data set is even then take the average of the middle two numbers. ")

    st.header("Mode")
    st.text("The mode just refers to the most often observation. If there is no duplicate data points, we say the data "
            "set has no mode.")

    st.header("Example")
    st.text("So let's look at a specific data set.")
    st.dataframe(example_data)

    numerator_list = []
    denominator = str(len(example_data))
    for idx, num in enumerate(example_data):
        if idx < len(example_data) - 1:
            numerator_list.append(str(num))
            numerator_list.append('+')
        else:
            numerator_list.append(str(num))
    mean_latex_string = r"\dfrac{" + "".join(numerator_list) + "}{" + denominator + "} = " + str(get_arithmetic_mean(example_data))

    st.text("Mean: ")
    st.latex(mean_latex_string)

    st.text("Median: " + str(bct.get_median(example_data)))

    st.text("Mode: " + str(bct.get_mode(example_data)))

    st.header("Now You Try")
    st.text("input your dataset here (make sure to separate each number with a comma:")
    user_data_string = st.text_input("Your Data", "Input your number list here")

    try:
        user_data_list = bct.string_to_list(user_data_string)

        user_numerator_list = []
        user_denominator = str(len(user_data_list))
        for idx, num in enumerate(user_data_list):
            if idx < len(user_data_list) - 1:
                user_numerator_list.append(str(num))
                user_numerator_list.append('+')
            else:
                user_numerator_list.append(str(num))
        user_mean_latex_string = r"\dfrac{" + "".join(user_numerator_list) + "}{" + user_denominator + "} = " + str(
            bct.get_arithmetic_mean(user_data_list))

        st.text("Mean: ")
        st.latex(user_mean_latex_string)

        st.text("Median: " + str(bct.get_median(user_data_list)))

        st.text("Mode: " + str(bct.get_mode(user_data_list)))
    except:
        st.text("It seems the number list you've input is invalid. Please input a comma separated number list.")
