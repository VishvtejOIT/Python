class Earphones:
    def __init__(self,Company,Price,Color,BL) :
        self.company=Company
        self.price=Price
        self.color=Color
        self.battery_life=BL
        
    def PrintInvoice(self):
        print("Company :",self.company)
        print("Price :",self.price)
        print("Colour :",self.color)
        print("Battery Life :",self.battery_life)
        
ep1=Earphones("Apple",25000,"White",3)
ep1.PrintInvoice()
ep2=Earphones("Boat",15000,"Black",4)
ep2.PrintInvoice()

# print("Company :",ap1.company)
# print("Price :",ap1.price)
# print("Colour :",ap1.color)
# print("Battery Life :",ap1.battery_life)

# print("Company :",ap2.company)
# print("Price :",ap2.price)
# print("Colour :",ap2.color)
# print("Battery Life :",ap2.battery_life)