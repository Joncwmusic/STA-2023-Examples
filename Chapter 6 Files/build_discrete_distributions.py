import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio

def build_discrete_probaility_distributions():
    example_df = pd.DataFrame({"X": [0, 1, 2, 3], "Pr(X)": [0.05, 0.25, 0.55, 0.15]})
    example_dice_df = pd.DataFrame({"Roll": [1, 2, 3, 4, 5 ,6], "Pr(X = Roll)": [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]})
    example_casino_df = pd.DataFrame({"Outcomes": ["17 Black", "Everything Else"]
                                            , "Payout": [350,-10]
                                            , "Pr(Outcome)": [1/38, 37/38]})
    example_lottery_df = pd.DataFrame({"Outcomes": ["5 correct", "4 correct", "3 correct", "2 correct", "1 correct", "0 correct"]
                                        , "Payout": [9999990, 4990, 490, 40, -10, -10]
                                       , "Pr(Outcome)": [0.0000004, 0.00009, 0.00416,0.06239, 0.34315, 0.59021]})

    st.header("Discrete Random Variables")

    st.dataframe(example_df)
    st.dataframe(example_dice_df)

    st.subheader("Connecting Relative Frequency to Probability")

    st.markdown(r"$$\mu_{X} = \sum x_{i}Pr(x_i) \hspace{50pt} \sigma_X = "
                r"\sqrt{\sum (x_i -\mu_X)^2 Pr(x_i)} $$")
    st.markdown(r"$$\mu = \dfrac{\sum x_{i} w_{i}}{\sum w_{i}} \hspace{50pt} "
                r"\sigma = \dfrac{\sqrt{\sum (x_i-\mu)^2 w_i}}{\sum w_i} $$")

    st.header("Finding Mean (Expected Value) and Standard Deviation")

    st.subheader("Treat Probabilities as Weights (Let it Ride)")
    st.dataframe(example_casino_df)

    st.subheader("Is This Lottery Worth Playing?")
    st.dataframe(example_lottery_df)