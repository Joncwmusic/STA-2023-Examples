import random
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
import math
import plotly.graph_objects as go


def normpdf(mu, sigma, x):
    part_1 = 1/(sigma*math.sqrt(2*math.pi))
    part_2 = math.exp(-((x-mu)**2)/(2*sigma**2))
    return part_1 * part_2


def gamma_integrand(t, alpha):
    return (t**(alpha-1))*math.exp(-t)


def area_interval_gamma(start_a, end_b, alpha, func):
    area_sum = func(end_b, alpha) + 4*(func((end_b+start_a)/2, alpha)) + func(start_a, alpha)
    avg_area = area_sum*(end_b-start_a)/6
    return avg_area


def area_interval(start_a, end_b, mu, sigma, func):
    area_sum = func(mu, sigma, end_b) + 4*(func(mu, sigma, (end_b+start_a)/2)) + func(mu, sigma, start_a)
    avg_area = area_sum*(end_b-start_a)/6
    return avg_area


def normalcdf(lb, up, mu = 0, sigma = 1, precision = 0.1, nsteps = 1000):
    current_sum = 0
    current_start = 0
    next_point = current_start + precision
    for i in range(nsteps):
        temp_sum = area_interval(current_start, next_point, mu, sigma, normpdf)
        current_sum += temp_sum
        current_start = next_point
        next_point += precision
    return current_sum


def gamma_function(alpha, step=0.1, nsteps = 1000):
    current_sum = 0
    current_start = 0
    next_point = current_start+step
    for i in range(nsteps):
        temp_sum = area_interval_gamma(current_start, next_point, alpha, gamma_integrand)
        current_sum += temp_sum
        current_start = next_point
        next_point += step
    return current_sum


def invNorm(area, mu=0, sigma=1, lcr="LEFT", precision=0.01):
    current_sum = 0
    if area > 1 or area < -1:
        raise ValueError("Invalid value for area. Must be between 0 and 1")
    if lcr == "LEFT":
        current_step = -10
        while current_sum < area:
            current_sum += precision*normpdf(mu, sigma, current_step)
            current_step += precision
        return current_step
    elif lcr == "RIGHT":
        current_step = -10
        while current_sum < area:
            current_sum += precision * normpdf(mu, sigma, current_step)
            current_step -= precision
        return current_step
    elif lcr == "CENTER":
        current_step_L = 0
        current_step_R = 0
        while current_sum < area:
            current_sum += precision * normpdf(mu, sigma, current_step_L)
            current_sum += precision * normpdf(mu, sigma, current_step_R)
            current_step_L -= precision
            current_step_R += precision
        return current_step_L, current_step_R
    else:
        raise ValueError("Invalid value for lcr parameter. Values are LEFT, RIGHT, or CENTER")


def t_distribution(x, df):
    numerator_part_1 = gamma_function((df+1)/2)
    denominator_part_1 = math.sqrt(df*math.pi)*gamma_function(df/2)
    base_part_2 = 1 + x**2/df
    exponent_part_2 = -(df+1)/2
    part_1 = numerator_part_1/denominator_part_1
    part_2 = base_part_2**exponent_part_2
    # print(numerator_part_1, denominator_part_1, " Divide these to get: ", part_1)
    # print(base_part_2, exponent_part_2, " Raise to the power to get: ", part_2)
    # print("Current_Values, (" + str(x) + "," + str(part_1*part_2) + ")")
    return part_1*part_2


def invT(area, df=30, lcr="LEFT", precision=0.01):
    current_sum = 0
    if area > 1 or area < -1:
        raise ValueError("Invalid value for area. Must be between 0 and 1")
    if lcr == "LEFT":
        current_step = -10
        while current_sum < area:
            current_sum += precision*t_distribution(current_step, df)
            current_step += precision
        return current_step
    elif lcr == "RIGHT":
        current_step = -10
        while current_sum < area:
            current_sum += precision*t_distribution(current_step, df)
            current_step -= precision
        return current_step
    elif lcr == "CENTER":
        current_step_L = 0
        current_step_R = 0
        while current_sum < area:
            current_sum += precision*t_distribution(current_step_L, df)
            current_sum += precision*t_distribution(current_step_R, df)
            current_step_L -= precision
            current_step_R += precision
        return current_step_L, current_step_R
    else:
        raise ValueError("Invalid value for lcr parameter. Values are LEFT, RIGHT, or CENTER")


def confidence_interval_calculator_mean(sd, xbar, n, data=None, confidence = 0.95, option="Z"):
    if option == "Z":
        error = invNorm(confidence) * sd / math.sqrt(n)
        lower = xbar - error
        upper = xbar + error
        return lower, upper, error
    elif option == "T":
        error = invT(area=confidence, df=n - 1) * sd / math.sqrt(n)
        lower = xbar - error
        upper = xbar + error
        return lower, upper, error
    elif option == "data":
        mean = sum(data)/len(data)
        samp_std_dev = sum([(i-mean)**2 for i in data])/(len(data)-1)
        error = invT(area=confidence, df=n - 1) * samp_std_dev / math.sqrt(n)
        lower = mean - error
        upper = mean + error
        return lower, upper, error
    else:
        raise ValueError("options are limited to T, Z, or data")


def confidence_interval_calculator_proportion(n=100, prop=0.5, confidence = 0.95):
    p_hat = prop
    error = invNorm(confidence) * math.sqrt(p_hat*(1-p_hat)/n)
    lower = p_hat - error
    upper = p_hat + error
    return lower, upper, error


def find_min_sample_size(error, sd, confidence = 0.95):
    sample_size = (invNorm(area=confidence, mu=0, sigma=1)*sd/error)**2
    return math.ceil(sample_size)

