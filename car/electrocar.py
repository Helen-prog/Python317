# from car import carclass
from car.carclass import CarClass


# class ElecroCar(carclass.CarClass):
class ElecroCar(CarClass):
    def __init__(self, brand, model, year, run):
        super().__init__(brand, model, year, run)
        self.battery = 100

    def description_battery(self):
        print(f"Этот автомобиль имеет мощность {self.battery} %")
