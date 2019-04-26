from garage import Garage


class Person:
    """Klasa Person zawierająca informacje o osobie"""

    def __init__(self, name="Nieznane", surname="Nieznane", address="Nieznany",
                 garage=Garage(), cars=None):
        self.name = name
        self.surname = surname
        self.address = address
        self.garage = garage
        if cars is None:
            cars = []
        self.cars = cars
        self.number_of_cars = len(cars)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if new_name:
            self._name = new_name
        else:
            print('Imię nie może być puste!\nUstawiono "Nieznane"')
            self._name = "Nieznane"

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, new_surname):
        if new_surname:
            self._surname = new_surname
        else:
            print('Nazwisko nie może być puste!\nUstawiono "Nieznane"')
            self._surname = "Nieznane"

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, new_address):
        if new_address:
            self._address = new_address
        else:
            print('Adres nie może być pusty!\nUstawiono "Nieznany"')
            self._address = "Nieznany"

    @property
    def garage(self):
        return self._garage

    @garage.setter
    def garage(self, new_garage):
        self._garage = new_garage

    @property
    def cars(self):
        return self._cars

    @cars.setter
    def cars(self, new_cars):
        if len(new_cars) <= 3:
            self._cars = new_cars
            self.number_of_cars = len(new_cars)
        else:
            print('Osoba może mieć maksymalnie 3 samochody!\nUstawiono pusty')
            self._cars = []

    def add_car(self, garage, car):
        if len(garage.cars) < garage.capacity:
            garage.add_car(car)
            self.number_of_cars += 1
            if len(self.cars) < 3:
                self.cars.append([car.registration, garage.address])
            else:
                print("Każda osoba może mieć maksymalnie 3 samochody")
        else:
            print("Garaż pełny!")

    def delete_car(self, registration):
        if registration in self.cars:
            del self.cars[self.cars.index(registration)]
            self.number_of_cars -= 1
            for car in self.garage.cars:
                if car.registration == registration:
                    car.__class__.quantity -= 1
                    del self.garage[self.garage.cars.index(car)]
                    break
            else:
                print("Brak takiego auta w danym garażu")
        else:
            print("Osoba nie ma przypisanego takiego auta")

    def __repr__(self):
        values = ', '.join(('{} = {!r}'.format(k.lstrip('_'), v)
                            for k, v in self.__dict__.items()))
        return '{}({})'.format(self.__class__.__name__, values)

    def __str__(self):
        str1 = "Imię:\t\t{0.name}\nNazwisko:\t{0.surname}\n".format(self)
        str2 = "Adres:\t\t{0.address}\n\nSamochody:\n".format(self)
        str3 = ""
        for auto in self.cars:
            str3 += "\nRejestracja:\t" + auto
            str3 += "\n"
        if not self.cars:
            str3 += "Garaż pusty\n"
        return str1 + str2 + str3


if __name__ == "__main__":
    print(Person.__doc__)
