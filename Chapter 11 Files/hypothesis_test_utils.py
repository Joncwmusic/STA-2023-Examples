import math


def gamma_integrand(t, alpha):
    return (t ** (alpha - 1)) * math.exp(-t)


def get_mean(data_list):
    if len(data_list) == 0:
        return None
    return sum(data_list)/len(data_list)


def get_standard_deviation(data_list):
    if len(data_list) <= 1:
        return None
    mu = get_mean(data_list)
    diff_square_list = [(i-mu)**2 for i in data_list]
    var = sum(diff_square_list)/len(data_list)
    return var**0.5


def get_sample_standard_deviation(data_list):
    if len(data_list) <= 1:
        return None
    mu = get_mean(data_list)
    diff_square_list = [(i-mu)**2 for i in data_list]
    var = sum(diff_square_list)/(len(data_list)-1)
    return var**0.5


def area_interval_gamma(start_a, end_b, alpha, func):
    area_sum = func(end_b, alpha) + 4 * (func((end_b + start_a) / 2, alpha)) + func(start_a, alpha)
    avg_area = area_sum * (end_b - start_a) / 6
    return avg_area


def gamma_function(alpha, step=0.1, nsteps=1000):
    current_sum = 0
    current_start = 0
    next_point = current_start + step
    for i in range(nsteps):
        temp_sum = area_interval_gamma(current_start, next_point, alpha, gamma_integrand)
        current_sum += temp_sum
        current_start = next_point
        next_point += step
    return current_sum


def normpdf(mu, sigma, x):
    part_1 = 1 / (sigma * math.sqrt(2 * math.pi))
    part_2 = math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
    return part_1 * part_2


def t_distribution(x, df):
    numerator_part_1 = gamma_function((df + 1) / 2)
    denominator_part_1 = math.sqrt(df * math.pi) * gamma_function(df / 2)
    base_part_2 = 1 + x ** 2 / df
    exponent_part_2 = -(df + 1) / 2
    part_1 = numerator_part_1 / denominator_part_1
    part_2 = base_part_2 ** exponent_part_2
    return part_1 * part_2


def area_interval(start_a, end_b, mu, sigma, func):
    area_sum = func(mu, sigma, end_b) + 4 * (func(mu, sigma, (end_b + start_a) / 2)) + func(mu, sigma, start_a)
    avg_area = area_sum * (end_b - start_a) / 6
    return avg_area


def area_interval_t(start_a, end_b, df, func):
    area_sum = func(end_b, df) + 4 * (func((end_b + start_a) / 2, df)) + func(start_a, df)
    avg_area = area_sum * (end_b - start_a) / 6
    return avg_area


def normalcdf(lb=0, ub=1, mu=0, sigma=1, precision=0.02, nsteps=10000):
    current_sum = 0
    current_start = lb
    next_point = current_start + precision
    for i in range(nsteps):
        temp_sum = area_interval(current_start, next_point, mu, sigma, normpdf)
        current_sum += temp_sum
        current_start = next_point
        next_point += precision
        if next_point > ub:
            break
    return current_sum


def invNorm(area, mu=0, sigma=1, lcr="LEFT", precision=0.01):
    current_sum = 0
    if area > 1 or area < -1:
        raise ValueError("Invalid value for area. Must be between 0 and 1")
    if lcr == "LEFT":
        current_step = -10
        while current_sum < area:
            current_sum += precision * normpdf(mu, sigma, current_step)
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


def t_cdf(lb, ub, df, precision = 0.05, nsteps = 5000):
    current_sum = 0
    current_start = lb
    start_point_list  = []
    next_point = current_start + precision
    for i in range(nsteps):
        start_point_list.append(current_start)
        temp_sum = area_interval_t(current_start, next_point, df, t_distribution)
        current_sum += temp_sum
        current_start = next_point
        next_point += precision
        if next_point >= ub+precision:
            break
    return current_sum


def invT(area, df=30, lcr="LEFT", precision=0.01):
    current_sum = 0
    if area > 1 or area < -1:
        raise ValueError("Invalid value for area. Must be between 0 and 1")
    if lcr == "LEFT":
        current_step = -10
        while current_sum < area:
            current_sum += precision * t_distribution(current_step, df)
            current_step += precision
        return current_step
    elif lcr == "RIGHT":
        current_step = -10
        while current_sum < area:
            current_sum += precision * t_distribution(current_step, df)
            current_step -= precision
        return current_step
    elif lcr == "CENTER":
        current_step_L = 0
        current_step_R = 0
        while current_sum < area:
            current_sum += precision * t_distribution(current_step_L, df)
            current_sum += precision * t_distribution(current_step_R, df)
            current_step_L -= precision
            current_step_R += precision
        return current_step_L, current_step_R
    else:
        raise ValueError("Invalid value for lcr parameter. Values are LEFT, RIGHT, or CENTER")


