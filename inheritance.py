class Computer:
    def __init__(self,ip,pro,op,price,os):
        self.input_device = ip
        self.processor = pro
        self.output_device = op
        self.price = price
        self.operating_system = os
        
    def display_details(self):
        print("Input device connected :"," & ".join(self.input_device))
        print("Processor:",self.processor)
        print("Output device connected :"," & ".join(self.output_device))
        print("Price :",self.price)
        print("Operating system :",self.operating_system)
        
class Mobile(Computer):
    def __init__(self, ip, pro, op, price, os,ch_type,mgpx, networkIs5g="No"):
        super().__init__(ip, pro, op, price, os)
        self.charging_type = ch_type
        self.camera = mgpx
        self.network_5g = networkIs5g
        
    def show_details(self):
        pass