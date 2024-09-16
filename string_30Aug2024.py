s="Hello, Good Morning!"

print(s)

print("Length of string:",len(s))
print('\n')

print(s[0])
print(s[7])
print('\n')

for i in range(len(s)):
    print(s[i],end="")

# print('\n')
# for ch in range s:
#     print(ch,end="")

print('\n')
# String slicing
print("--->",s[0:9])
print("--->",s[0:9:2]) 
print("--->",s[19::-1])

a=20
b=10
sum=a+b
print("Addition of",a, "and", b, "is",a+b)
print(f"Addition of {a} and {b} is {a+b}")
print("Addition of {} and {} is {}".format(a,b,a+b))
print("Addition of %d and %d is %d"%(a,b,a+b))
