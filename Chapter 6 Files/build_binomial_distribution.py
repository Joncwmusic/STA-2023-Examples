import math
import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
import plotly.graph_objs as go

def factorial(n):
    product = 1
    for i in range(n):
        product *= i + 1
    return product

def binompdf(n, p, x):
    prob = factorial(n)/(factorial(n-x)*factorial(x)) * p**x*(1-p)**(n-x)
    return prob

def binomcdf(n, p, x):
    sum = 0
    for i in range(x+1):
        sum += binompdf(n, p, i)
    return sum

def normpdf(mu, sigma, x):
    part_1 = 1/(sigma*math.sqrt(2*math.pi))
    part_2 = math.exp(-((x-mu)**2)/(2*sigma**2))
    return part_1 * part_2


def build_binomial_distribution():


    dataset_coinflip = [binompdf(6, 0.5, i) for i in range(7)]
    dataset_sales = [binompdf(10, 0.18, i) for i in range(11)]
    dataset_coinflip_more = [binompdf(20, 0.5, i) for i in range(21)]
    dataset_norm = [normpdf(10,math.sqrt(5),0.1*i) for i in range(200)]


    df_coinflip = pd.DataFrame({"Num Heads": range(7), "Pr(x)": dataset_coinflip})
    df_sales = pd.DataFrame({"Num Sales": range(11), "Pr(x)": dataset_sales})
    df_coinflip_more = pd.DataFrame({"Num Heads": range(21), "Pr(x)": dataset_coinflip_more})
    df_norm = pd.DataFrame({"X": [0.1*i for i in range(200)], "Norm(X)":dataset_norm})

    ax_coin = px.bar(data_frame=df_coinflip, x="Num Heads", y="Pr(x)")
    ax_sales = px.bar(data_frame=df_sales, x="Num Sales", y="Pr(x)")

    ax_more = px.bar(data_frame=df_coinflip_more, x="Num Heads", y="Pr(x)")
    ax_norm = px.line(data_frame=df_norm, x= "X", y="Norm(X)")
    ax_more.add_traces(ax_norm.data)

    st.header("The Obsession with Coin Flips")

    coincol1, coincol2 = st.columns(2)

    with coincol1:
        st.dataframe(df_coinflip)
    with coincol2:
        st.plotly_chart(ax_coin)

    st.header("Binomial Distribution is a Probability Distribution")

    sales_col1, sales_col2 = st.columns(2)

    with sales_col1:
        st.dataframe(df_sales)
    with sales_col2:
        st.plotly_chart(ax_sales)

    st.header("Finding Mean and Standard Deviation")

    st.header("Binomial Distributions are Roughly Bell Shaped")
    st.plotly_chart(ax_more)