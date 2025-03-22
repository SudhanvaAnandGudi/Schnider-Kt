class Mobile:
    def __init__(self, price, version):
        self.price = price
        self.version = version
    def  type(self):
        print(f"price: {self.price}, version: {self.version}")
        

class brand(Mobile):
    
    def samsung(self):
        self.type()
        print("This is Samsung info")

class OS(brand):
    def Android(self):
        self.samsung()
        print("this is android OS")
        

phone = OS("23000","2.0")
phone.Android()