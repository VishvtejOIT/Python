class Parent:
    def giveIntro(self):
        print("Hello, I am parent class")
        
class Child(Parent):
    def givenIntro(self):
        print("Hello, I am child class")
        
rajesh = Parent()
raju = Child()

rajesh.giveIntro()
raju.givenIntro()