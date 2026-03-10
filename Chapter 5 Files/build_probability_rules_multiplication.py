import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random
from streamlit.components.v1 import html as sthtml
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import matplotlib.patches as patches

def build_probability_rules_multiplication():

    st.header("Independence")
    st.markdown("In the section introducing the rules we talked a little bit about addition rule which is only needed "
                "when we look at the probability or either event happening but not necessary both. In this section "
                "we're talking both happening at the same time. which brings us to the concept of independence.")
    st.markdown("**Independence** is the idea that 2 events do not affect each other whether or not they occur. "
                "For example, there's no reason why a coin flip that is 50-50 should no longer be 50-50 on the next "
                "flip. Flipping heads on this flip does not affect the chance of flipping heads or tails on the next "
                "flip. Each flip is independent.")

    st.subheader("Quick Example")

    st.markdown("Let's suppose we are flipping a coin twice and treat flip 1 and flip 2 as 2 different events. What's "
                "the probability of flipping 2 heads?")

    st.markdown("The sample space is: ")
    st.markdown(r"$S = \{HH, HT, TH, TT\}$")

    st.markdown("Each of these outcomes is equally likely so getting HH is one of 4 possibilities so")
    st.markdown(r"$Pr(HH) = \dfrac{1}{4}$")

    st.markdown(r"Another way to reason this is to say the probability of heads on flip 1 is $\frac{1}{2}$ and the "
                r"probability of heads on flip 2 is $\frac{1}{2}$ and if we multiply these we get $\frac{1}{4}$ "
                r"which matched our prior probability using the sample space. We'll talk more about that soon.")

    st.subheader("Other Examples")
    st.markdown("- Roulette spins at the casino")
    st.markdown("- Drawing a card, replacing it and shuffling the deck before drawing the next.")
    st.markdown("- With enough volume and a small enough observation you can assume independence i.e. trading in the "
                "stock market: one retail trader has negligible impact on the market with their $500 robinhood account"
                " even though yes, their gambling behavior does technically affect the market")

    st.header("Conditional Probability")

    st.markdown("Conditional Probability is the case when you can't assume independence. It doesn't take a lesson on "
                "the butterfly affect to tell you a lot of events in our lives are interconnected. If I get into a car "
                "crash that will impact my ability to show up to lecture on time. So, the event showing up to lecture "
                "is affected by the event getting into a crash.")

    st.markdown(r"We use the notation $Pr(A|B)$ to say probability of A given B. This is the probability of A "
                r"happening assuming B occurs.")

    example_df = pd.DataFrame(

        {
            "Republican": [185, 134, 3, 1, 323],
            "Democrat": [126, 178, 42, 2, 348],
            "Libertarian": [47, 25, 5, 1, 78],
            "Green Party": [12, 6, 0, 7, 25],
            "Total": [370, 343, 50, 11, 774]
        },
        index=["Male", "Female", "Non Binary", "Prefer not to Say", "Total"],
    )

    st.subheader("Example Data")
    st.dataframe(example_df)

    st.markdown("So contingency tables are really good for understanding conditional probabilities. Here we have 774 "
                "individuals of varying gender identities and political affiliations (The data isn't real) "
                "But we can use this table to find all kinds of probabilities.")

    st.markdown("Let's think through a couple examples:")
    st.markdown(r"- $Pr(\text{Republican} | \text{Female})$")
    st.markdown(r"- $Pr(\text{Non Binary} | \text{Democrat})$")

    st.markdown("For the first example we're asked to find the probability of someone being a republican given they "
                "identify as female. We need to pretend the sample space is all females in the data as that is what we "
                "assume when we read 'given' in our probabilities. So, we consider only the 'Female' row and look at "
                "the republicans within that space which gives us:")

    st.markdown(r"$Pr(\text{Republican} | \text{Female}) = \dfrac{134}{343} \approx 0.39$")

    st.markdown("Likewise the probability someone is non binary GIVEN they are a democrat assume we're ONLY looking "
                "at the scenario where the person we picked is a democrat guaranteed. So, we have to consider 348 "
                "as our denominator and specifically the 42 Non Binary democrats as our numerator. So:")

    st.markdown(r"$Pr(\text{Non Binary} | \text{Democrat}) = \dfrac{42}{348} \approx 0.12$")

    st.markdown("In general,")
    st.markdown(r"$Pr(A|B) = \dfrac{Pr(A \text{ and } B)}{Pr(B)}$")
    st.markdown("It should be noted that if two events are independent then $Pr(A|B) = Pr(A)$ because $B$ does not "
                "affect whether $A$ happens")

    st.header("Multiplication Rule")
    st.markdown("We can summarize these cases as two (kind of) multiplication rules:")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Independent Events")
        st.markdown(r"$Pr(A \text{ and } B) = Pr(A) \cdot Pr(B)$")
    with col2:
        st.subheader("Dependent Events")
        st.markdown(r"$Pr(A \text{ and } B) = Pr(A|B) \cdot Pr(B)$")
