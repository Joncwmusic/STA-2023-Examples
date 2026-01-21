import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
import math

pio.templates.default = "plotly"
import plotly.graph_objects as go
import plotly.subplots as psub


# Qualitative Data
def build_error_tab():
    year_list = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017
        , 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    price_list = [350 * random.gauss(mu=1, sigma=0.05) * math.exp((item - 2000) / 30) + random.gauss(mu=0, sigma=50)
                  for item in year_list]
    revenue_list = [(2025-item)*2 + 200*random.gauss(mu=1, sigma=0.2) for item in year_list]
    inflation_list = [1.05**(item-2000) + random.gauss(mu=0, sigma=0.005) for item in year_list]

    year_series = pd.Series(year_list, name='Years')
    price_series = pd.Series(price_list, name='STA Stock Price')
    inflation_series = pd.Series(inflation_list, name='CumeInflation Y2000')
    revenue_series = pd.Series(revenue_list, name='Revenue (In Millions)')

    stock_price_df = pd.concat([year_series, price_series], axis=1)
    inflation_df = pd.concat([year_series, inflation_series], axis=1)
    revenue_df = pd.concat([year_series, revenue_series], axis=1)

    st.title("Chapter 2: Organizing and Summarizing Data")
    st.header("Part 3: Bias in Visualizations")
    st.text("On occasion, or rather, all the time. People are using data to push some kind of narrative or agenda. "
            "You as the interpreter of said data are responsible for parsing out the bias and finding "
            "what exactly could be wrong with the data as it's presented. This does not mean the narrative "
            "is true or false, just that the data presented doesn't technically support the claim.")

    st.text("*Data is generated randomly and not indicative of an actual sample or population")

    st.header("Getting to Know Our Data")
    st.text("Below are 3 datasets. The first is the stock price for our fictional company with the ticker 'STA', "
            "the second is annual inflation since the year 2000, and the third is annual revenue for the company.")

    st.header("Stock Price")
    st.dataframe(stock_price_df)

    st.header("Inflation")
    st.dataframe(inflation_df)

    st.header("Revenue")
    st.dataframe(revenue_df)


    st.header("Bias through Y Axis Scaling")
    st.text("Pay Attention to the y-axes for the charts below. What do you notice? Does one chart seem to indicate "
            "more growth that the other? If your chart doesn't start from 0, it may be hard to contextualize "
            "the price growth against it's start in the chart. If you want to project an image of growth you "
            "probably will have an excellent time convincing people your growth is more impactful if it "
            "looks like you started from nothing.")

    fig_linear_y_axis = px.bar(data_frame = stock_price_df, x='Years', y='STA Stock Price', range_y=[0,1000])
    fig_limited_y_axis = px.bar(data_frame = stock_price_df, x='Years', y='STA Stock Price', range_y=[350, 850])
    fig_limited_y_axis.update_traces(marker=dict(color='red'))

    st.plotly_chart(fig_linear_y_axis)
    st.plotly_chart(fig_limited_y_axis)

    st.header("Cumulative Charts")
    st.text("Sometimes when your company is going through bad times, the leadership wants to see good news to "
            "share with stakeholders and instead of transparently telling them the money line is not going up, "
            "you're better off showing them technically accurate information that looks good but doesn't illustrate "
            "the real problem. One way to do that is to use cumulative graphs painting 2 different pictures."
            "By the way this was exactly how prior management thought about presenting information to hide revenue dips"
            "from their boss so that they could continue to push off the inevitable end of a dying product.")

    revenue_df['CumeRevenue'] = revenue_df['Revenue (In Millions)'].cumsum()

    fig_rev = px.bar(data_frame=revenue_df, x='Years', y='Revenue (In Millions)')
    fig_cume_rev = px.bar(data_frame=revenue_df, x='Years', y='CumeRevenue')
    fig_cume_rev.update_traces(marker=dict(color='red'))

    st.header("Cumulative Revenue (In millions)")
    st.plotly_chart(fig_cume_rev)
    st.text("Notice how this cumulative chart shows 'growth' but when we look under the hood at annual revenue... ")
    st.header("Actual Revenue (in Millions)")
    st.plotly_chart(fig_rev)

    st.header("Bad Groupings or Classes")
    st.text("So let's look at issues with different 'groups'. The chart below shows revenue by year but not "
            "so shamelessly hides the fact that the last revenue bucket is not one year... but FIVE years of revenue. "
            "This leaves you, the interpreter of this chart to do the work of slicing the bar into 5 pieces to see "
            "if your revenue 'growth' is actually real growth or is obfuscating the real story underneath the data.")

    new_year_list = [str(item) for item in year_list[0:20]]
    new_revenue_group = revenue_list[0:20]
    new_year_list.append('2021-2025')
    new_revenue_group.append(sum(revenue_list[21:25]))

    bad_group_df = pd.concat([pd.Series(new_year_list, name='Years'), pd.Series(new_revenue_group, name='Revenue (in millions)')], axis=1)
    fig_bad_groups = px.bar(data_frame=bad_group_df, x='Years', y='Revenue (in millions)')
    fig_bad_groups.update_traces(marker=dict(color='red'))

    st.plotly_chart(fig_bad_groups)

    st.header("Neglecting Context")

    inflation_price_df = pd.merge(stock_price_df, inflation_df, on='Years')
    inflation_price_df['InflationAdjustedPrice'] = inflation_price_df['STA Stock Price']/inflation_price_df['CumeInflation Y2000']
    fig_adjusted_price = px.bar(data_frame=inflation_price_df, x='Years', y='InflationAdjustedPrice')

    st.text("Sometimes the issue is not with the data itself but instead it's with the context. For example. The "
            "stock price of this company, STA, has been going up and so someone may look at this as a solid investment "
            "to increase their net worth and TO BE FAIR, it will put more money in your bank account in terms of raw "
            "dollars. But will this asset actually improve your buying power? That needs context. Specifically it "
            "needs to be considered with inflation. To adjust for inflation I just take the price and divide by the "
            "cumulative inflation to get an adjusted increase in price (by Year 200 standards.")

    st.header("Raw Price Changes")
    st.plotly_chart(fig_linear_y_axis, key='dupe revisit')

    st.header("Inflation Adjusted Price Changes")
    st.plotly_chart(fig_adjusted_price)
    st.text("Now that we've added context by incorporating inflation we see that the value of the stock is actually "
            "declining despite the price going up.")
