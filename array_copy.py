from numpy import *
# copy array  (This is aliasing)
arr1 = array([5,4,7,8,1])
arr2 = arr1
arr2[1] = 10  # if we change in one array this reflect in both
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

# shallow copy
arrc1 = array([12,13,14,15])
arrc2 = arrc1.view()
arrc1[1] = 21
print(arrc1)
print(arrc2)
print(id(arrc1))
print(id(arrc2))

# Deep copy (In this type of copying array have not dependency between one other.Both addresses are different)
# if you change in one array this change not reflect to other array.
arrc1 = array([12,21,17,25])
arrc2 = arrc1.copy()
arrc1[1] = 10
print(arrc1)
print(arrc2)
print(id(arrc1))
print(id(arrc2))

