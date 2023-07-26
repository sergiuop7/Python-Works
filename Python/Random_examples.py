import random, secrets
import numpy as np

a = random.randrange(1, 10)
print(a)

a = random.normalvariate(0, 1)
print(a)

mylist = list("ABDGKN")
print(mylist)
a = random.choices(mylist, k=3)
print(a)

random.shuffle(mylist)
print(mylist)

random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))


mylist = list("ABCDEFGH")
a = secrets.choice(mylist)
print(a)


a = np.random.randint(0, 10, (3,4))
print(a)

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
np.random.shuffle(arr)
print(arr)

np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))