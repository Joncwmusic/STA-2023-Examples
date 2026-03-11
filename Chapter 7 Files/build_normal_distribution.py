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


def build_normal_distribution():

    dataset_coinflip_more = [binompdf(20, 0.5, i) for i in range(21)]
    dataset_norm = [normpdf(10,math.sqrt(5),0.1*i) for i in range(200)]

    df_coinflip_more = pd.DataFrame({"Num Heads": range(21), "Pr(x)": dataset_coinflip_more})
    df_norm = pd.DataFrame({"X": [0.1*i for i in range(200)], "Norm(X)":dataset_norm})

    ax_more = px.bar(data_frame=df_coinflip_more, x="Num Heads", y="Pr(x)")
    ax_norm = px.line(data_frame=df_norm, x= "X", y="Norm(X)")
    ax_more.add_traces(ax_norm.data)

    st.header("Why So Normal?")

    st.header("Characteristics of Normal")

    st.header("Standardizing the Normal Curve")