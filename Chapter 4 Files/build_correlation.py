import streamlit as st
import pandas as pd
import numpy as np
import math
import random
import plotly.express as px


def build_correlation():

    x_values = [i for i in range(-20, 70)]
    y_values = [-0.5*((i/10)-5)**2 + 3 + random.gauss(mu=0, sigma=2) for i in range(-20, 70)]

    example_df = pd.DataFrame({"Inputs": x_values, "Outputs": y_values})
    init_scatter = px.scatter(example_df, x="Inputs", y="Outputs")

    st.header("2 Dimensional Data")

    st.dataframe(example_df)

    st.header("Visualizing 2D Data")

    st.markdown("Use a **scatter plot** to visualize 2D data with the x axis being the *explanatory variable* and "
                "y axis being the **observed variable**")

    st.plotly_chart(init_scatter)

    st.header("Correlation")

    st.markdown("Correlation **IS NOT** causation. But it gives us a finger in the wind to investigate further for "
                "causality. One way to quantify correlation is the Pearson correlation which take the sum of the "
                "point by point product of z scores for both the x axis and y axis data and then dividing by the "
                "number of items in the sample. There's a more technical definition that looks even scarier based "
                "on covariances but we don't have to talk about that right now. For now we'll go over how to compute "
                "everything by hand.")

    st.markdown(r"$$ r = \dfrac{\sum(\dfrac{x_i-\bar{x}}{s_x})(\dfrac{y_i-\bar{y}}{s_y})}{n-1}$$")

    st.markdown(r"Okay so let's break this formula down. The first thing you need to do is find "
                r"$s_x, s_y, \bar{x}, \bar{y}$ which are the standard deviations and means of your x and y values.")

    # Calculate all the variables
    x_bar = example_df["Inputs"].mean()
    y_bar = example_df["Outputs"].mean()
    s_x = example_df["Inputs"].std()
    s_y = example_df["Outputs"].std()

    init_df = example_df.copy()
    init_df["x Mean"], init_df["y Mean"], init_df["x Std Dev"], init_df["y Std Dev"] = x_bar, y_bar, s_x, s_y

    st.dataframe(init_df)

    st.markdown(r"Now all we have to do is calculate the $(\dfrac{x_i-\bar{x}}{s_x})(\dfrac{y_i-\bar{y}}{s_y})$ part "
                r"which we'll break out into 3 more columns namely the z scores for all the x values, "
                r"$(\dfrac{x_i-\bar{x}}{s_x})$, the z scores for all the y values $(\dfrac{y_i-\bar{y}}{s_y})$ "
                r"and then of course the full product.")

    final_df = init_df.copy()

    final_df["(x_i-xbar)/sx"] = (final_df["Inputs"] - final_df["x Mean"])/final_df["x Std Dev"]
    final_df["(y_i-ybar)/sy"] = (final_df["Outputs"] - final_df["y Mean"])/final_df["y Std Dev"]
    final_df["((x_i-xbar)/sx)((y_i-ybar)/sy)"] = final_df["(x_i-xbar)/sx"]*final_df["(y_i-ybar)/sy"]

    x_sum = final_df["Inputs"].sum()
    y_sum = final_df["Outputs"].sum()
    zx_sum = final_df["(x_i-xbar)/sx"].sum()
    zy_sum = final_df["(y_i-ybar)/sy"].sum()
    r_presum = final_df["((x_i-xbar)/sx)((y_i-ybar)/sy)"].sum()

    st.dataframe(final_df)

    st.markdown("Here are the totals. the means and deviations are not summed. Also notice the z scores all sum to "
                "basically 0. Make a note of that for later chapters.")

    total_df = pd.DataFrame({"Inputs": [x_sum], "Outputs": [y_sum], "x Mean": [x_bar], "y Mean": [y_bar]
                                , "x Std Dev": [s_x], "y Std Dev": [s_y], "(x_i-xbar)/sx": [zx_sum]
                                , "(y_i-ybar)/sy": [zy_sum], "((x_i-xbar)/sx)((y_i-ybar)/sy)": [r_presum]})

    st.markdown(r"Now just divide by the number of data points minus which in this case is 90-1 so "
                r"$r = " + str(r_presum) + r"\div 89 \approx 0.884$ ")

    st.dataframe(total_df)

    st.header("Formulas")
    st.markdown(r"Pearson Correlation Coefficient:"
                r"$$ r = \dfrac{\sum(\dfrac{x_i-\bar{x}}{s_x})(\dfrac{y_i-\bar{y}}{s_y})}{n-1}$$"
                r"Line of best fit")