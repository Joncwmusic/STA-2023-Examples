import streamlit as st
import pandas as pd


def get_average(numlist):
    return sum(numlist)/len(numlist)


def get_median(numlist):
    if len(numlist)%2 == 0:
        return 0.5*(numlist[(len(numlist)/2) - 1]+numlist[len(numlist)/2])
    else:
        return numlist[(len(numlist)+1)/2]


def build_central_tendency_tab(user_string):
    st.title("Measures of Centeral Tendency")
    st.header("Mean (Average)")
    st.text("")

    st.header("Median")

    st.header("Mode")

    st.header("Now You Try")
    st.text("input your dataset here (make sure to separate each number with a comma:")
    st.text_input()

    return None

user_string = "3, 5, 6, 10, 12, 16, 18"