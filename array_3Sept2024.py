from array import *

arr = array("i",[12,56,43,21,90,12])
print(type(arr))
print(arr)
print(arr.typecode)
print(arr.tolist())

# print(arr[2])

# arr[2]=40

# print(arr.tolist())

# print(arr.index(40))

arr[arr.index(43)]=40
print(arr.tolist())

# append
arr.append(100)
print(arr.tolist())

# insert on any index
arr.insert(3,99)
print(arr.tolist())

arr.extend([44,55,66])
# arr.extend({23,45})
print(arr.tolist())

# remove any item:
arr.remove(100)
print(arr.tolist())

# remove item using index
arr.pop()
# arr.pop(2)
print(arr.tolist())

# count:
print("Occurance(12):",arr.count(12))

# slicing of array
print("Slicing of array:",arr[0:len(arr):2])
print("Reverse of array:",arr[len(arr)::-1])

arr.reverse()
print("Reverse:",arr.tolist())