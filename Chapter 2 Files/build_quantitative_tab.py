import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly"



# Qualitative Data
def build_quantitative_tab():
    continuous_data_list = [random.gauss(mu=70, sigma=8) for i in range(200)]
    discrete_data_list = [random.binomialvariate(n=1, p=0.5) for i in range(200)]

    print(continuous_data_list)
    print(discrete_data_list)


    st.title("Chapter 2: Organizing and Summarizing Data")
    st.header("Quantitative Data Visualizations")
    st.text("When presented with quantitative data, you can still get frequency tables for discrete values. "
            "it gets more complicated when you have continuous variables since you may have to bucket "
            "that data in order to get simple and actionable information without staring at 1000 bars")

    st.text("*Data is generated randomly and not indicative of an actual sample or population")

    # DISCRETE QUANTITATIVE DATA
    st.header("Raw Data (Discrete Values)")
    st.text("The following data is a list of individuals each with a political party affiliation.")
    st.dataframe(discrete_data_list)



    st.dataframe(continuous_data_list)