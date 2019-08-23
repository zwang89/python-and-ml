# this is practice for python udemy bootcamp
num = 12
name = 'Sam'
print ('My number is {one} and my name is {two}'.format(one=num,two=name))

# slice location
s  = "dfadfadfasfasdljladjflafj"
print(s[2:5])

# list
my_list = ['s', 'd']

# nested list

nest = [1,5 ,3, 5, ['dfadfa', 5]]

# dictionaries
d = {'key1': 'value', 'key2': [1,3,4,6]}

# tuble and list
# list can be change but tuble could not

# logic operation

1 < 2 and 2 > 4
print(1 > 4 or name == 'Sam')

# if statement
# elif only excute the first true condition
if 1 == 2 or 3 > 5:
    print ('you are right')
elif 4 ==4:
    print('yes')
else:
    print('nope')


# for loops
seq = [1,2,3,4,5]
for item in seq:
    print(item)

# while loop is continue excuting untile creteria meet
i = 1

while i < 5:
    print('i is {}'.format(i))
    i = i +0.5


# range function
for x in range(0,10):
    print(x)

# list comprehension
out = []
for num in seq:
    out.append(num ** 2)

print(out)

# the above code is able to list comprehension
# write down the outcome first and then list the for loop
[num**2 for num in seq]

# function to avoid write certain code again and again

def myfuct(name):
    """"""
    print('hellow ' + name)


myfuct('zhi')

# a complex example

def square(num):
    """
    this is the document for square fuction

    """
    return num**3

square(100)

# map ()
# no needs to add more files
new_list = list(map(square,seq))
print(new_list)

# lamba -  to reduce redundant codes
def square(num): return num**3

t = lambda num:num**3

# filter function
list(filter(lambda num: num%2 == 0, seq))

# method

s = 'try to get what I want through !!!!python'
s.capitalize()
print(s.split('!'))

# pop fuction

# in

'x' in ['x','y','z']