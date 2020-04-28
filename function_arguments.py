# Position arguments
def person(name, age):
    print(name)
    print(age)
person('rajendra',38)

# default argument
def person1(name, age = 18):
    print(name)
    print(age)
person1('rajendra')
person('amit',38)

#  keyword arguments
def person2(name,age,mobile):
    print(name)
    print(age)
    print(mobile)
person2(age=38,name='rajendra',mobile=9582063057)

# variable length arguments
def pr(a,*b):
    print(a)
    print(b)
pr(21,32,45,67)

def sum1(a,*b):
    c = a
    for i in b:
        c = c +i
    print(c)
sum1(21,32,45,67)

def sum2(*b):
    c = 0
    for i in b:
        c = c +i
    print(c)
sum2(21,32,45,67)

# keyword variable length arguments
def pr1(name, **data):
    print(name)
    print(data)
pr1('rajendra singh negi', age = 38, city = 'moradabad', mobile = 9582063057)

def pr2(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)
pr2('rajendra singh negi', age = 38, city = 'moradabad', mobile = 9582063057)