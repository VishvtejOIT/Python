class Earphone:
    def __init__(self, company, price, color, battery_life, number_of_piece, water_proof, battery_charge_time, earpiece_shape, material, charging_type, bluetooth_range):
        self.company = company
        self.price = price
        self.color = color
        self.battery_life = battery_life
        self.number_of_piece = number_of_piece
        self.water_proof = water_proof
        self.battery_charge_time = battery_charge_time 
        self.earpiece_shape = earpiece_shape
        self.material = material
        self.charging_type = charging_type
        self.bluetooth_range = bluetooth_range
        self.battery_max_life = battery_life
        self.volume_level = 50
        self.is_connected = False
        self.o_touch=False
        self.d_touch=False
        
    def display_info(self):
        print(f"Company : {self.company}")
        print(f"Price : {self.price}")
        print(f"Color : {self.color}")
        print(f"Battery Life : {self.battery_life}hr")
        print(f"Number of Pieces : {self.number_of_piece}")
        print(f"WaterProof : {self.water_proof}")
        print(f"Battery Charge Time : {self.battery_charge_time}hr")
        print(f"Earpiece Shape : {self.earpiece_shape}")
        print(f"Material : {self.material}")
        print(f"Charging Port Type : {self.charging_type}")
        print(f"Bluetooth Range : {self.bluetooth_range}")

    def pair_device(self):
        if self.bluetooth_range > 10:
            print(f"Cannot connect. Bluetooth range exceeds 10 meters.")
            self.is_connected = False
        else:
            if not self.is_connected:
                print("Pairing device...")
                self.is_connected = True
                print(f"{self.company} device paired successfully.")
            else:
                print("Device is already paired.")

    def unpair_device(self):
        if self.is_connected:
            self.is_connected = False
            print(f"{self.company} device unpaired successfully.")
        else:
            print("Device is not paired.")

    def increase_volume(self, volume):
        if self.volume_level + volume <= 100:
            self.volume_level += volume
        else:
            self.volume_level = 100
        print(f"Volume increased to {self.volume_level}%.")

    def decrease_volume(self, volume):
        if self.volume_level - volume >= 0:
            self.volume_level -= volume
        else:
            self.volume_level = 0
        print(f"Volume decreased to {self.volume_level}%.")

    def update_bluetooth_range(self, new_range):
        self.bluetooth_range = new_range
        if self.bluetooth_range > 10 and self.is_connected:
            print("Bluetooth range exceeds 10 meters. Device is disconnected.")
            self.unpair_device()

    def check_battery(self):
        if self.battery_life > 0:
            print(f"Battery remaining: {self.battery_life} hours.")
        else:
            print("Battery is drained. Please recharge the earphones.")

    def use_battery(self, hours):
        if self.battery_life - hours >= 0:
            self.battery_life -= hours
            print(f"Used for {hours} hours. Battery remaining: {self.battery_life} hours.")
        else:
            self.battery_life = 0
            print("Battery is completely drained. Please recharge.")

    # Charging the Earphone
    def charge_battery(self, hours):
        if self.battery_life < self.battery_max_life:
            self.battery_life += hours
            if self.battery_life > self.battery_max_life:
                self.battery_life = self.battery_max_life
            print(f"Charging... Battery now at {self.battery_life} hours.")
        else:
            print("Battery is already fully charged.")
            
    def one_touch(self):
        if not self.o_touch:
            self.o_touch=True
            print("Music play")  
        else:
            self.o_touch=False
            print("Music pause")
            
    def double_touch(self):
        if not self.d_touch:
            self.d_touch=True
            print("Next Music play")
            
ep1 = Earphone("Apple", 10000, "white", 3, 2, "Yes", 3, "stick", "plastic", "Type C", 10)
ep1.display_info()
ep1.pair_device()
ep1.increase_volume(10)
ep1.decrease_volume(20)
ep1.check_battery()
ep1.use_battery(1.5) 
ep1.check_battery()
ep1.charge_battery(1)
ep1.one_touch()
ep1.double_touch()
ep1.unpair_device()