def find_min_sample_size_prop(error, confidence = 0.95, p_hat = 0.5):
    sample_size = p_hat*(1-p_hat)*(invNorm(area=confidence, mu=0, sigma=1)/error)**2
    return math.ceil(sample_size)

def build_confidence_inteval_prop():
    x_vals = [i/20 for i in range(-100, 100)]
    t_dist_3 = [t_distribution(i, 3) for i in x_vals]
    t_dist_8 = [t_distribution(i, 8) for i in x_vals]
    t_dist_15 = [t_distribution(i, 15) for i in x_vals]
    norm_dist_0_1 = [normpdf(0, 1, i) for i in x_vals]

    norm_0_1_df = pd.DataFrame({"x_vals": x_vals, "y_vals": norm_dist_0_1, "dist": ["normal" for i in x_vals]})
    t_3_df = pd.DataFrame({"x_vals": x_vals, "y_vals": t_dist_3, "dist": ["df=3" for i in x_vals]})
    t_8_df = pd.DataFrame({"x_vals": x_vals, "y_vals": t_dist_8, "dist": ["df=8" for i in x_vals]})
    t_15_df = pd.DataFrame({"x_vals": x_vals, "y_vals": t_dist_15, "dist": ["df=15" for i in x_vals]})

    all_dist_df = pd.concat([norm_0_1_df, t_3_df, t_8_df, t_15_df])

    color_map_for_normal_vs_t = {"normal": "0000ff", "df=3": "ff0000", "df=8": "bb1111", "df=15": "992222"}

    fig_norm_0_1_solo = px.line(data_frame=norm_0_1_df, x="x_vals", y="y_vals", title="standard normal plot")
    fig_norm_0_1 = px.line(data_frame=norm_0_1_df, x="x_vals", y="y_vals"
                           ,color_discrete_map=color_map_for_normal_vs_t, title="normal plot vs. t distrbutions")

    fig_all_dist = px.line(data_frame=all_dist_df, x="x_vals", y="y_vals", color = "dist")

    st.header("Confidence Interval and Error for a Proportion")

    st.markdown("So instead of a Mean, we can estimate a proportion instead with a confidence interval. You see this "
                "all of the time with political polling showing 56% approval with a 3% margin of error. The formula "
                "for the confidence interval is very similar to that of the mean we just use the standard error "
                "for the proportion instead.")
    st.markdown(r"$\mu_{\hat{p}} = p \hspace{30pt} \sigma_{\hat{p}} = \sqrt{\dfrac{\hat{p}(1-\hat{p})}{n}}$")
    st.markdown(r"So naturally like our mean confidence interval it should look like this:")

    st.markdown(r"$\hat{p}-z_{\alpha /2}\sqrt{\dfrac{\hat{p}(1-\hat{p})}{n}} < p < "
                r"\hat{p}+z_{\alpha /2}\sqrt{\dfrac{\hat{p}(1-\hat{p})}{n}}$")

    st.markdown(r"This also means our error margin is just the part after the $\hat{p}$")

    st.markdown(r"$E = z_{\alpha /2}\sqrt{\dfrac{\hat{p}(1-\hat{p})}{n}}$")

    st.header("Minimum Sample Size")
    st.markdown("If we have a desired margin of error and ideal confidence level, to ensure we're getting the right "
                "sample size to even measure a population proportion, it'd be a good idea to have a way to figure out"
                "what the minimum sample size is. If we rearrange our confidence interval formula we can get "
                "the minimum sample size formula for a proportion:")

    st.markdown(r"$n = \hat{p}(1-\hat{p})\bigg(\dfrac{z_{\alpha/2}}{E}\bigg)^2$")

    st.markdown(r"Note that if an estimate of $\hat{p}$ isn't given, you can't get it because you don't have an $n$. "
                r"That's the part we're looking for. In this case use $\hat{p}$=0.5 as your estimate to maximize the "
                r"sample size.")

    st.header("Now You Try")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Find C.I. and Error")
        conf_level_user = st.number_input(label = "Put in confidence level:", value=.95, min_value=.8, max_value=.999
                                          ,key="prop_error_CL")
        sample_prop_user = st.number_input(label= "Put in your sample proportion", value = 0.5, min_value=0.001
                                           , max_value=0.999, key="prop_error_phat")
        sample_size_user = st.number_input(label="Put in sample size:", value=30, min_value=1, max_value=1000
                                           , key="prop_error_n")
        lower_bound, upper_bound, error = confidence_interval_calculator_proportion(confidence=conf_level_user
                                                                                    , prop=sample_prop_user
                                                                                    , n=sample_size_user)
        st.markdown("We are " + str(conf_level_user*100) + "% confident that the population mean falls between "
                    + str(round(lower_bound, 2)) + " and " + str(round(upper_bound, 2)) + " with our point estimate "
                    + str(sample_prop_user) + " and error margin " + str(error) + ".")

    with col2:
        st.subheader("Find Min Sample Size")
        conf_level_user = st.number_input(label="Put in a confidence level:", value=.95, min_value=.8, max_value=.999
                                          ,key = "min_sample_prop_CL")
        error_user = st.number_input(label="Put in the margin of error:", value=0.5, min_value=0.001
                                     ,key="min_sample_prop_error")
        p_hat_user = st.number_input(label="Put in a sample proportion:", value = 0.5, min_value=0.001, max_value=0.999
                                     ,key = "min_sample_prop_phat")
        sample_size_result = find_min_sample_size_prop(confidence=conf_level_user, error=error_user, p_hat=p_hat_user)
        st.markdown("The minimum sample size needed with " + str(conf_level_user) + "% confidence and a "
                    + str(error_user) + " margin of error is " + str(sample_size_result) + ".")