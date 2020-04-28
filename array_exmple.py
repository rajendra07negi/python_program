from array import *
# add 5 in all elements of array
arr = array('i',[21,32,43,54])
arr1 = array('i',[])
for i in arr:
    x = i + 5
    arr1.append(x)
print(arr1)
