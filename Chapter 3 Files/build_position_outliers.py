import math
import random
import streamlit as st
import pandas as pd
import plotly.express as px
import build_central_tendency as bct
import util_functions as uf


def get_z_score(val, mu, sigma):
    return (val-mu)/sigma


def build_position_outliers():

    x_axis = [x/50 for x in range(-200,200)]
    normal_curve = [1/math.sqrt(2*math.pi)*math.exp(-x**2) for x in x_axis]

    x_series = pd.Series(x_axis, name='domain')
    y_series = pd.Series(normal_curve, name='range')
    normal_df = pd.DataFrame({'domain': x_series, 'range': y_series})

    # st.dataframe(normal_df)

    normal_ax = px.line(data_frame=normal_df, x='domain', y='range')


    x_axis_blank = pd.Series([x for x in range(101)])
    curve = pd.Series([0 for item in x_axis_blank])
    blank_line_df = pd.DataFrame({'domain':x_axis_blank, 'range':curve})

    line_ax = px.line(data_frame=blank_line_df, x='domain', y='range')


    st.header("Measures of Position and Outliers")

    st.subheader("The Scenario")
    st.text("Let's suppose you're tracking your exam progress in a statistics class with 2 exams And receive a 77 and"
            " and 82. You may be thinking 'Hey, I think I'm getting better at this' and that may very well be true "
            "but leave it your professor to ruin your dreams and tell you otherwise. You learn the average exam "
            "scores for each test are 72 and 78, respectively, and the standard deviations are 6 and 10. "
            "so what does this mean about your performance relative to the class? ")

    st.text("This is where z-score comes in. z-score standardizes your mean and standard deviation to 0 and 1 so you "
            "can actually compare apples and oranges.")

    st.latex(r'''z=\dfrac{x-\mu}{\sigma}''')

    st.text("So now that we have formulas for z-score, let's use it to see if you actually did any better.")

    st.latex(r'''z_1=\dfrac{77-72}{6}=0.83 \hspace{50pt} z_2=\dfrac{82-78}{10}=0.40''')

    st.text("Well... this is awkward. It looks like relative to the rest of the class you actually did a little worse "
            ". That's no bueno. Looks like you need to study more.")

    st.subheader("Percentile with the bell curve (Empirical Rule)")

    normal_ax.add_vline(x=1, line_width=2, line_dash="dash", line_color="green")
    normal_ax.add_vline(x=-1, line_width=2, line_dash="dash", line_color="green")
    normal_ax.add_vline(x=2, line_width=2, line_dash="dash", line_color="yellow")
    normal_ax.add_vline(x=-2, line_width=2, line_dash="dash", line_color="yellow")
    normal_ax.add_vline(x=3, line_width=2, line_dash="dash", line_color="red")
    normal_ax.add_vline(x=-3, line_width=2, line_dash="dash", line_color="red")
    normal_ax.add_vline(x=0, line_width=2, line_dash="dash", line_color="blue")
    st.plotly_chart(normal_ax)

    st.text("So the math below in plain english implies for any bell shaped distribution 68% of data is inside the "
            "green lines, 95% of data is within the yellow lines and 99.7% of the data lives within the red lines. "
            "As it turns out, each line corresponds to a standard deviation away from the mean.")


    st.latex(r'''P(\mu - \sigma \leq X \leq \mu + \sigma) \approx 0.68 \\
P(\mu - 2\sigma \leq X \leq \mu + 2\sigma) \approx 0.95 \\
P(\mu - 3\sigma \leq X \leq \mu + 3\sigma) \approx 0.997
''')

    st.header("Percentiles, Quartiles, and IQR")
    st.subheader("Percentiles vs. Quartiles")

    st.text("Percentiles another way to determine your position with respect to a group. If you're in the top 100 of a"
            " group of 10000 people your percentile is 99% since you are better than 99% of everyone in the group. "
            "One key percentile to look at is the 50th percentile because this point is where 50% of subjects are above"
            " and below this point. So it cuts the data in half... I wonder where we've heard that before.")

    st.text("*cough cough* the median *cough cough*")

    st.text("Other important percentiles are the 25th and 75th percentile because they show the middle 50% of data "
            "They also correspond to the middle of each half. And if you consider the 25th, 50th, and 75th "
            "percentiles together they actually correspond the quartiles Q1, Q2, and Q3")

    st.text("To find Q1 and Q3 it's as simple as taking the median of each half of data separated by the median "
            "of the entire data set. Each green line in the graph below corresponds to the quartiles.")

    line_ax.add_vline(x=25, line_width=2, line_dash="dash", line_color="green")
    line_ax.add_vline(x=50, line_width=2, line_dash="dash", line_color="green")
    line_ax.add_vline(x=75, line_width=2, line_dash="dash", line_color="green")
    st.plotly_chart(line_ax)

    st.text("So now if you take the difference between Q3 and Q1, that range is known as the inter quartile range "
            " (IQR) which is used to compute boundaries for determining outliers called fences. Here are the formulas:")

    st.text("Lower Fence:")
    
    st.latex(r''' Q_1 - 1.5(IQR) ''')
    
    st.text("Upper Fence")
    
    st.latex(r''' Q_3 + 1.5(IQR)''')

    st.text("Anything that sits outside these boundaries is considered an outlier. But understand this is more of "
            "a heuristic than ")

    st.header("Five Number Summary and Box and Whisker Plots")
    st.subheader("Five Number Summary")

    st.text("The five number summary is effectively 5 numbers that give you a rough idea of the shape of your data "
            "without having to plot everything. Specifically, they are the minimum, Q1, median, Q3, and maximum. "
            "Let's jump into a quick example")

    five_num_sum_example = [-10, 0, 4, 4, 5, 6, 7, 8, 9, 9, 9, 10, 12, 13, 14, 15, 16, 17, 17, 19, 35, 40]

    min_val, q1, q2, q3, max_val = uf.get_five_num_summary_numpy(five_num_sum_example)

    st.dataframe(five_num_sum_example)
    st.text("So the 5 number summary for the above data is as follows: \n" + "Min: " + str(min_val)
            + "\n Q1: " + str(q1) + "\n Median: " + str(q2) + "\n Q3: " + str(q3) + "\n Max: " + str(max_val))

    st.subheader("Box and Whisker Plots")

    st.text("A box and whisker plot takes your five number summary in consideration of the fences and plots them "
            "where the edges of the box represent Q1 and Q3, the middle line in the box is the median, and the "
            "whiskers represent the rest of the data. Any dots on the plot are data points outside the fences.")
    five_num_df = pd.DataFrame({'values': five_num_sum_example})
    box_and_whisk_ax = px.box(five_num_df, x="values")

    st.plotly_chart(box_and_whisk_ax)

