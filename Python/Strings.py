# Strings: ordered, immutable, text representation
my_string = "Hello World"
char = my_string[0]
substring = my_string[::-1]

print(my_string)
print(char)
print(substring)

greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

for i in greeting:
    print(i)

if 'ell' in greeting:
    print('yes')
else:
    print('no')


my_string = 'Hello World'
my_string = my_string.strip()
print(my_string.upper())
print(my_string.lower())

my_string = 'how, are, you, doing'
my_list = my_string.split(", ")
print(my_list)

new_string = ' '.join(my_list)
print(new_string)

my_list = ['a'] * 6
print(my_list)

#bad
my_string = ''
for i in my_list:
    my_string += i
print(my_string)

#good
my_string = ''.join(my_list)
print(my_string)

var = 3.262
my_string = "the variable is %.3f" % var
print(my_string)

var = 3.262
var2 = 6
my_string = "the variable is {:.2f} and {}".format(var,var2)
print(my_string)

var = 3.262
var2 = 6
my_string = f"the variable is {var*2} and {var2}"
print(my_string)