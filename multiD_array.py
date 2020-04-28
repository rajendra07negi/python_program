from numpy import *
# 2D array
arr2d = array([
                [3,5,4,9,54,34],
                [12,43,54,56,30,40]
            ])
print(arr2d)
# Use some in built function on multi dimensional array
print(arr2d.dtype)
# give the type of array data
print(arr2d.ndim)
# return the number of dimensional of array
print(arr2d.shape)
# it is give the dimension and size information of array
# but if arrays have different size
# than it returns only dimension not return size
print(arr2d.size)
# it return size of entire block
arr1 = arr2d.flatten()
# this make multi dimensional array to single dimensional array
print(arr1)
# if we want to make 2 d from 1 d
arr3 = arr1.reshape(2,2,3)
print(arr3)