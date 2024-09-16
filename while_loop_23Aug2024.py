'''
Ex.1
i=1
while i<10:
    print(i)
    i+=1

Ex.2
i=1
while i<=10:
    print(i)
    i+=1

#Ex.3: print table for 5
i=1
while i<=10:
    print("5 x",i,"=",i*5)
    i+=1

#Ex.4: 2 5 8 11
i=2
while i<=50:
    print(i)
    i+=3
    
# Ex.5: 1 4 7 10 13 16 19
i=1
while i<=50:
    print(i)
    i+=3

# Ex.6: print series power of 2 
i=1
while i<=10:
    print("2 ^",i,"=",2**i)
    i+=1

# break and continue
i=0
while i<10:
    i+=1
    if i==5:
        break
    print(i)
print("Done")

i=0
while i<10:
    i+=1
    if i==5:
        continue
    print(i)
print("Done")
'''
# when we perform do-while in python than use condition while True
while True:
    password=input("Enter your passkey:")
    if password=="1234":
        break
    
print("Your device is unlocked")