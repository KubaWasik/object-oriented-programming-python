import re


class Car:
    """Klasa Car zawerająca informacje o samochodzie"""
    quantity = 0

    def __init__(self, brand="Nieznana", model="Nieznany", doors=0,
                 engine_capacity=1.0, registration="Nieznany",
                 average_combustion=1.0):
        self.brand = brand
        self.model = model
        self.doors = doors
        self.engine_capacity = engine_capacity
        self.registration = registration
        self.average_combustion = average_combustion
        self.__class__.quantity += 1

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, new_brand):
        if new_brand:
            self._brand = new_brand
        else:
            print('Marka nie może być pusta!\nUstawiono "Nieznany"')
            self._brand = "Nieznany"

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new_model):
        if new_model:
            self._model = new_model
        else:
            print('Model nie może być pusty!\nUstawiono "Nieznany"')
            self._model = "Nieznany"

    @property
    def doors(self):
        return self._doors

    @doors.setter
    def doors(self, new_doors):
        if 0 <= new_doors < 10:
            self._doors = new_doors
        else:
            print("Za duża bądź za mała iloć dzrzwi! \nUstawiono 0")
            self._doors = 0

    @property
    def engine_capacity(self):
        return self._engine_capacity

    @engine_capacity.setter
    def engine_capacity(self, new_engine_capacity):
        if new_engine_capacity > 0:
            self._engine_capacity = new_engine_capacity
        else:
            print("Pojemność silnika musi być dodatnia! \nUstawiono 1")
            self._engine_capacity = 1

    @property
    def registration(self):
        return self._registration

    @registration.setter
    def registration(self, new_registration):
        new_registration = re.sub(r"[^\w\s]", '', new_registration)
        new_registration = re.sub(r"\s+", '-', new_registration)
        if new_registration and (5 < len(new_registration) < 10):
            self._registration = new_registration
        else:
            print('Niepoprawny numer rejestracyjny! \nUstawiono "Nieznany"')
            self._registration = "Nieznany"

    @property
    def average_combustion(self):
        return self._average_combustion

    @average_combustion.setter
    def average_combustion(self, new_average_combustion):
        if new_average_combustion > 0:
            self._average_combustion = new_average_combustion
        else:
            print("Średnie spalanie musi być liczną dodatnią! \nUstawiono 1")
            self._average_combustion = 1

    def calculate_combustion(self, route_length):
        return self.average_combustion * route_length / 100

    def calculate_fuel_price(self, route_length, fuel_price_per_liter):
        return self.calculate_combustion(route_length) * fuel_price_per_liter

    @staticmethod
    def number_of_class_objects():
        return Car.quantity

    def __repr__(self):
        values = ', '.join(('{} = {!r}'.format(k.lstrip('_'), v)
                            for k, v in self.__dict__.items()))
        return '{}({})'.format(self.__class__.__name__, values)

    def __str__(self):
        str1 = '\nMarka:\t\t\t{0.brand}\nModel:\t\t\t{0.model}\n'.format(self)
        str2 = 'Ilość drzwi:\t\t{0.doors}\n'.format(self)
        str3 = 'Pojemność silnika:\t{0.engine_capacity} l\n'.format(self)
        str4 = 'Numer rejestracyjny:\t{0.registration}\n'.format(self)
        str5 = 'Średnie spalanie:\t{0.average_combustion} l/100 km'.format(self)
        return str1 + str2 + str3 + str4 + str5


if __name__ == "__main__":
    print(Car.__doc__)
