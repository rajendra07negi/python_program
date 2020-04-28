from array import *
arr = array('i',[]) # blank array
length = int(input("Enter the length of Array :"))
for i in range(length):
    value = int(input("Enter the element for Array :"))
    arr.append(value)  # inserting value in array
print(arr)

# manual program for searching element index number
val = int(input("Which element index number you want to know:"))
k = 0
for e in arr:
    if(e == val):
        print(k)
        break
    k+=1

# index number search by in built function
print(arr.index(val))