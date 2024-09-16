'''
# Ex.1:
def greet(): #Function declaration
    print("Good Morning") #Function defination
    print("Have a nice day")
    print("Welcome")

greet() #Function call

#EX.2:
def add():
    a=int(input("Enter value of a:"))
    b=int(input("Enter value of b:"))
    print("Addition",(a+b))
add()

# Ex.3:
def AreaOfCuboid():
    l=int(input("Enter length:"))
    b=int(input("Enter breadth:"))
    h=int(input("Enter height:"))
    Area=2*(l*b + b*h + h*l)
    print(f"The area of cuboid is: {Area} cu.cm.")
 
AreaOfCuboid()   
print(AreaOfCuboid)
print(id(AreaOfCuboid))

# for i in range(5):
#     AreaOfCuboid()

# Ex.4:
def evenOdd():
    num=int(input("Enter a number"))
    if (num&1)==0:
        print("The number is Even")
    else:
        print("The number is Odd")
        
evenOdd()
'''
# Ex.4:
def calculateBill():
    item=input("Enter the item one")
    price=float(input("Enter price of the item:"))
    tax=float(input("Enter the tax percentage"))
    tax_amt=(price*tax)/100
    total_bill=price+tax_amt
    print(f"Your total bill is for {item}:{total_bill} Rs")
    
calculateBill()