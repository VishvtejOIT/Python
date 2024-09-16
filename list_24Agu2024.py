# List
'''
# Ex.1:
nums=[2,5,1,6,8,9]
print(type(nums))

# Ex.2:
mylist=[23,4.23,True,"Vishvtej","123"]
print(mylist)

# Ex.3:
#   0  1  2  3  4   ---> +ve indexing
a=[33,55,77,99,88]
#  -5 -4 -3 -2 -1   ---> -ve indexing
print("List:",a)
print(a[1])
print(a[-4])

# Ex.4
# Sort list 
b=[33,11,77,99,88]
print("List:",b)
print("List:",b.sort())
print("List:",b)
print("List:",b.sort(reverse=True))
print("List:",b)

# Ex.5
# remove list value 
mylist=[2,4,3,6,7]
print("Original list:",mylist)
mylist[2]=8 #replace
print("List after modify:",mylist)
mylist.remove(6) #remove
mylist.remove(4)
print("List after remove:",mylist)

# Ex.6
# To add the new element in list
mylist=[2,4,3,6,7]
print("Original list:",mylist)

#append:
mylist.append(9)
print("List after append:",mylist)

#insert:
mylist.insert(2,8)
print("List after insert:",mylist)

# Ex.7:
# To find the index of element in list
mylist=[2,7,4,1,8,9,4,3]
print("Index of 9:",mylist.index(9))

# Ex.8:
# To find the count of element in list
mylist=[4,1,6,2,7,4,8]
print("count of 4:",mylist.count(4))

# Ex.9:
mylist=[4,1,6,2,7,4,8]
print("Max element",max(mylist))
mylist=[4,1,6,2,7,4,8]
print("Min element",min(mylist))

# Ex.9:
mylist=[2,1,5]
print("Sum of all element:",sum(mylist))
'''
# Ex.10
#reverse
mylist=[2,4,3,6,7,4]
print("Original list:",mylist)
mylist.reverse()
print("List after reverse:",mylist)
