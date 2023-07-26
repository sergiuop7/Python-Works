# Sets: unordered, mutable, no duplicates
myset = set("Hello")

myset.add(1)
myset.add(2)
myset.add(3)

myset.remove(3)
myset.discard(2)

print(myset.pop())

for i in myset:
    print(i)

if 1 in myset:
    print("yes")
else:
    print("no")

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
diff = setB.symmetric_difference(setA)
print(diff)

setA.symmetric_difference_update(setB)
print(setA)

setC = setA.copy()
#setC = set(setA)

setC.add(15)
print(setC)
print(setA)

a = frozenset([1, 2, 3, 4])

a.remove(1)

print(a)