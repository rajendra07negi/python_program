from numpy import *
# In this program we add 5 in each element of array
arr = array([21,32,32,34])
arr = arr + 5
print(arr)

# in this program we add two array each element (this called vectorized operation)

arr1 = array([5,6,7,8])
arr2 = array([19,28,57,16])
arr3 =  arr1 + arr2
print(arr3)

# use some mathematical in built function
arrayElement = array([3,5,7,9])
print(sin(arrayElement))
print(cos(arrayElement))
print(log(arrayElement))
print(sqrt(arrayElement))
print(sum(arrayElement))
print(min(arrayElement))
print(max(arrayElement))

# concatenate to two arrays
arr_one = array([11,14,17,24])
arr_sec = array([1,12,10,20,43])
print(concatenate([arr_one,arr_sec]))