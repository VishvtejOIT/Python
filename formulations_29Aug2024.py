#formulations:
'''
# (a+b)^2=a*a+b*b+2*a*b
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
ans=a*a + b*b + 2*a*b
print("(a+b)^2:",ans)

# Area of circle= (3.14)* (r)* (r)
r=int(input("Enter the radius of circle:"))
ans=3.14*r*r
print(f"Area of circle: {ans} sq.cm.")

# Volume of sphere=(4/3)*3.14*r**3
r=int(input("Enter the radius of circle:"))
ans=(4/3) * (3.14) * (r**3)
print(f"Volume of sphere: {ans} cu.cm.")

# prime number
num=int(input("Enter a number:"))
flag=1
for i in range(2,num//2):
    if num%i==0:
        flag=0
        break
if flag==1:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
'''
    
# Palindrome number
num=int(input("Enter a number:"))
temp=str(num)
rev=int(temp[::-1])
# rev=int(str(num)[::-1])
if(num==rev):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not palindrome")