# Dictionary: Key-Value pairs, Unordered, Mutable
mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

value = mydict["name"]
print(value)

mydict["email"] = "max@xyz.com"
print(mydict)

mydict["email"] = "coolmax@xyz.com"
print(mydict)

del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()
print(mydict)

mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["lastname"])
except:
    print("Error")

for key,value in mydict.items():
    print(key,value)

mydict_cpy = mydict.copy()
#mydict_cpy = dict(mydict)

mydict_cpy["email"] = "max@xyz.com"
print(mydict_cpy)
print(mydict)

my_dict = {"name": "Max", "age": 28, "email": "max@xyz.com"}
my_dict_2 = dict(name="Mary", age=27, city="Boston")
my_dict.update(my_dict_2)
print(my_dict)

my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)
value = my_dict[3]
print(value)

mytuple = (8, 7)
mydict = {mytuple: 15}
print(mydict)