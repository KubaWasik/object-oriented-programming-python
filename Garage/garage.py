class Garage:
    """Klasa Garage zawierająca informacje o garażu i samochodach w nim"""

    def __init__(self, address="Nieznany", capacity=1, cars=None):
        self.address = address
        self.capacity = capacity
        if cars is None:
            cars = []
        if len(cars) <= self.capacity:
            self.cars = cars
        else:
            self.cars = []
            print("Brak miejsca w garażu na tyle samochodów, ustawiono pusty")

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
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, new_capacity):
        if new_capacity > 0:
            self._capacity = new_capacity
        else:
            print("Pojemność musi być liczbą dodatnią!\nUstawiono 1")
            self._capacity = 1

    @property
    def cars(self):
        return self._cars

    @cars.setter
    def cars(self, new_cars):
        if len(new_cars) <= self.capacity:
            self._cars = new_cars
        else:
            self.cars = []
            print("Brak miejsca w garażu na tyle samochodów, ustawiono pusty")

    def __getitem__(self, position):
        return self._cars[position]

    def __setitem__(self, position, car):
        self._cars[position] = car

    def __delitem__(self, position):
        del self.cars[position]

    def add_car(self, new_car):
        if len(self.cars) + 1 <= self.capacity:
            self.cars.append(new_car)
        else:
            print("Garaż pełny")

    def __repr__(self):
        values = ', '.join(('{} = {!r}'.format(k.lstrip('_'), v)
                            for k, v in self.__dict__.items()))
        return '{}({})'.format(self.__class__.__name__, values)

    def __str__(self):
        str1 = "Adres:\t\t{0.address}\nPojemność:\t{0.capacity}".format(self)
        str2 = "\n\nSamochody w garażu:"
        for car in self.cars:
            str2 += str(car.__str__())
            str2 += "\n"
        if not self.cars:
            str2 += "\nGaraż pusty\n"
        return str1 + str2


if __name__ == "__main__":
    print(Garage.__doc__)
