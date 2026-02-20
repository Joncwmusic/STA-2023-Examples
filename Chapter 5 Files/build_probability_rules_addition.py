import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random

def build_probability_rules():

    st.header("Probability Rules and the Law of Large Numbers")
    st.markdown("""
    Probability quantifies uncertainty and always lies between **0 and 1**:
    - 0 means an event is **impossible**  
    - 1 means an event is **certain**

    The **sum of all possible outcomes** for a given experiment equals 1.
    """)

    st.divider()
    st.subheader("The Law of Large Numbers")

    st.markdown("""
    Let's simulate rolling a fair six-sided die.  
    The theoretical probability of rolling each number (1–6) is **1/6 ≈ 0.1667**.  
    But what happens when we simulate the experiment many times?
    """)

    n_rolls = st.slider("Number of Dice Rolls", 10, 10000, 1000, step=10)

    # Simulate dice rolls
    rolls = np.random.randint(1, 7, size=n_rolls)
    freq = pd.Series(rolls).value_counts(normalize=True).sort_index()
    df = pd.DataFrame({
        "Die Face": freq.index,
        "Empirical Probability": freq.values
    })

    fig = px.bar(
        df,
        x="Die Face",
        y="Empirical Probability",
        text=np.round(df["Empirical Probability"], 3),
        range_y=[0, 0.3],
        title=f"Empirical vs Theoretical Probabilities (n={n_rolls})",
        color_discrete_sequence=["#636EFA"]
    )
    fig.add_hline(y=1/6, line_dash="dash", line_color="red",
                  annotation_text="Theoretical P = 1/6")

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    As the number of rolls increases, the relative frequencies (empirical probabilities)  
    converge toward their theoretical values — this is the **Law of Large Numbers**.
    """)

    st.divider()
    st.subheader("➕ The Addition Rule")

    st.markdown("""
    There are two versions of the **Addition Rule**:

    1. **Disjoint (Mutually Exclusive) Events**  
       If A and B cannot occur together:  
       $$P(A \\text{ or } B) = P(A) + P(B)$$  

    2. **General Addition Rule**  
       For any two events:  
       $$P(A \\text{ or } B) = P(A) + P(B) - P(A \\text{ and } B)$$

    Let's visualize this with dice events.
    """)

    st.divider()
    st.subheader("Example: Rolling a Single Die")

    st.markdown("""
    Let event A = rolling an **even number**  
    Let event B = rolling a **number greater than 3**
    """)

    # Define outcomes
    outcomes = np.array([1, 2, 3, 4, 5, 6])
    A = set([2, 4, 6])  # even
    B = set([4, 5, 6])  # > 3

    p_A = len(A)/6
    p_B = len(B)/6
    p_AandB = len(A & B)/6
    p_AorB = p_A + p_B - p_AandB

    st.latex(f"P(A) = {p_A:.2f},\\quad P(B) = {p_B:.2f},\\quad P(A∩B) = {p_AandB:.2f}")
    st.latex(f"P(A∪B) = P(A) + P(B) - P(A∩B) = {p_AorB:.2f}")

    st.markdown(f"""
    So the probability of rolling an even number **or** a number greater than 3 is **{p_AorB:.2f}**.
    """)

    # Visualize event overlap
    df_overlap = pd.DataFrame({
        "Outcome": outcomes,
        "Event A (Even)": [1 if x in A else 0 for x in outcomes],
        "Event B (>3)": [1 if x in B else 0 for x in outcomes],
    })
    df_overlap["Outcome Type"] = df_overlap.apply(
        lambda r: "A ∩ B" if r["Event A (Even)"] and r["Event B (>3)"]
        else ("A only" if r["Event A (Even)"] else ("B only" if r["Event B (>3)"] else "Neither")),
        axis=1
    )

    fig2 = px.bar(
        df_overlap,
        x="Outcome",
        color="Outcome Type",
        color_discrete_map={
            "A ∩ B": "#EF553B",
            "A only": "#636EFA",
            "B only": "#00CC96",
            "Neither": "#AB63FA"
        },
        title="Overlap of Events A and B"
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""
    The overlap (red) shows outcomes that belong to both events.  
    That’s why we subtract \\(P(A \\text{ and } B)\\) in the **General Addition Rule** —  
    to avoid double counting those outcomes.
    """)

    st.divider()
    st.subheader("Key Takeaways")

    st.markdown("""
    - Probabilities are **always between 0 and 1**.  
    - The **sum of all possible outcomes** = 1.  
    - **Disjoint events**: add probabilities directly.  
    - **Non-disjoint events**: subtract overlap.  
    - The **Law of Large Numbers** ensures empirical frequencies approach theoretical ones.
    """)