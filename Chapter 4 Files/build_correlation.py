import streamlit as st
import pandas as pd
import numpy as np
import math
import random
import plotly.express as px


def build_correlation():

    x_values = [i for i in range(-20, 100)]
    y_values = [-0.5*((i/10)-5)**2 + 3 + random.gauss(mu=0, sigma=0.25) for i in range(-20, 100)]
    example_df = pd.DataFrame({"Inputs":x_values, "Outputs":y_values})
    px.scatter(example_df, x="Inputs", y="Outputs")

    st.header("2 Dimensional Data")

    st.dataframe(example_df)

    st.header("Visualizing 2D Data")

    st.markdown("Use a **scatter plot** to visualize 2D data with the x axis being the *explanatory variable* and "
                "y axis being the **observed variable**")

    st.header("Correlation")