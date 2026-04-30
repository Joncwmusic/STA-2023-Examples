import hypothesis_test_utils as htu
import streamlit as st
import pandas as pd

def build_2_prop_htest():
    st.header("The Situation")
    st.markdown("Let's say you're conducting a political survey on certain issues where you classify people by their "
                "party affiliation. In that survey your responses could be agree or disagree on a certain topic. For "
                "this particular survey ou find 68 percent of republicans agree while 72 percent of democrats agree. "
                "Is that a statistically significant enough difference?")

    st.markdown("Well it depends on how many people you surveyed. If you interviewed 25 republicans and 25 democrats "
                "that means 17 out of 25 republicans and 18 out of 25 democrats agree. That's a 1 person difference "
                "which may not be statistically significant enough. However, if you interviewed 3211 republicans and "
                "3572 democrats. You might have more evidence to suggest there is a statistical difference.")

    st.markdown("If we remember, from chapter 10, hypothesis tests on one proportion we would assume the proportion "
                "was the value claimed by some person or organization and then collect a sample to challenge the claim "
                "that we're assuming to be true. If the sample we collect is too unlikely to get at random, then we "
                "have evidence to reject the original claim.")

    st.markdown("So with that framework translating from one sample to two samples is basically changing the claim "
                "from 'This value is exactly $p_0$' to 'the value from group 1, $p_1$, is the same as the value from "
                "group 2, $p_2$.'")

    st.subheader("One Prop to Two Prop Language")
    col1_prop, col2_prop = st.columns(2)

    with col1_prop:
        st.subheader("One Prop")
        st.markdown("Is there evidence to suggest the true proportion is greater than 50%?")
        st.markdown("Is the percentage of yes responses different from 11%?")
    with col2_prop:
        st.subheader("Two Props")
        st.markdown("Is there evidence to suggest both groups are different?")
        st.markdown("Does the data suggest group A has a higher error rate than group B?")

    st.header("Step by Step")
    st.subheader("Set up the Hypothesis Test")
    col1tail, col2tail, col3tail = st.columns(3)

    with col1tail:
        st.markdown("**Left Tail**")
        st.markdown(r"$H_0: p_1 = p_2$")
        st.markdown(r"$H_0: p_1 < p_2$")
    with col2tail:
        st.markdown("**Right Tail**")
        st.markdown(r"$H_0: p_1 = p_2$")
        st.markdown(r"$H_0: p_1 > p_2$")
    with col3tail:
        st.markdown("**Two Tail**")
        st.markdown(r"$H_0: p_1 = p_2$")
        st.markdown(r"$H_0: p_1 \ne p_2$")

    st.subheader("Determine your alpha")
    st.markdown("Your alpha is usually given by the problem but if it isn't 0.05 is a good rule of thumb unless you "
                "need more or less scrutiny.")

    st.subheader("Compute your Test Statistic")
    st.markdown("The formula for the test statistic for 2 independent means is: ")
    st.markdown(r"$z_0 = \dfrac{\hat{p}_1 - \hat{p}_2}{\sqrt{\hat{p}(1-\hat{p})} \sqrt{\dfrac{1}{n_1} + \dfrac{1}{n_2}}}$")
    st.markdown(r"Where $\hat{p}_1$ and $\hat{p}_2$ are your point estimates for the proportions of each group, "
                r"$\hat{p}$ is the pooled proportion for both groups and $n_1$, $n_2$ are the sample sizes for group 1 "
                r"and group 2, respectively.")
    st.markdown("If you have access to a TI84 then you could just use `2-PropZTest` and plug in the values.")

    st.subheader("Compute the p value")
    st.markdown(r"$Pr(z > z_0), Pr(z < z_0), \text{ or } 2Pr(z > |z_0|)$ depending on the tail of your test. This is "
                r"taken care of by your calculator as the letter `p` in your output.")

    st.subheader("Make a Conclusion")
    st.markdown("And just like with 1 sample, if we set up our test correctly we can get to a conclusion. If the p is low"
                ", we reject the $H_0$")