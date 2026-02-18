import streamlit as st
import pandas as pd
import numpy as np
import math
import random
import plotly.express as px


def build_residual_analysis():

    x_values = [x for x in range(-50,150)]
    y1_values = [x/3 + random.gauss(mu=0, sigma=10) for x in x_values]
    y2_values = [x/3 + random.gauss(mu=0, sigma=25) for x in x_values]

    example_df_1 = pd.DataFrame({"Inputs": x_values, "Outputs": y1_values})
    example_df_2 = pd.DataFrame({"Inputs": x_values, "Outputs": y2_values})

    y1_plot = px.scatter(data_frame=example_df_1, x="Inputs", y="Outputs", trendline="ols", range_y=[-60, 120])
    y2_plot = px.scatter(data_frame=example_df_2, x="Inputs", y="Outputs", trendline="ols", range_y=[-60, 120])

    x_bar = example_df_1["Inputs"].mean()
    y1_bar = example_df_1["Outputs"].mean()
    y2_bar = example_df_2["Outputs"].mean()
    s_x = example_df_1["Inputs"].std()
    s_y1 = example_df_1["Outputs"].std()
    s_y2 = example_df_2["Outputs"].std()
    n = len(x_values)

    presum1 = ((example_df_1["Inputs"] - x_bar)/s_x)*((example_df_1["Outputs"]-y1_bar)/s_y1)
    presum2 = ((example_df_2["Inputs"] - x_bar)/s_x)*((example_df_2["Outputs"]-y2_bar)/s_y2)

    corr_coeff_y1 = presum1.sum()/(n-1)
    corr_coeff_y2 = presum2.sum()/(n-1)

    y1_slope = round(corr_coeff_y1*(s_y1/s_x), 3)
    y2_slope = round(corr_coeff_y2*(s_y2/s_x), 3)
    y1_int = round(y1_bar - y1_slope*x_bar, 3)
    y2_int = round(y2_bar - y2_slope*x_bar, 3)

    st.header("Getting to know the Data")

    st.markdown("Below are 2 different data sets with very similar regression lines, however, they have very different "
                "spreads which mean they have different correlation strength which we'll talk about a little later. "
                "For now, I'll give you their best fit regression lines.")

    col1, col2 = st.columns(2)  # Creates two columns of equal width

    # 3. Generate and display the first plot in the first column
    with col1:
        st.markdown(r"$$ \hat{y} = " + str(y1_slope) + r"x + " + str(y1_int) + r"$$")
        st.markdown(r"$$r = " + str(round(corr_coeff_y1, 4)) + r"$$")
        st.markdown(r"$$R^2 = " + str(round(corr_coeff_y1**2, 4)) + r"$$")
        st.plotly_chart(y1_plot)
    with col2:
        st.markdown(r"$$ \hat{y} = " + str(y2_slope) + r"x + " + str(y2_int) + r"$$")
        st.markdown(r"$$r = " + str(round(corr_coeff_y2, 4)) + r"$$")
        st.markdown(r"$$R^2 = " + str(round(corr_coeff_y2**2, 4)) + r"$$")
        st.plotly_chart(y2_plot)

    st.header("Plotting the Residuals")

    st.markdown("One way to visualize the strength of a correlation is to plot the residuals which are just the "
                "differences between the actual values from the data and the predicted values from the line, namely")
    st.markdown("$$Residual = \hat{y_i} - y_i$$")

    example_df_1["Predicted"] = y1_slope*example_df_1["Inputs"] + y1_int
    example_df_2["Predicted"] = y2_slope*example_df_2["Inputs"] + y2_int

    example_df_1["Residual"] = example_df_1["Predicted"] - example_df_1["Outputs"]
    example_df_2["Residual"] = example_df_2["Predicted"] - example_df_2["Outputs"]

    y1_resid_plot = px.scatter(data_frame=example_df_1, x="Inputs", y="Residual", trendline="ols", range_y=[-80, 80])
    y2_resid_plot = px.scatter(data_frame=example_df_2, x="Inputs", y="Residual", trendline="ols", range_y=[-80, 80])
    y1_resid_box_whisker = px.box(data_frame=example_df_1, y="Residual", range_y=[-80,80])
    y2_resid_box_whisker = px.box(data_frame=example_df_2, y="Residual", range_y=[-80,80])


    col1, col2 = st.columns(2)  # Creates two columns of equal width
    # 3. Generate and display the first plot in the first column
    with col1:
        box_col, scatter_col = st.columns(2)
        with box_col:
            st.plotly_chart(y1_resid_box_whisker)
        with scatter_col:
            st.plotly_chart(y1_resid_plot)
    with col2:
        box_col, scatter_col = st.columns(2)
        with box_col:
            st.plotly_chart(y2_resid_box_whisker)
        with scatter_col:
            st.plotly_chart(y2_resid_plot)


    st.header("Influential Points")

    st.markdown("Sometimes when looking at points on a regression line you might wonder if any particular point "
                "significantly changes the line. And that generally can be found by finding points with the highest "
                "residuals. Especially if the residuals themselves are outliers as this will greatly affect "
                "the sum of the squares of the residuals which is why it's necessary to plot the residuals "
                "and look at their outliers first to identify these points.")