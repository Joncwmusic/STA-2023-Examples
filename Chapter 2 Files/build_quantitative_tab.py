import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly"
import math
import datetime as dt


# Qualitative Data
def build_quantitative_tab():
    continuous_data_list = [random.gauss(mu=70, sigma=18) for i in range(200)]
    messy_data_list = [round(random.gauss(mu = 10, sigma=2.75)) for i in range(200)]
    messy_data_list_only_pos = [max(x, 0) for x in messy_data_list]
    discrete_data_list = [min(x,20) for x in messy_data_list_only_pos]

    time_series_dict = {dt.date(2025, 1, 1) + dt.timedelta(days=i): math.sin((i-90)*math.pi/365) for i in range(365)}

    st.title("Chapter 2: Organizing and Summarizing Data")
    st.header("Part 2: Quantitative Data Visualizations")
    st.text("When presented with quantitative data, you can still get frequency tables for discrete values. "
            "it gets more complicated when you have continuous variables since you may have to bucket "
            "that data in order to get simple and actionable information without staring at 1000 bars")

    st.text("*Data is generated randomly and not indicative of an actual sample or population")

    # DISCRETE QUANTITATIVE DATA

    st.header("Raw Data (Discrete Values)")
    st.text("The following data is a list of 200 scores scores between 0 and 20. We can construct "
            "a frequency table and bar chart much like with our categorical data. ")
    st.dataframe(discrete_data_list)

    st.header("Frequency Table and Relative Frequency for Discrete Data")
    st.text("Below is the frequency and relative frequency. Note how I added a column for cumulative frequency. "
              "The cumulative frequency is the sum of the relative frequency up to this value. "
              "The very last value should always come out to 1 as that means you are summing ALL observations.")
    count_dict = {i: discrete_data_list.count(i) for i in range(21)}
    freq_frame = pd.DataFrame.from_dict(count_dict, orient='index', columns=['Frequency'])
    freq_frame['Relative Frequency'] = freq_frame['Frequency']/200
    freq_frame['Cumulative Frequency'] = freq_frame['Relative Frequency'].cumsum()
    st.dataframe(freq_frame)

    # DISCRETE DATA VISUALIZATIONS

    st.header("Visualizing Discrete Data")
    st.text("Below is a histogram with our discrete data. This shows the number of scores in each 'score bucket' "
            "much like with the categorical data in the first tab. We'll see how this differs from continuous data. "
            "as we continue.")
    hist_chart_fig_discrete = px.histogram(freq_frame, x=freq_frame.index, y='Frequency', nbins=21)
    st.plotly_chart(hist_chart_fig_discrete)

    # CONTINUOUS QUANTITATIVE DATA

    st.header("Raw Data (Continuous Values)")
    st.text("Below is our data with continuous data. We can still get an idea of frequency but we have to do some "
            "extra steps to simplify these values.")
    st.dataframe(continuous_data_list)

    st.header("Classes and Histograms with Continuous Data")
    st.text("Classes are evenly sized 'buckets' to organize data into. In this case we may want to define a class size "
            "of let's say 10 buckets. There is a simple formula for getting our class sizes.")
    st.latex(r'Class Size \approx \dfrac{Max Observation - Min Observation}{Number Of Classes}')
    st.text("Note that sometimes if your data is particularly skewed you may opt to keep the first "
            "and last buckets open.")

    number_of_classes = 10
    class_size = (max(continuous_data_list) - min(continuous_data_list))/number_of_classes
    new_class_size = math.ceil(class_size)

    hist_chart_fig_continuous = px.histogram(continuous_data_list, nbins = new_class_size)

    st.plotly_chart(hist_chart_fig_continuous)

    st.header("Time Series Data")
    st.text("Often times, you'll see data monitored over time ")



# continuous_data_list = [random.gauss(mu=70, sigma=8) for i in range(200)]
# discrete_data_list = [random.binomialvariate() for i in range(200)]
# print(continuous_data_list)
# print(discrete_data_list)