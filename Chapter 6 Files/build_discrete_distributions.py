import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio

def build_discrete_probaility_distributions():
    example_df = pd.DataFrame({"X": [0, 1, 2, 3], "Pr(X)": [0.05, 0.25, 0.55, 0.15]})
    example_dice_df = pd.DataFrame({"Roll": [1, 2, 3, 4, 5 ,6], "Pr(X = Roll)": [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]})
    example_casino_df = pd.DataFrame({"Outcomes": ["17 Black", "Everything Else"]
                                            , "Payout": [350,-10]
                                            , "Pr(Outcome)": [1/38, 37/38]})
    example_lottery_df = pd.DataFrame({"Outcomes": ["5 correct", "4 correct", "3 correct", "2 correct", "1 correct", "0 correct"]
                                        , "Payout": [9999990, 4990, 490, 40, -10, -10]
                                       , "Pr(Outcome)": [0.0000004, 0.00009, 0.00416,0.06239, 0.34315, 0.59021]})

    st.header("Discrete Random Variables")
    st.markdown("Discrete data is 'countable'. Halves, decimals, and pi aren't real in the discrete world. In other "
                "words you can't infinitely subdivide whatever your measuring like you would with measurements like "
                "height or speed where you can be 183.267 cm tall or drive 98.791 km per hour. there's a semantic "
                "argument to be made about measurement accuracy but the point is discrete and continuous (that's "
                "next chapter) measurements usually follow different rules. Let's look at some examples.")

    st.subheader("Examples")
    st.markdown("Below is a discrete probability distribution. This one represents a die roll and the numerical "
                "outcomes with their probabilities. They are all 1/6 (of course assuming a fair die) and we can use "
                "this distribution to get an expectation for what we should get on average after several rolls.")

    st.dataframe(example_dice_df)

    st.markdown("To demonstrate expectation we'll stick with a simpler distribution with values 0 through 3 with "
                "differing probabilities.")

    st.dataframe(example_df)

    example_df["x * Pr(x)"] = example_df["X"]*example_df["Pr(X)"]
    example_df_with_product = example_df.copy()

    st.markdown("To calculate expected value, all we have to do is multiply our values with the probabilities and "
                "add them to compute expected value. It says so in this formula:")

    st.markdown(r"$$\mu_{X} = \sum x_{i}Pr(x_i)$$")

    st.dataframe(example_df_with_product)

    st.markdown("When we add up those values in the xPr(x) column we should get $1.8$ which looks like it'd be about "
                "the right value. Like we 'expected' it to be... wowzers")

    st.header("Finding Mean (Expected Value) and Standard Deviation")

    st.markdown(r"If you look at that formula you might not think it looks that familiar, but that $\mu$ should look "
                r"very familiar. In fact the mean and expected value can be used fairly interchangeably in this context"
                r". Standard deviation is also similarly defined and so if you're thinking 'okay how do I do this in "
                r"my calculator' it's the same as in the chapter 3 notes: 1 Var Stats with the probabilities being "
                r"your 'weights' for your FreqList parameter.")

    st.markdown(r"$$\mu_{X} = \sum x_{i}Pr(x_i) \hspace{50pt} \sigma_X = "
                r"\sqrt{\sum (x_i -\mu_X)^2 Pr(x_i)} $$")
    st.markdown(r"$$\mu = \dfrac{\sum x_{i} w_{i}}{\sum w_{i}} \hspace{50pt} "
                r"\sigma = \dfrac{\sqrt{\sum (x_i-\mu)^2 w_i}}{\sum w_i} $$")

    st.subheader("Let it Ride")

    st.markdown("You're at the casino. You're betting it all on 17 black. And by 'all' I mean 10 dollars. But this "
                "means you only have a 1 in 38 chance to win. That's not good, but the payout is 360 dollars (minus "
                "the 10 dollars you put in). Given the odds and the payout, is it worth it to play this roulette game?")

    st.dataframe(example_casino_df)

    st.markdown("The math works out to no.")
    st.markdown(r"$$ x * \sum Pr(x) = (350)(\dfrac{1}{38}) + (-10)(\dfrac{37}{38}) = -0.526 $$")
    st.markdown("This means if you played roulette 1000 times like this you'd **on average** lose 52 cents per spin. "
                "This of course is an estimate since some gamblers do get lucky. Especially the ones that do just one "
                "more spin because most gamblers quit before they hit it big.")

    st.subheader("Is This Lottery Worth Playing?")
    st.markdown("Suppose you have a lottery with 52 numbers to choose from and you need to get 5 numbers correct to "
                "win the grand prize. As it turns out, partial credit counts as well so getting 4 or 3 numbers right "
                "gives you proportionally smaller payouts. Is this lottery with the payouts laid out as below worth "
                "playing at all?")

    st.dataframe(example_lottery_df)

    st.header("Cumulative Probability Distribution")
    st.markdown("It's not always useful to look at the probability of exactly on value. Sometimes we need to consider "
                "multiple probabilities or think about our chances of being below some maximum or above some minimum. "
                "For example, for a 10 question quiz, you'd probably want to know your odds of getting at least 7 "
                "questions right. We can add our probabilities one row at a time similar to how we computed cumulative "
                "frequency back in chapter 2 to get the **cumulative distribution**")

    example_df_cume = example_df.copy()
    example_df_cume["cdf"] = example_df_cume['Pr(X)'].cumsum()

    st.dataframe(example_df_cume)
