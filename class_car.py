class Car:
    def __init__(self, make_pm: str, model_pm: str, year_pm: int, mileage_pm: int):
        self.make = make_pm
        self.model = model_pm
        self.year = year_pm
        self.__mileage = mileage_pm

    def drive(self, distance: int):
        self.__mileage += distance

    def get_mileage(self):
        print(self.__mileage)

class Fleet:
    def __init__(self):
        self.list_cars = []

    def add_car(self, new_car: Car):
        self.list_cars.append(new_car)

    def remove_car(self, make, model):
        for item in self.list_cars:
            if item.make == make and item.model == model:
                self.list_cars.remove(item)

    def cars(self):
        print(self.list_cars)


car1 = Car('mercedes', 'zaychik', 2014, 3000)
car2 = Car('daewoo', 'matiz', 2009, 1500)



fl1 = Fleet()

fl1.add_car(car1)
fl1.cars()
car2.drive(100)
fl1.add_car(car2)
fl1.cars()
fl1.remove_car('daewoo', 'matiz')
fl1.cars()
