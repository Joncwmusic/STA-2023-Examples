import hypothesis_test_utils as htu
import streamlit as st
import pandas as pd

def build_2_samp_mean_htest_indep():
    st.header("The Situation")
    st.markdown("So before when were did hypothesis testing on means, we would look at a claim that would say "
                "something along the lines of: 'A car company CLAIMS their average customer has a credit score of 689.'"
                " Then, we would gather data or be given data/information like the standard deviation and mean to "
                "challenge the claim.")

    st.markdown(r"$H_0: \mu = 689$ The null hypothesis that makes a claim about the mean.")
    st.markdown(r"$H_0: \mu \ne 689$ The alternative hypothesis that challenges the claim.")

    st.markdown("What happens if instead of having one sample to challenge a claim, the claim itself is whether or not "
                "two groups are different. i.e. 'community college students score better in their courses than state "
                "university students.' Which might be true... I don't know... or it could be entirely fueled by biases "
                "that isn't backed up by any data. Now if I took a *sample* of community college students vs. state "
                "university students and then measured something like their GPAs, how different would they need to be "
                "to say they are or aren't the same? What if I gave each sample an exam and took their scores as my "
                r"sample? Let's say the true average scores can be represented as $\mu_1$ and $\mu_2$")

    st.markdown(r"$H_0: \mu_1 = \mu_2$")
    st.markdown(r"$H_1: \mu_1 \ne \mu_2$")

    st.markdown("Notice how I don't need specific numbers in $H_0$ or $H_1$. If both means are the same it doesn't "
                "matter if I'm saying their scores are 73 or 85 on this hypothetical exam. Just that they're the same")

    st.header("Step by Step")
    st.subheader("Set up the Hypothesis Test")
    col1tail, col2tail, col3tail = st.columns(3)

    with col1tail:
        st.markdown("**Left Tail**")
        st.markdown(r"$H_0: \mu_1 = \mu_2$")
        st.markdown(r"$H_1: \mu_1 < \mu_2$")
    with col2tail:
        st.markdown("**Right Tail**")
        st.markdown(r"$H_0: \mu_1 = \mu_2$")
        st.markdown(r"$H_1: \mu_1 > \mu_2$")
    with col3tail:
        st.markdown("**Two Tail**")
        st.markdown(r"$H_0: \mu_1 = \mu_2$")
        st.markdown(r"$H_1: \mu_1 \ne \mu_2$")

    st.subheader("Determine your alpha")
    st.markdown("Your alpha is usually given by the problem but if it isn't 0.05 is a good rule of thumb unless you "
                "need more or less scrutiny.")

    st.subheader("Compute your Test Statistic")
    st.markdown("The formula for the test statistic for 2 independent means is: ")
    st.markdown(r"$t_0 = \dfrac{\bar{x}_1 - \bar{x}_2}{\sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}}$")

    st.markdown("If you have access to a TI84 then you could just use `2-SampTTest` and plug in the values.")

    st.subheader("Compute the p value")
    st.markdown("The p value is basically the probability of getting your test statistic or worse. So that's ")
    st.markdown(r"$Pr(t > t_0), Pr(t < t_0), \text{ or } 2Pr(t > |t_0|)$ depending on the tail of your test. This is "
                r"taken care of by your calculator as the letter `p` in your output.")

    st.subheader("Make a Conclusion")
    st.markdown("And like normal if we set up our test correctly we can get to a conclusion. If the p is low, we reject"
                " the $H_0$")