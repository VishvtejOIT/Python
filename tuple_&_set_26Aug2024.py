# tuple: is immutable(unchangeble) data type in python
'''
mytuple=(3,5,8,1)
print("My tuple:",mytuple)
print(type(mytuple))

mytuple[0]=55 #TypeError: 'tuple' object does not support item assignment
a=(2,5,77,"hello",2,"vadapav",2)
print("Tuple:",a)
print(a.index(77))
print(a.count(2))
'''

#set: is an unordered collection of unique elements

'''
myset={8,2,6,3,1,2,7,3}
print("Set:",myset)
print(type(myset))

myset.add(10)
print(myset)

myset.remove(7)
print(myset)

myset.discard(6)
myset.discard(15)
print(myset)

myset.update({12,43,67})
print(myset)
'''

#Ex.2
A={3,1,5,8,3}
B={9,1,5,3,8}

C=A.copy()

A.remove(8)
print(A)
print(C)

print("A U B:",A.union(B))
print("A n B:",A.intersection(B))
print("A D B:",A.difference(B))
print("A D B:",B.difference(A))