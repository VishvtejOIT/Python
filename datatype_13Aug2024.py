#Data type in python
#Number:
a=32
print(type(a)) #Output: <class 'int'>

b=3.14
print(type(b)) #Output: <class 'float'>

c=4+5j
print(type(c)) #Output: <class 'complex'>

#Text:
#Single line comment
"Hello"
'Bye'
#Multiline comment
'''Hello good
morning'''
"""Hello
ji"""

#Sequence type
#List
my_list=[1,2,3,4,5]
print(type(my_list)) #Output: <class 'list'>
#tuple
my_tuple=(1,2,3,4,5)
print(type(my_tuple)) #Output: <class 'tuple'>
#Dictionary: Map
my_dict={
    "name":"Atharve",
    "age":20
}
print(type(my_dict)) #Output: <class 'dict'>
#Set
my_set={1,2,3,4,5}
print(type(my_set)) #Output: <class 'set'>

#Boolean
is_admin=True
print(type(is_admin)) #Output: <class 'bool'>