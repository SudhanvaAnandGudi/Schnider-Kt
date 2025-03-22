class Mobile:
    def __init__(self,price,version):
        self.price = price
        self.version = version

    def  type(self):
        print(f"price: {self.price}, version: {self.version}")
        

class brand:
    # def __init__(self, samsung_ver):
    #     self.samsung_ver = samsung_ver

    def samsung(self):
        print("this is samsung")

class OS(Mobile,brand):
    def Android(self):
        self.samsung()
        self.type()
        print("this is android OS")
phone = OS("23000","2.0")
phone.Android()