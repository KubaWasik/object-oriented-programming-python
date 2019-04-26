import time

from car import Car
from garage import Garage
from person import Person


def main():
    print("Tworzymy Janusza, obiekt klasy Person z pustą listą samochodów...")
    janusz = Person("Janusz", "Dziki", "Gdziesiowo 1A")
    time.sleep(1)
    print("Tworzymy 3 samochody Janusza oraz garaż w którym będą samochody...")
    audi = Car("Audi", "A4", 5, 1.6, "GDZ IES1", 6.5)
    volvo = Car("Volvo", "XC60", 5, 2.0, "GDZ IES2", 7.3)
    seat = Car("Seat", "Vario", 5, 1.4, "GDZ IES3", 7.0)
    janusz_garage = Garage("Gdziesiowo 1B", 3, [audi, volvo, seat])
    time.sleep(1)
    print("przypisujemy auta do Janusza...\n")
    janusz.cars = [audi.registration, volvo.registration,
                   seat.registration]
    janusz.garage = janusz_garage
    time.sleep(1)
    print(janusz)
    time.sleep(1)
    print("Sprawdzamy ile utworzyliśmy obiektów...")
    time.sleep(1)
    print("Ilość obiektów klasy Car:", Car.quantity)
    print("Ilość aut należących do Janusza:", janusz.number_of_cars, end="\n\n")
    time.sleep(1)
    print("Janusz testuje swoje autko...")
    time.sleep(1)
    print(janusz.cars[2])
    time.sleep(1)
    print(janusz.garage[2])
    time.sleep(1)
    print("\nIlość potrzebnego paliwa na trase 765 km:",
          str(janusz.garage[2].calculate_combustion(765)) + " l")
    time.sleep(1)
    print("Koszt tego paliwa (cena paliwa: 4.92 zł/l): {:.2f} zł\n\n".format(
        janusz.garage[2].calculate_fuel_price(700, 4.92)))
    time.sleep(1)
    print("Halina wrzuca na autostradzie bieg R jak RAKIETA i niszczy auto...")
    janusz.delete_car("GDZ-IES1")
    time.sleep(1)
    print("\n", janusz)
    time.sleep(1)
    print(janusz.garage)
    time.sleep(1)
    print("Ilość obiektów klasy Car:", Car.quantity, end="\n\n")
    time.sleep(1)
    print("Jakieś cwane nicponie kradną Januszowi pozostałe auta...")
    janusz.delete_car("GDZ-IES2")
    janusz.delete_car("GDZ-IES3")
    time.sleep(1)
    print(janusz)
    time.sleep(1)
    print(janusz.garage)
    time.sleep(1)
    print("Ilość obiektów klasy Car:", Car.quantity, end="\n\n")
    print("Ilość aut Janusza:", janusz.number_of_cars)


if __name__ == "__main__":
    main()
