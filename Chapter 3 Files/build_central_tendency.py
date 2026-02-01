import streamlit as st
import pandas as pd
import plotly.express as px

import util_functions as uf


def build_central_tendency_tab():
    example_data = [4, 7, 10, 12, 12, 12, 15, 16, 17, 17, 18, 19, 20, 21, 25]

    st.title("Measures of Central Tendency")
    st.header("Arithmetic Mean (Average)")
    st.text("The arithmetic mean is a simple sum of all the data points after which you just have to divide that "
            "sum by the number of data points to get your final number. Regardless of if you're measuring the mean "
            "of a sample or a population, it is calculated the same way.")

    st.header("Median")
    st.text("To find the median of a data set you just need to first SORT the data and then pick the middle number. "
            "If the number of items in the data set is even then take the average of the middle two numbers. ")

    st.header("Mode")
    st.text("The mode just refers to the most often observation. If there is no duplicate data points, we say the data "
            "set has no mode.")

    st.header("Example")
    st.text("So let's look at a specific data set.")
    st.dataframe(example_data)

    numerator_list = []
    denominator = str(len(example_data))
    for idx, num in enumerate(example_data):
        if idx < len(example_data) - 1:
            numerator_list.append(str(num))
            numerator_list.append('+')
        else:
            numerator_list.append(str(num))
    mean_latex_string = r"\dfrac{" + "".join(numerator_list) + "}{" + denominator + "} = " + str(uf.get_arithmetic_mean(example_data))

    st.text("Mean: ")
    st.latex(mean_latex_string)

    st.text("Median: " + str(uf.get_median(example_data)))

    st.text("Mode: " + str(uf.get_mode(example_data)))

    st.header("Now You Try")
    st.text("input your dataset here (make sure to separate each number with a comma:")
    user_data_string = st.text_input("Your Data", "Input your number list here")

    try:
        user_data_list = uf.string_to_list(user_data_string)

        user_numerator_list = []
        user_denominator = str(len(user_data_list))
        for idx, num in enumerate(user_data_list):
            if idx < len(user_data_list) - 1:
                user_numerator_list.append(str(num))
                user_numerator_list.append('+')
            else:
                user_numerator_list.append(str(num))
        user_mean_latex_string = r"\dfrac{" + "".join(user_numerator_list) + "}{" + user_denominator + "} = " + str(
            uf.get_arithmetic_mean(user_data_list))

        st.text("Mean: ")
        st.latex(user_mean_latex_string)

        st.text("Median: " + str(uf.get_median(user_data_list)))

        st.text("Mode: " + str(uf.get_mode(user_data_list)))
    except:
        st.text("It seems the number list you've input is invalid. Please input a comma separated number list.")



    st.header("Grouped Data")
    st.text("Grouped data works differently. We approximate the mean by using class midpoints and multiply each "
            "frequency by the midpoints and divide by the sum of all the frequencies. You can think of this as a weighted mean")

    grouped_data = {"class":["0-49.99","50-99.99", "100-149.99", "150-199.99", "200-249.99", "250-299.99"]
        , "midpoint":[25, 75, 125, 175, 225, 275], "frequency":[5, 9, 12, 15, 5, 2]}

    grouped_data_df = pd.DataFrame(grouped_data)
    grouped_data_df["x_i*f_i"] = grouped_data_df["midpoint"]*grouped_data_df["frequency"]

    st.dataframe(grouped_data_df)

    st.text("From here it's a matter of adding all of the items in the product column (x_i*f_i) and dividing by the"
            " sum of the frequencies i.e.")

    st.markdown(r'''$$ \mu = \dfrac{\sum x_i f_i}{\sum f_i} = \dfrac{125+675+1500+2625+1125+550}{5+9+12+15+5+2} = \dfrac{6600}{48} = 137.5$$''')
    st.header("Formulas")
    st.markdown(r"""

Population Mean and Standard Deviation:

$$\mu = \dfrac{\sum x_i}{N} \hspace{50pt} \sigma = \sqrt{\dfrac{\sum (x_i - \mu ) ^2}{N}}$$

Sample Mean and Standard Deviation:

$$\bar{x} = \dfrac{\sum x_i}{N} \hspace{50pt} s = \sqrt{\dfrac{\sum (x_i - \bar{x}) ^2}{N -1}}$$

Grouped Data Population Mean and Standard Deviation:

$$ \mu = \dfrac{\sum x_i f_i}{\sum f_i} \hspace{50pt} \sigma = \sqrt{\dfrac{\sum (x_i - \mu ) ^2f_i}{\sum f_i}}$$

Grouped Data Sample Mean and Standard Deviation:

$$ \bar{x} = \dfrac{\sum x_i f_i}{\sum f_i} \hspace{50pt} s = \sqrt{\dfrac{\sum (x_i - \bar{x} ) ^2f_i}{(\sum f_i) -1}}$$

Weighted Mean:

$$\dfrac{\sum x_i w_i}{\sum w_i}$$

z-score for Data from Population and Sample:

$$z=\dfrac{x-\mu}{\sigma} \hspace{50pt} z=\dfrac{x-\bar{x}}{s}$$""")

