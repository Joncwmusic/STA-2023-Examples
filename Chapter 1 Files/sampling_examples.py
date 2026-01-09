import random

test_score_list = []

for i in range(500):
    test_score_list.append(round(random.gauss(mu= 70, sigma= 12),2))

print(test_score_list)


def get_random_sample_with_replacement(data_list, num_samples):
    sample_list = []
    for i in range(num_samples):
        sample_list.append(data_list.pop(random.randint(1, len(data_list) - 1)))
    return sample_list


def get_random_sample_without_replacement(data_list, num_samples):
    sample_list = []
    for i in range(num_samples):
        sample_list.append(data_list[random.randint(1, len(data_list) - 1)])
        data_list.pop()
    return sample_list


def get_systematic_sample(data_list, k, offset):
    sample_list = [x for i, x in enumerate(data_list) if i%k == offset]
    return sample_list

def show_histogram(data_list):
    return None

def show_dual_histogram(data_list_1, data_list_2):
    return None





##### tests
sample_with_replacement = get_random_sample_with_replacement(test_score_list, 50)
sample_without_replacement = get_random_sample_without_replacement(test_score_list, 50)
sample_systematic = get_systematic_sample(test_score_list, 9, 3)

print(sample_with_replacement)
print(sample_without_replacement)
print(sample_systematic)