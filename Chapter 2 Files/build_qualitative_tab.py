import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly"



# Qualitative Data
def build_qualitative_tab():
    label_dict = {1: "Republican Party", 2: "Republican Party", 3: "Democratic Party", 4: "Democratic Party",
                  5: "Libertarian Party", 6: "Green Party", 7: "Harambe 4life Party"}
    data_list = [random.randint(1, 7) for x in range(200)]
    cat_data_list = [label_dict[item] for item in data_list]

    raw_df = pd.DataFrame(data=cat_data_list, columns=["Party Affiliation"])
    summarized_df = raw_df.groupby(["Party Affiliation"]).size().to_frame('Count')

    relative_freq_df = summarized_df.copy()
    relative_freq_df['Proportion'] = relative_freq_df['Count']/200


    summarized_df = summarized_df.reset_index()
    relative_freq_df = relative_freq_df.reset_index()
    #
    # print(summarized_df)
    # print(relative_freq_df)

    num_data_list = [round(random.gauss(mu=5, sigma=2), 1) for i in range(200)]
    skewed_data_list = [x*1.1 for x in num_data_list if x > 4]


    st.title("Chapter 2: Organizing and Summarizing Data")
    st.header("Part 1: Qualitative Data Visualizations")
    st.text("When presented with qualitative data like categories, you can get frequency tables to get a count of each "
            "category and try to draw some conclusions about your data. Namely, you can make bar charts and pie charts "
            "from either the frequencies or relative frequencies. Here's what that might look like.")

    st.text("*Data is generated randomly and not indicative of an actual sample or population")

    # RAW DATA AND TABLES
    st.header("Raw Data")
    st.text("The following data is a list of individuals each with a political party affiliation.")
    st.dataframe(raw_df)

    st.header("Summarized Data")
    st.text("Here is both a table summarizing the total number of people in each party and the relative frequency "
            "(the *proportion* of individuals belonging to each group). The relative frequency should ALWAYS add up to 1.")
    st.dataframe(summarized_df)
    st.dataframe(relative_freq_df)

    # BAR CHARTS
    st.header("Bar Charts")
    st.text("Here are the bar charts and you'll notice they look exactly the same, besides their axes labels and scaling.")
    bar_count_fig = px.bar(summarized_df, x='Party Affiliation', y='Count', color='Party Affiliation', color_discrete_map={'Republican Party':'red',
                                     'Democratic Party':'blue',
                                     'Libertarian Party':'yellow',
                                     'Green Party':'green',
                                     'Harambe 4life Party': "cyan"})
    bar_relfreq_fig = px.bar(relative_freq_df, x='Party Affiliation', y='Proportion',color='Party Affiliation', color_discrete_map={'Republican Party':'red',
                                     'Democratic Party':'blue',
                                     'Libertarian Party':'yellow',
                                     'Green Party':'green',
                                     'Harambe 4life Party': "cyan"})

    st.plotly_chart(bar_count_fig)
    st.plotly_chart(bar_relfreq_fig)


    # PIR CHARTS
    st.header("Pie Chart")
    st.text("And here's the pie chart conveying basically the same information.")
    pie_relfreq_fig = px.pie(summarized_df, values='Count', names='Party Affiliation'
                             , color_discrete_map={'Republican Party':'red',
                                     'Democratic Party':'blue',
                                     'Libertarian Party':'yellow',
                                     'Green Party':'green',
                                     'Harambe 4life Party': "cyan"})
    st.plotly_chart(pie_relfreq_fig)

    st.text("You might notice that the pie chart conveys effectively the same information and so "
        "in most contexts you don't really see pir charts being front and center in most dashbaords since bar "
        "charts generally do an equivalent job at conveying the messaging of the data.")