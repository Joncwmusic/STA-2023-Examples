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

class tree_node:
    def __init__(self, data, label = None, tier = 0, parent = None):
        self.data = data
        self.label = label
        self.left = None
        self.right = None
        self.tier = tier
        self.parent = parent

    def add_left_node(self, node_data, label):
        self.left = tree_node(node_data*self.data, label, self.tier + 1, self)

    def add_right_node(self, node_data, label):
        self.right = tree_node(node_data*self.data, label, self.tier + 1, self)

    def add_both_nodes(self, left_data, right_data, left_label, right_label):
        self.add_left_node(left_data,left_label)
        self.add_right_node(right_data, right_label)

    def build_binomial_tree(self, left_data, right_data, tiers, left_label=None, right_label=None):
        if tiers == 0:
            return self
        self.add_both_nodes(left_data, right_data, left_label, right_label)
        self.left.build_tree(left_data, right_data, tiers - 1, left_label, right_label)
        self.right.build_tree(left_data, right_data, tiers - 1, left_label, right_label)


def create_binomial_probs(num_trials, success_prob, success_label="Success", failure_label="Failure", chart_lbl="main"):
    y_coordinates = []
    x_coordinates = []
    labels = []
    point_pairs = []
    p_powers = {}
    start = 0.5
    step = 1

    ### getting coordinates and labels
    for i in range(num_trials+1):
        for j in range(2**i):
            x_coordinates.append(start + j * step)
            y_coordinates.append((num_trials - i)/2)

            if i < num_trials:
                point_pairs.append(pd.DataFrame({"x_vals":[start+j*step, start+j*step + step/4]
                                            ,"y_vals":[(num_trials - i)/2, (num_trials - (i+1))/2]}))
                point_pairs.append(pd.DataFrame({"x_vals":[start+j*step, start+j*step - step/4]
                                            ,"y_vals":[(num_trials - i)/2, (num_trials - (i+1))/2]}))

            if j%2 == 0 and i == 0:
                labels.append("Start")
            elif j%2 == 0 and i != 0:
                labels.append(failure_label)
            else:
                labels.append(success_label)
        step = step/2
        start = start/2

    print(point_pairs)
    ### getting probability powers

    p_powers[0] = [0]
    for k in range(1, num_trials):
        p_powers[k] = []
        for idx,item in enumerate(p_powers[k-1]):
            p_powers[k].append(item)
            p_powers[k].append(item+1)
            # print("Index: ", idx, "Item: ", item, "Looking at list:", p_powers[k - 1], "Current List:", p_powers[k])

    ### getting probability values
    probs_dict = {}
    for k in p_powers:
        for power in p_powers[k]:
            probs_dict[(k, power)] = round(success_prob ** power * (1 - success_prob) ** (num_trials - power),ndigits=6)

    ##### plotting the points
    coordinate_df = pd.DataFrame({"x_coord": x_coordinates, "y_coord": y_coordinates, "labels": labels})
    fig  = px.scatter(coordinate_df,x="x_coord", y="y_coord", color="labels")

    ax_list = []
    for coords in point_pairs:
        ax_list.append(px.line(data_frame=coords, x= "x_vals", y= "y_vals"))
    for line_obj in ax_list:
        trace = line_obj.data[0]
        trace.line.color = "black"
        trace.line.width = 1
        fig.add_trace(line_obj.data[0])
    st.plotly_chart(fig, key=chart_lbl)
    return None


