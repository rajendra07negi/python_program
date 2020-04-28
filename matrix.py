from numpy import *
arr1 = array([
               [21,32,43,54],
               [22,33,44,35]
            ])
m = matrix(arr1)
# print(m)
mat = matrix('1, 2 3, 4  5, 7 8, 6')
print(mat)
mat1 = matrix('1, 2, 3, 4; 5, 6, 7, 8')
print(mat1)
mat2 = matrix('1,2,3;4,5,6;7,8,9')
print(mat2)
# if you want to print diagonal elements of matrix
print(diagonal(mat2))

# use some important in built function
print(mat2.max())
print(mat2.max())

# you want to sum two matrix
arr1 = matrix('1,2,3;4,5,6;7,8,9')
arr2 = matrix('10,20,30;40,50,60;70,80,90')
arr3 = arr1 + arr2
print(arr3)

# you want to multiply two matrix
arr3 = arr1 * arr2
print(arr3)



