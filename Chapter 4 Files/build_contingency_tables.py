import streamlit as st
import pandas as pd
import numpy as np
import math
import random
import plotly.express as px


def build_contingency_tables():

    example_df = pd.DataFrame(
        {
            "Republican": [185, 134, 3, 1, 323],
            "Democrat": [126, 178, 42, 2, 348],
            "Libertarian": [47, 25, 5, 1, 78],
            "Green Party": [12, 6, 0, 7, 25],
            "Total":[370, 343, 50, 11, 774]
        },
        index=["Male", "Female", "Non Binary", "Prefer not to Say", "Total"],
    )

    example_df_party_by_gender = pd.DataFrame(
        {
            "Republican": [185/370, 134/343, 3/50, 1/11, 323/774],
            "Democrat": [126/370, 178/343, 42/50, 2/11, 348/774],
            "Libertarian": [47/370, 25/343, 5/50, 1/11, 78/774],
            "Green Party": [12/370, 6/343, 0/50, 7/11, 25/774],
            "Total": [1, 1, 1, 1, 1]
        },
        index=["Male", "Female", "Non Binary", "Prefer not to Say", "Total"],
    )


    example_df_gender_by_party = pd.DataFrame(
        {
            "Male": [185/323,126/348,47/78,12/25,370/774],
            "Female": [134/323,178/348,25/78,6/25,343/774],
            "Non Binary": [3/323,42/348,5/78,0/25,50/774],
            "Prefer not to Say": [1/323,2/348,1/78,7/25,11/774],
            "Total": [1,1,1,1,1]
        },
        index=["Republican", "Democrat", "Libertarian", "Green", "Total"],
    )

    st.header("Categorical Data in 2 Dimensions")
    st.markdown("Not all of our 2 dimensional data will be quantitative. It may instead be qualitative which may call "
                "for the use of **contingency tables** to observe any patterns in the data. We can use the table to "
                "get marginal frequencies (similar to relative frequency). We can also use bar charts to "
                "visualize these relationships.")

    ax1 = px.bar(example_df_gender_by_party[["Male", "Female", "Non Binary", "Prefer not to Say"]])
    ax2 = px.bar(example_df_party_by_gender[["Republican", "Democrat", "Libertarian", "Green Party"]])

    st.table(example_df)

    st.header("Marginal Distribution")

    st.table(example_df_party_by_gender)
    st.plotly_chart(ax2)

    st.table(example_df_gender_by_party)
    st.plotly_chart(ax1)