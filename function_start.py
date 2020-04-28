# use function to print statements
def greet():
    print('Hello World!')
    print('Rajendra')
greet() # calling the function
# pass arguments and print result
def add(x,y):
    c = x + y
    print(c)
add(6,4)

# pass arguments and return value

def add(x,y):
    c = x +y
    return c
result = add(6,4)
print(result)

# pass arguments and return more than one value
def add_sub(x,y):
    c = x + y
    d = x - y
    return c,d
result1,result2 = add_sub(6,4)
print(result1,result2)




