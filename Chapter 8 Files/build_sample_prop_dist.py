import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
import math


def build_sample_prop_page():
    st.header("Distribution of a Sample Proportion")

    st.subheader("Comparing to the Sample Mean")