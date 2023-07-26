result = 2 ** 4
print(result)

zeros = [0,1] * 10
print(zeros)

def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, six=6, seven=7)

def foo(a, b, c):
    print(a, b, c)

foo(1, 2, c=3)

my_list = [0, 1, 2]
foo(*my_list)

my_dict = {'a': 1, 'b': 2, 'c': 3}
foo(**my_dict)

numbers = [1,2 , 3, 4, 5, 6]

*beginning, last = numbers
print(beginning)
print(last)

beginning, *last = numbers
print(beginning)
print(last)

beginning, *middle, last = numbers
print(beginning)
print(middle)
print(last)

my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {4, 5, 6}

new_list = [*my_tuple, *my_list]
new_list2 = [*my_tuple, *my_set]
print(new_list)
print(new_list2)

dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}
my_dict = {**dict_a, **dict_b}
print(my_dict)