import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random
from streamlit.components.v1 import html as sthtml
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import matplotlib.patches as patches

def build_probability_rules_addition():

    dice_options = [1, 2, 3, 4, 5, 6]
    probability_fair = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
    probability_unfair = [0.1, 0.1, 0.1, 0.2, 0.2, 0.3]

    coin_flip_list = []

    fair_df = {"Roll":dice_options, "Probability":probability_fair}
    unfair_df = {"Roll": dice_options, "Probability": probability_unfair}

    st.header("Probability Rules and the Law of Large Numbers")
    st.markdown("Probability is an interesting landscape of uncertainties and trying to quantify possibilities to "
                "make sure we kid ourselves into believing the consequences of our own actions are no more valid "
                "than luck itself. But in an attempt to pursue objectivity within a landscape of noise, we have "
                "found a way to do just that. So let's explore this by covering a few rules of probability.")

    st.markdown("In probability there is something called a **Sample Space** that contains all the possible outcomes "
                r"of an event. Think of a coin flip. The sample space is $S=\{Heads, Tails\}$. This Sample Space is "
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
                "the closer you will get to the true probability of the outcomes of the experiment. You can see this "
                "for yourself by setting the number of flips and hitting the flip button.")

    with open("Chapter 5 Files/coin_flip_sim.html", "r") as f:
        html_content = f.read()

    sthtml(html_content, height=150)

    st.subheader("The Rules")

    st.markdown("- The sum of all probabilities of the possible outcomes of an event must be equal to 1 ")
    st.markdown("- and any probability of an outcome must be between 0 and 1.")

    st.markdown("In math notation land that is: ")
    st.markdown("- $\sum_{x \in S} Pr(x) = 1$")
    st.markdown("- $0 \leq Pr(x) \leq 1$ for any $x \in S$")

    st.header("Other Rules")
    st.subheader("Addition Rule")

    st.markdown("Events don't happen in isolation and so if you want to find the probability of one event happening OR "
                "another event happening, you might want to consider their individual probabilities and combine them. "
                "Enter the addition rule:")

    st.markdown(r"$$Pr(A \text{ or } B) = Pr(A)+Pr(B)-Pr(A \text{ and } B)$$")

    st.markdown("Where did that 'A and B' come from? And why is it being taken away? Let's take a moment to think "
                "about it.")

    st.markdown("Okay no more thinking. Let's draw pictures.")

    fig, ax = plt.subplots()
    v = venn2(subsets=(0.6, 0.3, 0.1), set_labels=("Pr(A)", "Pr(B)"), ax=ax)
    st.pyplot(fig)

    st.markdown("If we represent events as a venn diagram the events have the potential to overlap. This means if we "
                "strictly add the probabilities of events A and B we double count the possibilities where they both "
                "happen. So as long as we subtract that intersection once, we're now considering all types of "
                "outcomes once.")

    st.markdown("Note that if the events cannot happen at the same time, we consider them 'disjoint' and their venn "
                "diagrams look like this instead")

    fig3, ax3 = plt.subplots()
    v = venn2(subsets=(0.4, 0.3, 0), set_labels=("Pr(A)", "Pr(B)"), ax=ax3)
    st.pyplot(fig3)

    st.subheader("Complements")
    st.markdown("While you may look super cutie today, that's not what I'm talking about when I say complement. "
                "Complements are the opposite of the event occurring. In other words while there is a probability "
                "of an event happening, there is also a probability of an event not happening. And so, if you have "
                "a probability and subtract it from 1 which is the probability of all possibilities together, you "
                "get the probability of the event NOT happening.")

    st.markdown(r"$$Pr(A^c) = 1-Pr(A)$$")

    fig2, ax2 = plt.subplots()

    # Draw universal set rectangle
    rect = patches.Rectangle((-1, -0.75), 2, 1.5, linewidth=1, edgecolor='black', facecolor='none')
    ax2.add_patch(rect)
    ax2.text(-0.9, 0.6, "Pr(not A)", fontsize=10)

    venn2(subsets=(0.5, 0, 0), set_labels=("Pr(A)", " "), ax=ax2)

    ax2.set_xlim(-1, 1)
    ax2.set_ylim(-.75, .75)

    st.pyplot(fig2)

