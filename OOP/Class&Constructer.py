# class Car:
#       def __init__(self, brand, model, color):
#             self.carBrand = brand
#             self.carModel = model
#             self.carColor = color

# my_Car = Car("Toyota", "Carolla", "Black")
# print("Car brand is {0}, Model is {1} and Color is {2}".format(my_Car.carBrand, my_Car.carModel, my_Car.carColor))




class Car:
      def __init__(self, brand, model, color):
            self.carBrand = brand
            self.carModel = model
            self.carColor = color

      def otherProperties(self, price, year):
            print (f"{self.carBrand}, {self.carModel}, {self.carColor}, {price}, {year}")


class ElectricCar(Car):
      def __init__(self, brand, model, color, price, year, batterySize):
            super().__init__(brand, model, color,)
            self.batterySize = batterySize
           
# my_car = Car("Toyota", "Carolla", "Black")
# my_car.otherProperties(20000, 2022)
my_car = ElectricCar("Tesla", "Model S", "Red", 200000, 2022, "85kWh")
print(my_car.batterySize)
my_car.otherProperties(20000, 2022)
