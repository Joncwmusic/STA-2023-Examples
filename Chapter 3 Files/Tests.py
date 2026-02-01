import util_functions as uf


assert uf.get_arithmetic_mean([1, 2, 3]) == 2

assert uf.get_median([1, 2, 3, 4]) == 2.5
assert uf.get_median([1, 2, 3]) == 2

print(uf.get_mode([3, 6, 8, 9]))
assert uf.get_mode([3, 6, 8, 8, 12]) == [8]
assert uf.get_mode([3, 6, 8, 8, 12, 12]) == [8, 12]