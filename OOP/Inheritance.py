class Car:
      def __init__(self, brand, model):
            self.brand = brand
            self.model = model

class CarSpec(Car):
      def __init__(self, brand, model, electric):
            super().__init__(brand, model)
            self.electric = electric      

class CarTheme(Car):
      def __init__(self, brand, model, theme):
            super().__init__(brand, model)
            self.theme = theme


# my_New_Car = CarSpec("Toyota", "Corolla", False)
# print(my_New_Car.brand)
# print(my_New_Car.model)
# print(my_New_Car.electric)


my_car = CarTheme("Toyota", "Corolla", "silver")
print(my_car.brand)
print(my_car.model)
print(my_car.theme)