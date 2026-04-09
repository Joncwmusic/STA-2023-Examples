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

def build_hypothesis_mean():

    salary_data = [84200, 64800, 72000, 104250, 109000, 68500, 125000, 69900, 99800, 87500, 78900, 85000, 36500, 127000]

    salary_mean = sum(salary_data)/len(salary_data)
    salary_deviations = [(i - salary_mean)**2 for i in salary_data]
    salary_ssd = math.sqrt(sum(salary_deviations)/(len(salary_deviations)-1))
    test_stat = (salary_mean - 64700)/(salary_ssd/math.sqrt(14))


    # normal line data
    x_values_full = [i/50 for i in range(-200, 200)]
    x_values_left = [i / 50 for i in range(-200, -50)]
    x_values_right = [i / 50 for i in range(125, 200)]

    normal_full_line = [normpdf(mu=0, sigma=1, x=i) for i in x_values_full]
    normal_left_area = [normpdf(mu=0, sigma=1, x=i) for i in x_values_left]
    normal_right_area = [normpdf(mu=0, sigma=1, x=i) for i in x_values_right]
    normal_both_area = [normpdf(mu=0, sigma=1, x=i) if (i > 2 or i < -2) else 0 for i in x_values_full ]

    normal_full_line_df = pd.DataFrame({"x_val":x_values_full,"y_val":normal_full_line})
    normal_left_area_df = pd.DataFrame({"x_val": x_values_left, "y_val": normal_left_area})
    normal_right_area_df = pd.DataFrame({"x_val": x_values_right, "y_val": normal_right_area})
    normal_both_tail_df = pd.DataFrame({"x_val": x_values_full, "y_val": normal_both_area})

    normal_line_fig_right = px.line(data_frame=normal_full_line_df, x="x_val", y="y_val")
    normal_line_fig_right.add_scatter(x=normal_right_area_df['x_val']
                                     , y=normal_right_area_df['y_val']
                                     , fill='tozeroy', showlegend=False)
    normal_line_fig_right.add_vline(x=3.3, line_width=2, line_dash="dash", line_color="green")
    normal_line_fig_left = px.line(data_frame=normal_full_line_df, x="x_val", y="y_val")
    normal_line_fig_left.add_scatter(x=normal_left_area_df['x_val']
                                , y=normal_left_area_df['y_val']
                                , fill='tozeroy', showlegend=False)
    normal_line_fig_both = px.line(data_frame=normal_full_line_df, x="x_val", y="y_val")
    normal_line_fig_both.add_scatter(x=normal_both_tail_df['x_val']
                                     , y=normal_both_tail_df['y_val']
                                     , fill='tozeroy', showlegend=False)

    st.header("Hypothesis Testing for a Mean")
    st.markdown("When testing a hypothesis on the population mean, the basic idea is assuming the null hypothesis $H_0$"
                " is true, then gathering a sample and finding a sample mean. The rest is determining how likely "
                "getting the mean for you sample is if the null is in fact true. If that probability is low (p value), "
                "or the z score for your sample mean is beyond a certain value (classical method) you can say 'hmm... "
                "it seems impossibly unlikely I would get this sample average from the population, maybe I should "
                "challenge my assumption and reject the $H_0$'")

    st.markdown("Let's start with an example. Suppose you're arguing with your boss asserting that you are underpaid "
                "and are *this* close to becoming a proletariat hell bent on overthrowing your capitalist oppressor. "
                "Your boss; however, says your wage is the market rate. So you go to LinkedIn and message a random "
                "sample of people with our same job title in your industry and intrusively ask how much they make.")

    st.dataframe(salary_data)
    st.markdown("**The Average Salary**: " + str(round(salary_mean,2)))
    st.markdown("**Your Salary**: 65700... oof")
    st.markdown("You bring this data to your boss and he says 'that sample is random and you could've easily gotten "
                "any other average that would be below your salary.' This is a fair point, but you, stubborn, and "
                "feeling incredibly dejected from the remark, now need to convince you boss that the chance your sample"
                " overestimates to the degree by which it does is so unlikely given his other statement that you are "
                "paid MARKET rate. This is where the hypothesis test comes in.")

    st.header("Setting Up the Hypothesis Test")
    st.markdown("First you must determine your hypothesis setup. Your boss has claimed your salary is the average. But "
                "you're claiming instead that the average is higher that your salary. This mean your null and "
                "alternative look like this: ")
    st.markdown(r"$H_0: \mu = 65700$")
    st.markdown(r"$H_1: \mu > 65700$")

    st.markdown("For the sake of removing doubt let's say we're operating on 99% confidence or a significance level of "
                "0.01.")

    st.markdown("Lastly, let's get the point estimates for the mean and standard deviation:")
    st.markdown(r"$\bar{x} = " + str(round(salary_mean,2)) + "$")
    st.markdown(r"$s_x = " + str(round(salary_ssd,2))+ "$")

    st.header("Getting a Test Statistic")

    st.markdown("The test statistic for the mean is as follows:")
    st.markdown(r"$t_0 = \dfrac{\bar{x} - \mu}{\dfrac{s}{\sqrt{n}}}$")
    st.markdown("This may look familiar as it is basically the z score of the sample mean. Now let's plug in all of "
                "our values:")
    st.markdown(r"$t_0 = \dfrac{\bar{x} - \mu}{\dfrac{s}{\sqrt{n}}} \Rightarrow \dfrac{86596.43 - 65700}"
                r"{\dfrac{24756}{\sqrt{14}}} = " + str(round(test_stat,4)) + "$")

    st.header("Classical Approach")

    st.markdown(r"When using the classical approach you need to compare your test statistic to the critical value. You "
                r"can find a critical value by using `invT(area, df)` where the area is your alpha and df is the "
                r"degrees of freedom which is your sample size minus 1. For a left tail test use area = alpha, right "
                r"tail use area = 1-alpha, and for a 2 tail test use alpha/2 and take both the positive and negative "
                r"values.")

    st.markdown("If you aren't using a computer to do this for you, you can use a t table with common alpha values and "
                "estimate for various degrees of freedom. The critical value for a right tail test with alpha = 0.01 "
                "and degrees of freedom of 13 is ~2.65")

    st.plotly_chart(normal_line_fig_right, key = "right tail t")

    st.markdown("Now all you have to do is compare the test statistic to the critical value. Turns out 3.3 is in fact "
                "bigger than 2.65, so the assumption that you pay is market rate is likely wrong and you can tell your "
                "boss to shove it before he fires you. But you can hold your head high knowing you are right.")

    st.header("P Value Approach")

    st.markdown("The p value approach is a little different. It asks the question 'how likely is it to get your average"
                " or worse given your assumed average?' You still need the test statistic but now you compute "
                "$Pr(t>3.31)$ which is... low (0.0028). Since it's lower than 0.01, it seems like your boss is "
                "doubly wrong.")

    st.header("In Summary:")
    st.markdown(r"""
    * Define your hypothesis type and get your variables
    * Get a significance level $\alpha$ or a critical value
    * Get a test statistic based on your data
    * Compare:
        * Compare the test statistic to your critical value OR
        * Compare the p value of the test statistic to the significance level
    """)
