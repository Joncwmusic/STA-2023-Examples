import streamlit as st
import pandas as pd


def get_arithmetic_mean(numlist):
    return sum(numlist)/len(numlist)


def get_median(numlist):
    if len(numlist)%2 == 0:
        return 0.5*(numlist[(len(numlist)/2) - 1]+numlist[len(numlist)/2])
    else:
        return numlist[(len(numlist)+1)/2]


def build_central_tendency_tab(user_string):
    example_data = [4, 7, 10, 12, 15, 17, 19, 20, 21, 25]

    st.title("Measures of Centeral Tendency")
    st.header("Arithmetic Mean (Average)")
    st.text("The arithmetic mean is a simple sum of all the data points after which you just have to divide that "
            "sum by the number of data points to get your final number. Regardless of if you're measuring the mean "
            "of a sample or a population, it is calculated the same way.")


    st.header("Median")

    st.header("Mode")

    st.header("Now You Try")
    st.text("input your dataset here (make sure to separate each number with a comma:")
    user_string = st.text_input()
    user_data_list = list(map(int, user_string.split(',')))

    st.button("Reset", type="primary")
    if st.button("Compute Mean"):
        user_mean = get_arithmetic_mean(user_data_list)
        st.write(str(user_mean))
    else:
        st.write("Goodbye")

    if st.button("Aloha", type="tertiary"):
        st.write("Ciao")


user_string = "3, 5, 6, 10, 12, 16, 18"