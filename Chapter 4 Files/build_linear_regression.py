import streamlit as st
import pandas as pd
import numpy as np
import math
import random
import plotly.express as px
import plotly.graph_objs as go


def build_linear_regression():

    x_values = [i for i in range(-20, 70)]
    y_values = [-0.5*((i/10)-5)**2 + 3 + random.gauss(mu=0, sigma=2) for i in range(-20, 70)]
    categories = ["marked" if i in (-10, 42) else "data" for i in range(-20,70)]

    example_df = pd.DataFrame({"Inputs": x_values, "Outputs": y_values, "Category":categories})

    init_scatter = px.scatter(example_df, x="Inputs", y="Outputs", color="Category")

    st.header("Our Data and Scatter Plot")

    st.dataframe(example_df[["Inputs", "Outputs", "Category"]])
    st.plotly_chart(init_scatter)

    st.header("Regression Lines")
    st.markdown("Okay if you remember from algebra $y=mx+b$ is the bane of most students' existences "
                "as they wonder how they'll ever use it real life. Here it is... in real life. You might be able to "
                "to use a line to predict what would happen if you had a new input value and wanted to see what the "
                "output value **should** be.")

    st.markdown("You may have also noticed I marked 2 points on the regression line. If you can stomach going back "
                "into your dark algebraic past you might be able to recall a line can be defined by 2 points. "
                "You could use point slope form and find slope before making the equation of a line")

    st.markdown(r"$$ y-y_1=m(x-x_1)$$ $$m=\dfrac{y_2-y_1}{x_2-x_1}$$")

    y_2, y_1, x_2, x_1 = round(y_values[10], 2),  round(y_values[62], 2),  round(x_values[10], 2), round(x_values[62], 2)
    slope = (y_2-y_1)/(x_2-x_1)

    x_range_1, y_range_1 = (-20, slope*(-20-x_1)+y_1)
    x_range_2, y_range_2 = example_point_2 = (70, slope*(70-x_2)+y_2)
    line_df = pd.DataFrame({"Inputs": [x_range_1, x_range_2], "Outputs": [y_range_1, y_range_2]})

    st.markdown(r"Those two points are $(x_1,y_1) = (" + str(x_1) + "," + str(y_1) +
                r")$ and $(x_2, y_2) = (" + str(x_2) + "," + str(y_2) + "$) which we can use to find the equation of "
                                                                        "**A** line. But is it the best line?")


    new_scatter_axis = px.scatter(example_df, x="Inputs", y="Outputs", color="Category")
    new_scatter_axis.add_trace(
        go.Scatter(
            x=line_df["Inputs"],
            y=line_df["Outputs"],
            mode="lines",
            name="Regression Line"
        )
    )

    st.plotly_chart(new_scatter_axis)

    st.header("The Line of BEST Fit")

    resid_axis = px.scatter(example_df, x="Inputs", y="Outputs", color="Category")
    resid_axis.add_trace(
        go.Scatter(x=line_df["Inputs"],y=line_df["Outputs"],mode="lines",name="Regression Line"))

    for index,row in example_df.iterrows():
        resid_axis.add_shape(type="line",xref="x", yref="y",x0=row["Inputs"],y0=row["Outputs"],x1=row["Inputs"]
                             ,y1=slope*(row["Inputs"]-x_1)+y_1,line=dict(color="Red",width=2,dash="dot"))

    st.markdown("The way we determine if a line is a 'good fit' is based on the residual sum of squares. Visually, "
                "you have to look at the differences between the y values observed and what the line predicts it to "
                "be and you must minimize those differences (technically the square of those differences because an "
                "overestimate doesn't cancel an underestimate). Luckily we have a formula for the line that does that.")

    #### insert formula for line of best fit
    st.markdown(r"$$ $$")

    st.plotly_chart(resid_axis)
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

    st.dataframe(final_df)

    x_sum = final_df["Inputs"].sum()
    y_sum = final_df["Outputs"].sum()
    zx_sum = final_df["(x_i-xbar)/sx"].sum()
    zy_sum = final_df["(y_i-ybar)/sy"].sum()
    r_presum = final_df["((x_i-xbar)/sx)((y_i-ybar)/sy)"].sum()


    st.markdown("Here are the totals. the means and deviations are not summed. Also notice the z scores all sum to "
                "basically 0. Make a note of that for later chapters.")

    total_df = pd.DataFrame({"Inputs": [x_sum],"Outputs": [y_sum],"x Mean": [x_bar],"y Mean": [y_bar]
                     , "x Std Dev": [s_x], "y Std Dev": [s_y], "(x_i-xbar)/sx": [zx_sum]
                     , "(y_i-ybar)/sy": [zy_sum], "((x_i-xbar)/sx)((y_i-ybar)/sy)": [r_presum]})

    st.markdown(r"Now just divide by the number of data points minus which in this case is 90-1 so "
                r"$r = " + str(r_presum) + r"\div 89 \approx 0.884$ ")

    st.dataframe(total_df)

    st.header("Formulas")
    st.markdown(r"Pearson Correlation Coefficient:"
                r"$$ r = \dfrac{\sum(\dfrac{x_i-\bar{x}}{s_x})(\dfrac{y_i-\bar{y}}{s_y})}{n-1}$$"
                r"Line of best fit")