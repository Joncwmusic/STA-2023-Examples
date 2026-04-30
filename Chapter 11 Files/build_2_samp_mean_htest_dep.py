import random

import hypothesis_test_utils as htu
import streamlit as st
import pandas as pd

def build_2_samp_mean_htest_dep():

    random_dataset_1 = [30.1, 20.2, 12.4, 14.6, 34.2, 28.1, 39.3, 10.1, 34.9, 42.9, 29.1, 10.3, 31.4, 53.2, 42.1, 11.7]
    random_dataset_2 = [round(0.95*random.choice([0.91, 0.95, 0.99, 1.03, 1.07, 1.1])*i, 1) for i in random_dataset_1]

    example_data = pd.DataFrame({"Before":random_dataset_1, "After":random_dataset_2})
    example_data_diff = example_data.copy()
    # example_data_diff["Differences"] = example_data_diff["Before"] - example_data_diff["After"]

    example_data_diff['Differences'] = example_data_diff["Before"] - example_data_diff["After"]

    st.header("The Situation")
    st.markdown("Instead of 2 independent samples, sometimes we need to look at samples that involve before and afters "
                "or matched pairs of subjects. For example. You might believe a certain weight loss protocol works and "
                "you decide to test it on 20 people and measure their weight before and after, the '2 samples' are the "
                "before measurements and the after measurements which are MATCHED by each person.")

    st.markdown("This means that instead of comparing the before mean and the after mean, what we should be looking at "
                "is the *DIFFERENCES* between both and then challenge the claim that there is no difference i.e.")
    st.markdown(r"$\mu_d = \mu_1 - \mu_2$")

    st.markdown(r"$H_0: \mu_d = 0$")
    st.markdown(r"$H_1: \mu_d \ne 0$")

    st.markdown("Notice how this time the null difference is 0. I would like to point out that the process for getting "
                r"this $\mu_d$ is actually by subtracting the 2 data points for each matched pair and then using the "
                "differences as a single dataset and treating it like a 1 sample hypothesis test. Here's what that "
                "looks like in practice:")

    st.subheader("The Data")
    st.markdown("The first column is the before column and the second column is our after.")
    st.dataframe(example_data)

    st.markdown("When we subtract column 2 from column 1, we get a third column with the differences.")
    st.dataframe(example_data_diff)

    st.markdown("So now the question we ask is this: Does the 3rd column of data showing the differences provide "
                "sufficient evidence to suggest there is a difference between the before and after?")

    st.header("Step by Step")
    st.subheader("Set up the Hypothesis Test")

    st.markdown(r"Nothing really changes from a normal 1 mean hypothesis test aside from using $\mu_d$ as your mean to "
                r"test.")
    col1tail, col2tail, col3tail = st.columns(3)

    with col1tail:
        st.markdown("**Left Tail**")
        st.markdown(r"$H_0: \mu_d = 0$")
        st.markdown(r"$H_1: \mu_d < 0$")
    with col2tail:
        st.markdown("**Right Tail**")
        st.markdown(r"$H_0: \mu_d = 0$")
        st.markdown(r"$H_1: \mu_d > 0$")
    with col3tail:
        st.markdown("**Two Tail**")
        st.markdown(r"$H_0: \mu_d = 0$")
        st.markdown(r"$H_1: \mu_d \ne 0$")

    st.subheader("Determine your alpha")
    st.markdown("Your alpha is usually given by the problem but if it isn't 0.05 is a good rule of thumb unless you "
                "need more or less scrutiny.")

    st.subheader("Compute your Test Statistic")
    st.markdown("The formula for the test statistic for 2 dependent means is: ")
    st.markdown(r"$t_0 = \dfrac{\bar{x}_d - 0}{\dfrac{s_d}{\sqrt{n}}}$")
    st.markdown(r"Where $n$ is the number of pairs in your sample, $s_d$ is the sample standard deviation of the "
                r"differences, and $\bar{x}_d$ is the sample mean of the differences.")

    st.markdown("If you have access to a TI84 then you would use `TTest` and instead of using the stats input you'd "
                "instead use the data input after calculating the difference list from L1 and L2 and putting it into "
                "L3.")

    st.subheader("Compute the p value")
    st.markdown("The p value is basically the probability of getting your test statistic or worse. So that's ")
    st.markdown(r"$Pr(t > t_0), Pr(t < t_0), \text{ or } 2Pr(t > |t_0|)$ depending on the tail of your test. This is "
                r"taken care of by your calculator as the letter `p` in your output.")

    st.subheader("Make a Conclusion")
    st.markdown("And like normal if we set up our test correctly we can get to a conclusion. If the p is low, we reject"
                " the $H_0$")