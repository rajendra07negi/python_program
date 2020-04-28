def update(x):
    print(id(x))
    x = 9
    print(id(x))
    print("x ", x)
a = 10
print(id(a))
update(a)
print("a ",a)

def updateLst(lst):
    print(id(lst))
    lst[2] = 25
    print(id(lst))
    print(lst)
lst = [20,30,40,50]
print(id(lst))
updateLst(lst)
print(lst)