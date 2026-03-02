import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random


def record_flip(coin_flip_list):
    coin_flip_list.append(random.choice(["Heads","Tails"]))

def reset_flip(coin_flip_list):
    coin_flip_list.clear()
    return None

def build_probability_rules_addition():

    dice_options = [1, 2, 3, 4, 5, 6]
    probability_fair = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
    probability_unfair = [0.1, 0.1, 0.1, 0.2, 0.2, 0.3]

    coin_flip_list = []

    if 'click_count' not in st.session_state:
        st.session_state.click_count = 0

    # Button with callback
    st.button("Click me", on_click=increment_counter)

    st.write(f"Button clicked {st.session_state.click_count} times")

    fair_df = {"Roll":dice_options, "Probability":probability_fair}
    unfair_df = {"Roll": dice_options, "Probability": probability_unfair}

    st.header("Probability Rules and the Law of Large Numbers")
    st.markdown("Probability is an interesting landscape of uncertainties and trying to quantify possibilities to "
                "make sure we kid ourselves into believing the consequences of our own actions are no more valid "
                "than luck itself. But in an attempt to pursue objectivity within a landscape of noise, we have "
                "found a way to do just that. So let's explore this by covering a few rules of probability.")

    st.markdown("In probability there is something called a **Sample Space** that contains all the possible outcomes "
                "of an event. Think of a coin flip. The sample space is $S={Heads, Tails}$. This Sample Space is "
                "context dependent and each outcome may or may not be equally likely. For example a 6 sided die may "
                "be equally likely to fall on any of the 6 faces, but a loaded die would have the same sample space "
                "with each outcome being a different probability")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Fair Die Probabilities")
        st.dataframe(fair_df)
    with col2:
        st.subheader("Unfair Die Probabilities")
        st.dataframe(unfair_df)

    st.markdown("These dice have the **Same Outcomes** but the chances for each of these outcomes is different.")

    st.header("The Law of Large Numbers")

    st.markdown("So how would you determine whether or not these dice are fair? That's where the "
                "**Law of Large Numbers** comes in. Basically, the more times you repeat a probability experiment "
                "the closer you will get to the true probability of the outcomes of the experiment. Let's try this with"
                "a coin flip. Press the button for heads or tails")

    result = st.button(label = "Heads or Tails", on_click=increment_counter())


    clear_command = st.button(label = "Reset", on_click=reset_counter)

    st.subheader("The Rules")

    st.markdown("- The sum of all probabilities of the possible outcomes of an event must be equal to 1 ")
    st.markdown("- and any probability of an outcome must be between 0 and 1.")

    st.markdown("In math notation land that is: ")
    st.markdown("- $\sum_{x \in S} Pr(x) = 1$")
    st.markdown("- $0 \leq Pr(x) \leq 1$ for any $x \in S$")

