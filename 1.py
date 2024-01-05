class Car:
    # 初始化車名，品牌，價格 屬性
    def set_car_details(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

 # 顯示汽車資訊
    def display_info(self):
        print(f"車名：{self.name}，品牌：{self.brand}，價格：${self.price}")

# 建立三個 Car 物件
car1 = Car()
car1.set_car_details("Model S","Tesla","256w")
car2 = Car()
car2.set_car_details("M2","BMW","369w")
car3 = Car()
car3.set_car_details("C300","Benz","299w")


# 呼叫副函式，顯示汽車資訊
car1.display_info()
car2.display_info()
car3.display_info()
