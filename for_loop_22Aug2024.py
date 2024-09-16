#For Loop

#range()

# for i in range(1,11):
#     print(i)

# for i in range(-10,11):
#     print(i)
    
# for i in range(11,11):
#     print(i)
    
# for i in range(11,1):
#     print(i)
    
# for i in range(1,11,1):
#     print(i)

# for i in range(1,11,2):
#     print(i)

# for i in range(1,11,3):
#     print(i)

# for i in range(10,0,-1):
#     print(i)


# for
# for i in range(5):
#     print("Hello")
'''
Ex.1
#accept the number of iteration from user and print Hello   
n=int(input("Enter a number:"))
# for i in range(n):
#     print(i,":Hello")
for i in range(n+1):
    print(i,":Hello")
'''

'''
# Ex.2
# accept the number of iteration from user and print sum of all number from 1 to n
n=int(input("Enter a number:"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)
'''

#Ex.3
#Accept the number from user and print factorial for given number
# 1!=1
# 0!=1
n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1):
# for i in range(n,0,-1):
    fact=fact*i 
print(n,"!:",fact,sep="")