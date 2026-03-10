import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random
from streamlit.components.v1 import html as sthtml
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import matplotlib.patches as patches
from itertools import permutations, combinations


def build_combination_permutation():

    st.header("Multiplication Rule (for counting)")

    st.markdown("It's date night with your pookie. You've had a rocky relationship because you haven't taken enough "
                "accountability to seek out a therapist, and your partner thinks the only way to show affection is "
                "through material actions because 'gift giving is his or her love language' and you're the one giving. "
                "You decide to take your partner out to a fancy 4 course dinner instead of confronting your issues."
                "You have a few options for your dinner: 6 appetizers, 2 salads, 4 entrees, and 3 desserts. "
                "How many different you start considering all of your parallel universe selves and think 'how "
                "many different dinner combinations are actually possible with this menu?")

    st.markdown("The answer is 144. But how did we get there?")

    st.markdown("If you have $k$ choices each with $p_1$, $p_2$, ... $p_k$ options for each choice then the "
                r"total number of options is ")

    st.markdown(r"$$n = p_1 \cdot p_2 \cdot ... \cdot p_k$$")

    st.markdown("In other words: You take the number of options for each choice and multiply it all together.")

    st.subheader("Passwords")
    st.markdown("Suppose you need a new password because 'corgi123' just isn't secure enough to keep yourself safe "
                "from phishing scams (a more secure password will not keep you from giving it away to scammers). The "
                "requirements are as follows: you can use any letters uppercase or lowercase and any digits 0-9 but "
                "it must be 10 characters. How many different passwords could you make?")

    st.subheader("Some Options")
    st.dataframe(["password01", "youCanTry9", "TryHackMe7", "PlzNoSt3aL", "Corgi12345", "StAtIsTiCs"])

    st.markdown("If you're a hacker, you care about this question because you want to know if it's worth it to brute "
                "force guess every password. But let's think about the problem like before. You have 26 uppercase "
                "letters, 26 lowercase letters, and 10 digits total. So for a single character of your password, "
                "you have 26 + 26 + 10 = 62 options. Then you have that many options for the second character. "
                "If you remember our multiplication rule that means for just the first 2 characters that's 62 times 62 "
                r"possibilities... that's 3844. If we repeat this logic, that's $62^{10}$ total passwords.")

    st.markdown("")

    st.header("Permutations")

    st.markdown("Okay let's look at another type of counting problem:")
    st.markdown("You have a bunch of probability textbooks like 8 of them because you have a master's in math "
                "and an interest in AI and machine learning. How many ways could you arrange these books on your "
                "bookshelf. In this case the order by which you arrange your books matters.")

    st.markdown("Now think. 'How many options do I have for my first book?' The answer is 8. But then after you pick "
                "the first book how many options do you have for the second book? Is it still 8? No. It's 7 because "
                "you already picked the first book. Then next is 6 and so on until you have only one option "
                "left. So using our multiplication rule our number of arrangements n is:")

    st.markdown(r"$$n = 8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 $$")

    st.markdown("This type of thing is so common we use a special symbol '!' which is called a 'factorial' which "
                r"represents the descending product of integers from a number. So, $6! = 6 \cdot 5 \cdot 4 \cdot "
                r"3 \cdot 2 \cdot 1 \cdot$")

    st.markdown("Okay let's change the problem a little bit. Now you find out your shelf only has 5 spaces. So 3 books "
                "need to go. How many arrangements of 5 can you make from 8 possible books? Well the logic is largely "
                "the same but you cut it off at 5 spaces. So instead you compute the following:")

    st.markdown(r"$$n = 8 \cdot 7 \cdot 6 \cdot 5 \cdot 4$$")
    st.markdown("Notice how if I were to just write $8!/3!$ this would be the same as the above product because the "
                "3, 2, and 1 all cancel. In fact we can generalize this as a formula as follows:")

    st.markdown(r"$$_nP_r = \dfrac{n!}{(n-r)!}$$")

    st.markdown("You can think of permutations as how many ways you can pick and shuffle r things from n things.")

    st.header("Combinations")

    st.markdown("Now let's change the problem one more time. You need to lend the books to your friend. He does not "
                "care what order you hand over the books but he needs 5 of your 8 statistics books for his actuary "
                "exams and he promises once he gets a job he'll give them back. Since the order doesn't matter you can "
                "take all the arrangements of 5 books from 8 and divide out all the arrangement of the 5 books as they "
                "are irrelevant. So, it's ")

    st.markdown(r"$$_nC_r = \dfrac{8!}{(8-5)!} \div 5! = \dfrac{8!}{3!5!}$$")

    st.markdown("Notice how both denominator factors add to get the numerator. The formula in general is:")

    st.markdown(r"$$_nC_r = \dfrac{n!}{(n-r)!r!}$$")

    st.markdown("With combinations you might want to think 'I have 10 things to do but I need to get 3 done today "
                "but it doesn't matter how they get done' or maybe think of committee members that all have equal say "
                "so whether someone is the first committee member or the second member doesn't really matter.")

    st.header("Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Combinations")
        st.markdown(r"$$_nC_r = \dfrac{n!}{(n-r)!r!}$$")
        st.markdown("- Order does not matter")
        st.markdown("- Think electing 2 people to a committee")
        st.markdown("- Divides out the extra r!")

    with col2:
        st.subheader("Permutations")
        st.markdown(r"$$_nP_r = \dfrac{n!}{(n-r)!}$$")
        st.markdown("- Order matters")
        st.markdown("- Think electing President and VP for a club")

    with col3:
        st.subheader("Other")
        st.markdown(r"$$n = p_1 \cdot p_2 \cdot ... \cdot p_k$$")
        st.markdown("- Not about order, but options")
        st.markdown("- Think about the number of steps and options per step.")
        st.markdown("- Can it be reframed as a password problem?")
