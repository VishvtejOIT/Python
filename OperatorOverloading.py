# class ComplexNumber:
#     def __init__(self, X, Y):
#         self.x = X
#         self.y = Y
        
#     def __str__(self):
#         return f"({self.x}+{self.y}i)"
    
#     def __repr__(self):
#         return f"Real Part:{self.x}\nImaginary Part:{self.y}\n"
    
# a = ComplexNumber(2,5)
# print(str(a))
# print(repr(a))

# ---------------------------------------------------

# Ex.2
class Vector:
    def __init__(self, X, Y, Z):
        self.x = X
        self.y = Y
        self.z = Z
        
    def __str__(self):
        return f"Vector({self.x}i+{self.y}j+{self.z}k)"
    
v1 = Vector(4,5,3)
print(v1)
