# Itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator

a = [1, 2]
b = [3, 4]
prod = product(a,b, repeat=2)
print(list(prod))


a = [1, 2, 3]
perm = permutations(a, 2)
print(list(perm))


a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))


a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=max)
print(a)
print(list(acc))


def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))


for i in count(10):
    print(i)
    if i == 15:
        break

a = [1, 2, 3]
for i in cycle(a):
    print(i)


for i in repeat(1, 4):
    print(i)