# if() ----> if is false

# res=input("what is your result ? ")
# if(res=='pass'):
#     print('Yes')
# else:
#     print('No')

# n=int(input("Enter a number:"))    
# if(n%7==0):
#     print("Yes, it is divisible by 7")
# else:
#     print("No, it is divisible by 7")

# n=int(input("Enter a number:"))
# if(n%2==0):
#     print("Number is Even")
# else:
#     print("Number is Odd")
    
# n=int(input("Enter a number:"))
# if n>0:
#     print('Number is Positive')
# elif n<0:
#     print('Number is Negative')
# else:
#     print('Number is Zero')

# n=int(input("Enter your age:"))
# if n>18:
#     print('You can vote')
# elif n<18:
#     print('You can\'t vote')
# else:
#     print('Applied for card')
  
#-------- Nested if-else --------------  
# a=int(input("Enter 1st number:"))
# b=int(input("Enter 2nd number:"))
# c=int(input("Enter 3rd number:"))

# if a>b:
#     if a>c:
#         print('a is grater')
#     else:
#         print('c is greater')
# else:
#     if b>c:
#         print('b is greater')
#     else:
#         print('c is greater')
        
password=int(input("Enter your password"))
# if password==1234:
#     print('Welcome')
# else:
#     print('Invalid password')
print('Welcome') if password==1234 else print('Invalid password')