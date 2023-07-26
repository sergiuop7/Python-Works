import sys

def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()

print(sum(g))

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)

value = next(cd)
print(value)
print(next(cd))


def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sum(firstn(10)))
print(sum(firstn_generator(10)))

print(sys.getsizeof(firstn(10000)))
print(sys.getsizeof(firstn_generator(10000)))

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

fib = fibonacci(30)
for i in fib:
    print(i)

mygenerator = (i for i in range(10000) if i % 2 == 0)

mylist = [i for i in range(10000) if i % 2 == 0]

for i in mygenerator:
    print(i)

print(mylist)

print(sys.getsizeof(mygenerator))
print(sys.getsizeof(mylist))