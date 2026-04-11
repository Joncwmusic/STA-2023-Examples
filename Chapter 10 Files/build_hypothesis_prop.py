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

def build_hypothesis_prop():

    sample_vs_pop_prop = {"Ads":["Without Owners", "With Owners"],"Results":[4/100, 56/850]}
    example_prop_df = sample_vs_pop_prop

    p_hat = 56/850
    sigma_p_hat = math.sqrt((0.04)*(0.96)/850)
    test_stat = (p_hat - 0.04)/sigma_p_hat

    # normal line data
    x_values_full = [i/50 for i in range(-200, 200)]
    x_values_left = [i / 50 for i in range(-200, -50)]
    x_values_right = [i / 50 for i in range(80, 200)]

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
    normal_line_fig_right.add_vline(x=3.85, line_width=2, line_dash="dash", line_color="green")
    normal_line_fig_left = px.line(data_frame=normal_full_line_df, x="x_val", y="y_val")
    normal_line_fig_left.add_scatter(x=normal_left_area_df['x_val']
                                , y=normal_left_area_df['y_val']
                                , fill='tozeroy', showlegend=False)
    normal_line_fig_both = px.line(data_frame=normal_full_line_df, x="x_val", y="y_val")
    normal_line_fig_both.add_scatter(x=normal_both_tail_df['x_val']
                                     , y=normal_both_tail_df['y_val']
                                     , fill='tozeroy', showlegend=False)

    st.header("Hypothesis Testing for a Proportion")
    st.markdown("When testing a hypothesis on the population proportion, the idea is assuming the null hypothesis $H_0$"
                " is true, then getting a proportion from a random sample. The rest is determining how likely "
                "getting the proportion for you sample is if the null is in fact true. If that probability is low, "
                "or the z score for your sample prop is way too high or low, you can say 'hmm... it seems impossibly "
                "unlikely I would get this sample average from the population, maybe I should challenge my assumption "
                "and reject the $H_0$'")

    st.markdown("Let's start with an example. Suppose you're launching a new marketing campaign for your 'uggs but for "
                "dogs' brand and you want to test if ads that include the pets' owners are better than just featuring "
                "the product itself. So you, with a current benchmark of a 4% click through rate on your ad want to "
                "know if these new ads will perform substantially better. And when you test these ads on 850 potential "
                "customers you get 56 that decide to click. Not bad.")


    st.dataframe(example_prop_df)
    st.markdown("**Current CTR**: " + str(0.040))
    st.markdown("**New CTR**: " + str(round(56/850, 3)))
    st.markdown("But now you have an issue. How do you know this wasn't a fluke? This is where the hypothesis testing "
                "thing we've been talking about comes in handy. Essentially you want to find the probability you could "
                "get a 6.6% conversion rate or higher assuming it was supposed to be 4% to begin with. (I would like "
                "to point out here that in practice most companies take the point estimate values and roll with it "
                "instead of verifying statistical significance even if the sample sizes are super small).")

    st.header("Setting Up the Hypothesis Test")
    st.markdown("First you must determine your hypothesis setup. You start with assuming that your. But "
                "you're claiming instead that the average is higher that your salary. This mean your null and "
                "alternative look like this: ")
    st.markdown(r"$H_0: p = 0.04$")
    st.markdown(r"$H_1: p > 0.04$")

    st.markdown("For the sake of removing doubt let's say we're operating on 95% confidence or a significance level of "
                "0.05.")

    st.markdown("Lastly, let's get the point estimate for the proportion:")
    st.markdown(r"$\hat{p} = " + str(round(56/850, 4)) + "$")

    st.header("Getting a Test Statistic")

    st.markdown("The test statistic for the mean is as follows:")
    st.markdown(r"$z_0 = \dfrac{\hat{p} - p}{\sqrt{\dfrac{p(1-p)}{n}}}$")
    st.markdown("This may look familiar as it is basically the z score of the sample mean. Now let's plug in all of "
                "our values:")
    st.markdown(r"$z_0 = \dfrac{\hat{p} - p}{\sqrt{\dfrac{p(1-p)}{n}}} \Rightarrow \dfrac{0.066 - 0.04}"
                r"{\sqrt{\dfrac{(0.04)(0.96)}{850}}} = " + str(round(test_stat, 4)) + "$")

    st.header("Classical Approach")

    st.markdown(r"When using the classical approach you need to compare your test statistic to the critical value. You "
                r"can find a critical value by using `invNorm(area, 0, 1)` where the area is your alpha For a left tail"
                r" test use area = alpha, right tail use area = 1-alpha, and for a 2 tail test use alpha/2 and take "
                r"both the positive and negative values.")
    st.markdown("NOTE: If you have a TI84+CE then ignore manipulating alpha and just use LEFT and RIGHT. You still "
                "have to cut alpha in half for 2 tails.")

    st.markdown("If you aren't using a computer to do this for you, you can use a z table to get the critical value. "
                "For a right tail test with alpha = 0.05 the critical value is is ~1.645")

    st.plotly_chart(normal_line_fig_right, key="right tail t")

    st.markdown("**The Key Idea:** If the test statistic is beyond the red boundary based on your critical value, this "
                "is when you reject the null hypothesis.")

    col1_crit, col2_crit = st.columns(2)

    with col1_crit:
        st.markdown(r"""
        One Tail Critical Value Z Scores:
        
        - 90% Confidence $z_{\alpha} = z_{0.1} = 1.28$
        - 95% Confidence $z_{\alpha} = z_{0.05} = 1.645$
        - 99% Confidence $z_{\alpha} = z_{0.01} = 2.32$
        """)
    with col2_crit:
        st.markdown(r"""
        Two Tail Critical Value Z Scores:
    
           - 90% Confidence $z_{\alpha / 2} = z_{0.05} = 1.645$
           - 95% Confidence $z_{\alpha / 2} = z_{0.025} = 1.96$
           - 99% Confidence $z_{\alpha / 2} = z_{0.005} = 2.576$
           """)

    st.header("P Value Approach")

    st.markdown("When using the p value approach you still must compute the test statistic but instead of comparing it "
                "to a critical value, you can compute the probability of getting that proportion or worse against the "
                "significance level. So for our example compute $Pr(z>3.85)$ which is `normalcdf(3,85, 10000, 0, 1)` "
                "remember since this is a z-score that means your mean and standard deviation are 0 and 1. This will "
                r"give you can absurdly small probability (0.0001) which is far less than our $\alpha$ = 0.05.")

    st.header("In Summary:")
    st.markdown(r"""
        * Define your hypothesis type and get your variables
        * Get a significance level $\alpha$ or a critical value
        * Get a test statistic based on your data
        * Compare:
            * Compare the test statistic to your critical value OR
            * Compare the p value of the test statistic to the significance level
        """)