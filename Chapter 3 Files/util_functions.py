import math
import numpy as np


def get_five_num_summary_numpy(numlist):
    data = np.array(numlist)
    minimum = np.min(data)
    q1 = np.percentile(data, 25)
    median = np.median(data)
    q3 = np.percentile(data, 75)
    maximum = np.max(data)
    return minimum, q1, median, q3, maximum


def get_arithmetic_mean(numlist):
    return sum(numlist)/len(numlist)


def string_to_list(numstring):
    return [float(x) for x in numstring.split(',')]


def get_median(numlist):
    numlist.sort()
    if len(numlist)%2 == 0:
        return 0.5*(numlist[int((len(numlist)/2) - 1)]+ numlist[int(len(numlist)/2)])
    else:
        return numlist[int((len(numlist)-1)/2)]


def get_mode(numlist):
    count_dict = {}
    for item in numlist:
        if item in count_dict.keys():
            count_dict[item]+=1
        else:
            count_dict[item]=1
    if max(count_dict.values()) == 1:
        return None
    else:
        mode_list = [keyval for keyval in count_dict if count_dict[keyval] == max(count_dict.values())]
        return mode_list


def get_range(numlist):
    return max(numlist) - min(numlist)


def get_variance(numlist):
    if len(numlist) == 0:
        return None
    sum_error = 0
    for item in numlist:
        sum_error = sum_error + (item - get_arithmetic_mean(numlist))**2
    return sum_error/len(numlist)


def get_standard_deviation(numlist):
    var = get_variance(numlist)
    return math.sqrt(var)
