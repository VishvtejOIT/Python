#String: A string is sequence of characters, such 

# Ex.1:
# str1="Hello"
# str2='Hello'
# str3='''Hello'''
# str4="""Hello"""
# print(str1)
# print(str2)
# print(str3)
# print(str4)

'''
# Ex.2: Escape Squence character: (\",\',\n,\t)
d1='Ramesh said,"I want to apple".'
print(d1)
d2="Ramesh said,\"I want to apple\"."
print(d2)
d3="Ramesh say's,\"I want to apple\"."
print(d3)
d4='Ramesh say\'s,"I want to apple".'
print(d4)
d5='Ramesh say\'s,"\nI want to apple".'
print(d5)
d6='Ramesh say\'s,"\tI want to apple".'
print(d6)

# Ex.3:String Concatenation
str1="Hello,"
str2="Good Morning!"
str3=str1+" "+str2
print(str3)
'''
# Ex.4
# Formated string (f-string):
a=30
b=40
ans1=f"Addition of {a} and {b} is {a+b}"
print(ans1)
ans2="Addition of {} and {} is {}",format(a,b,a+b)
print(ans2)