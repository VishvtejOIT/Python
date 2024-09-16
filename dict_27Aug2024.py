#dict: A collection of key-value pairs where each key is unique 
'''
Flist={
    "a":"apple",
    "A":"apple",
    "b":"banana",
    "c":"cherry",
}
print(type(Flist))
print(Flist)

# print(id(Flist["a"]))

for key in Flist:
    print(key,":",Flist[key])
    
# Ex.2:
mydict={
    "name":"John",
    "age":30,
    "city":"New York"
}
for key in mydict:
    print(key,":",mydict[key])
    
mydict.update({
    "country":"India",
    "phone":"1234567890"  
})
print(mydict)
print("conName:",mydict.get("country"))
print("Keys:",mydict.keys())
print("Values:",mydict.values())
print("Items:",mydict.items())

mydict.clear()
print(mydict)

# Ex.3 : Change key value
mydict={
    "name":"John",
    "age":30,
    "city":"New York",
    "name":"Ram",
}
mydict["name"]="Mona"

print(mydict)
'''
# mydict={
#     "name":"John",
#     "age":30,
#     "city":"New York",
#     "name":"Ram",
# }
# print(mydict["name"])

# Ex.4: remove key-value pair
mydict={
    "name":"John",
    "age":30,
    "city":"New York",
    "name":"Ram",
}
print(mydict)
del mydict["age"]
print(mydict)
