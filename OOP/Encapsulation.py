# class Car:
#       def __init__(self, brand, model):
#             self.brand = brand
#             self.model = model

# class CarSpec(Car):
#       def __init__(self, brand, model, electric):
#             super().__init__(brand, model)
#             self.electric = electric

# class CarTheme(Car):
#       def __init__(self, brand, model, theme):
#             super().__init__(brand, model)
#             self.theme = theme


# my_New_Car = CarSpec("Toyota", "Corolla", False)
# print(my_New_Car.brand)
# print(my_New_Car.model)
# print(my_New_Car.electric)


# my_car = CarTheme("Toyota", "Corolla", "silver")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.theme)


class laptop:
    def __init__(self, brand, model, **kwargs):
        self.brand = brand
        self.model = model
        super().__init__(**kwargs)
    # def display(self):
    #     return f"Brand: {self.brand}, Year: {self.model}"


class laptopBag:
    def __init__(self, color, **kwargs):
        self.color = color
        super().__init__(**kwargs)
    # def display(self):
    #     return f"Brand: {self.brand}, Year: {self.model}"


class laptopAccessories(laptop, laptopBag):
    def __init__(self, brand, model, charge, cables, color):
        super().__init__(brand=brand, model=model, color=color)
        self.charge = charge
        self.cables = cables
        



# laptopSepc = laptop("HP", 2016,True,4)
laptopSepcAcc = laptopAccessories("HP", 2016, True, 4, "black")
# print(laptopSepc.display())
# print(laptopSepcAcc.display())
print(laptopSepcAcc.charge)
print(laptopSepcAcc.cables)