def one_prop_interval(x, n, c_level):
    prop = x/n
    z_alpha = -invNorm((1-c_level)/2)
    error = -z_alpha*math.sqrt(prop*(1-prop)/n)
    return prop - error, prop + error


def one_prop_z_test(p0, x, n, alpha, htest_type):
    phat = x/n
    test_statistic = (phat - p0) / (math.sqrt(p0*(1-p0)/n))
    if htest_type == 'Left':
        p_value = normalcdf(-100, test_statistic, 0, 1)
    elif htest_type == 'Right':
        p_value = normalcdf(test_statistic, 100, 0, 1)
    else:
        p_value = 2*normalcdf(abs(test_statistic), 100, 0, 1)
    if p_value < alpha:
        decision = "reject"
    else:
        decision = "do not reject"
    return test_statistic, p_value, phat, decision


def two_prop_z_interval(x1, n1, x2, n2, c_level):
    prop1 = x1/n1
    prop2 = x2/n2
    z_alpha = -invNorm((1-c_level)/2)
    error = -z_alpha*math.sqrt(prop1*(1-prop1)/n1 + prop2*(1-prop2)/n2)
    return (prop1-prop2) - error, (prop1-prop2) + error


def two_prop_z_test(x1, n1, x2, n2, alpha, htest_type):
    prop1 = x1/n1
    prop2 = x2/n2
    prop_pool = (x1+x2)/(n1+n2)
    test_statistic = (prop1 - prop2) / (math.sqrt(prop_pool * 1 - prop_pool) * math.sqrt((1 / n1) + (1 / n2)))
    if htest_type == 'Left':
        p_value = normalcdf(-100, test_statistic, 0, 1)
    elif htest_type == 'Right':
        p_value = normalcdf(test_statistic, 100, 0, 1)
    else:
        p_value = 2*normalcdf(abs(test_statistic), 100, 0, 1)
    if p_value < alpha:
        decision = "reject"
    else:
        decision = "do not reject"
    return test_statistic, p_value, prop1, prop2, prop_pool, decision


def t_interval(x_bar, s, n, c_level):
    error = -invT((1-c_level)/2, n-1)*s/math.sqrt(n)
    return x_bar - error, x_bar + error


def t_test(mu0, xbar, sx, n, alpha, htest_type):
    test_statistic = (xbar - mu0) / (sx/math.sqrt(n))
    if htest_type == 'Left':
        p_value = t_cdf(-100, test_statistic, n-1)
    elif htest_type == 'Right':
        p_value = t_cdf(test_statistic, 100, n-1)
    else:
        p_value = 2*t_cdf(abs(test_statistic), 100, n-1)
    if p_value < alpha:
        decision = "reject"
    else:
        decision = "do not reject"
    return test_statistic, p_value, xbar, decision


def two_samp_t_interval(xbar1, s1, n1, xbar2, s2, n2, c_level):
    error = -invT((1-c_level)/2, n1+n2-2)*math.sqrt(s1**2/n1 + s2**2/n2)
    return xbar1-xbar2 - error, xbar1-xbar2 + error


def two_samp_t_test(xbar1, s1, n1, xbar2, s2, n2, alpha, htest_type):
    test_statistic = (xbar1 - xbar2) / math.sqrt(s1**2 /n1 + s2**2 /n2)
    if htest_type == 'Left':
        p_value = t_cdf(-100, test_statistic, n1+n2-2)
    elif htest_type == 'Right':
        p_value = t_cdf(test_statistic, 100, n1+n2-2)
    else:
        p_value = 2*t_cdf(abs(test_statistic), 100, n1+n2-2)
    if p_value < alpha:
        decision = "reject"
    else:
        decision = "do not reject"
    return test_statistic, p_value, xbar1, xbar2, decision


# L1, L2 = [12.4, 11.9, 13.1, 12.7, 11.5, 12.8, 13.3, 12.0], [12.1, 11.5, 12.7, 12.9, 11.2, 12.4, 12.8, 11.8]
# L3 = [round(L1[i] - L2[i], 1) for i in range(len(L1))]
# mu_d, sigma_d, n_d = get_mean(L3), get_sample_standard_deviation(L3), len(L3)
#
# test_1 = one_prop_z_test(0.6, 108, 200, 0.05, 'Left')
# test_2 = one_prop_z_test(0.3, 37, 150, 0.05, "2 Tail")
# test_3 = t_test(16, 15.84, 0.52, 40, 0.05, "2 Tail")
# test_4 = t_test(50, 58.3, 14.7, 12, 0.05, "Right")
# test_5 = two_samp_t_test(82.4, 9.1, 35, 78.6, 11.3, 38, 0.05, "2 Tail")
# test_6 = t_test(0, mu_d, sigma_d, n_d, 0.05, "Right")
#
# print(test_1)
# print(test_2)
# print(test_3)
# print(test_4)
# print(test_5)
# print(test_6)