def build_binomial_distribution():

    dataset_coinflip = [binompdf(6, 0.5, i) for i in range(7)]
    dataset_sales = [binompdf(10, 0.18, i) for i in range(11)]
    dataset_coinflip_more = [binompdf(20, 0.5, i) for i in range(21)]
    dataset_norm = [normpdf(10,math.sqrt(5),0.1*i) for i in range(200)]


    df_coinflip = pd.DataFrame({"Num Heads": range(7), "Pr(x)": dataset_coinflip})
    df_sales = pd.DataFrame({"Num Sales": range(11), "Pr(x)": dataset_sales})
    df_coinflip_more = pd.DataFrame({"Num Heads": range(21), "Pr(x)": dataset_coinflip_more})
    df_norm = pd.DataFrame({"X": [0.1*i for i in range(200)], "Norm(X)":dataset_norm})

    ax_coin = px.bar(data_frame=df_coinflip, x="Num Heads", y="Pr(x)")
    ax_sales = px.bar(data_frame=df_sales, x="Num Sales", y="Pr(x)")

    ax_more = px.bar(data_frame=df_coinflip_more, x="Num Heads", y="Pr(x)")
    ax_norm = px.line(data_frame=df_norm, x= "X", y="Norm(X)")
    ax_more.add_traces(ax_norm.data)

    st.header("The Obsession with Coin Flips")
    st.markdown("Okay I admit it...")
    st.markdown("Statisticians are obsessed with coin flips. But for good reason. Coin flips are a phenomenal way to "
                "demonstrate a special kind of discrete probability distribution, **The Binomial Distribution** "
                "Here's the scenario.")
    st.markdown("Let's say you're flipping a coin 6 times and wants to know what the chances are of getting 2 heads "
                "or maybe 5 heads. You know it's probably exceedingly rare to get 6 heads in a row before starting "
                "the experiment but how do we quantify that? Also how do we make sure we account for the difference "
                "between HHTHHT and TTHHHH? It seems different arrangements call for different probabilities... "
                "or do they?")
    st.markdown("Spoiler alert: we account for the arrangements in the formula. But first let's look at a naive method "
                "to solve this problem: the probability tree")

    create_binomial_probs(6, 0.5)

    st.markdown("So you could hand draw the above visualization and get the probabilities by tracing down a specific "
                "path down the probability tree to eventually get the probability of a specific arrangement and even "
                "try to follow all the paths that consist of flipping 3 heads. But if you change the number of trials "
                "or the probabilities of success you'll have to draw the figure all over again.")
    st.markdown("Gross.")

    st.subheader("Binomial Formula")

    st.markdown("The more elegant solution is to use this formula:")
    st.markdown(r"$$Pr(X=x) = \binom{n}{x}p^x(1-p)^{n-x}$$")
    st.markdown(r"$$Pr(X=x) = _nC_x p^x(1-p)^{n-x}$$")
    st.markdown(r"Keep in mind that $\binom{n}{x}$ is the same exact thing as $_nC_x$. This means that if you have a "
                r"binomial experiment with 15 trials, a probability of success of 0.45, and want to know the "
                r"probability of getting exactly 8 success, you would compute "
                r"$$Pr(X=8) = \binom{15}{8}(0.45)^8(0.55)^{7} = $$ " + str(binompdf(15, .45, 8)))

    st.markdown("We could do this for every value of X we can possibly have from 0 to 15. For now, let's go back to our"
                " simple example of coin flips with p = 0.5 and our number of trials, n = 6. If we were to calculate "
                "each individual probability using that formula above we would get the following table and graph. ")

    coincol1, coincol2 = st.columns(2)


    with coincol1:
        st.dataframe(df_coinflip)
    with coincol2:
        st.plotly_chart(ax_coin)

    st.header("Binomial Distribution is a Probability Distribution")
    st.markdown("Remember, binomial distribution is a probability distribution which means we can treat it like any "
                "other discrete probability distribution. In fact, we can find mean and standard deviation like we "
                "can for any weighted data. Luckily we don't have to input values in L1 and L2 in our calculators or "
                "try to compute a weighted mean after creating a table with all the probabilities.")

    sales_col1, sales_col2 = st.columns(2)

    with sales_col1:
        st.dataframe(df_sales)
    with sales_col2:
        st.plotly_chart(ax_sales)

    st.subheader("Finding Mean and Standard Deviation")
    st.markdown("To calculate mean and standard deviation you just need to use n, the number of trials, and p, the "
                "probability to calculate both of the values. They are as follows: ")
    st.markdown(r"$$\mu_x = np \hspace{50pt} \sigma_X = \sqrt{np(1-p)}$$")



    st.header("Binomial Distributions are Roughly Bell Shaped")
    st.markdown("We'll learn in a bit that binomial distributions are approximately bell shaped and if the number of "
                "trials is pushed to absurdly large number it'll get closer and closer to that bell shape.")

    st.plotly_chart(ax_more)

    st.header("Now you try:")

    user_trials = st.number_input("Number of Trials", value=4, max_value=7)
    user_prob = st.number_input("Probability of success", value=0.5,min_value=0.0, max_value=1.0)
    user_num_wins = st.number_input("Number of Successes", value=2, max_value=7)
    user_total_data = [binompdf(user_trials, user_prob, i) for i in range(user_trials+1)]
    user_data_labels = ["red" if i == user_num_wins else "blue" for i in range(user_trials+1)]
    user_cume_labels = ["red" if i <= user_num_wins else "blue" for i in range(user_trials+1)]
    user_df = {"x": range(user_trials+1),"Pr(x)": user_total_data, "Label": user_data_labels}
    user_cume_df = {"x": range(user_trials + 1), "Pr(x)": user_total_data, "Label": user_cume_labels}
    user_ax = px.bar(user_df, x="x", y="Pr(x)", color="Label", color_discrete_map={"red": "red","blue": "blue"})
    user_cume_ax = px.bar(user_cume_df, x="x", y="Pr(x)", color="Label",color_discrete_map={"red": "red","blue": "blue"} )

    binomcol1, binomcol2 = st.columns(2)

    with binomcol1:
        st.markdown(r"$Pr(X=x)$")
        st.markdown(str(binompdf(user_trials, user_prob, user_num_wins)))
        st.plotly_chart(user_ax)
    with binomcol2:
        st.markdown(r"$Pr(X \leq x)$")
        st.markdown(str(binomcdf(user_trials, user_prob, user_num_wins)))
        st.plotly_chart(user_cume_ax)

    st.markdown("The Probability Tree")
    create_binomial_probs(user_trials, user_prob, chart_lbl="user_viz")

