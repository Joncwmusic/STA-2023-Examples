import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly"



# Qualitative Data
def build_error_tab():
    continuous_data_list = [random.gauss(mu=70, sigma=8) for i in range(200)]
    messy_data_list = [round(random.gauss(mu = 10, sigma=1.75)) for i in range(200)]
    discrete_data_list = [max(x, 0) for x in messy_data_list if x <= 0]

    print(continuous_data_list)
    print(discrete_data_list)


    st.title("Chapter 2: Organizing and Summarizing Data")
    st.header("Part 3: Bias in Visualizations")
    st.text("On occassion, or rather, all the time. People are using data to push some kind of narrative or agenda. "
            "You as the interpreter of said data are responsible for ")

    st.text("*Data is generated randomly and not indicative of an actual sample or population")

    # DISCRETE QUANTITATIVE DATA
    st.header("Raw Data (Discrete Values)")
    st.text("The following data is a list of individuals each with a political party affiliation.")
    st.dataframe(discrete_data_list)



    st.dataframe(continuous_data_list)


# continuous_data_list = [random.gauss(mu=70, sigma=8) for i in range(200)]
# discrete_data_list = [random.binomialvariate() for i in range(200)]
# print(continuous_data_list)
# print(discrete_data_list)