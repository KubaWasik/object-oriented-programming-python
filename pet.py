import sys


class Pet:
    """Główny zwierz, statystyki i metody wpływające na zwierza"""

    def __init__(self, name="Miluś", hunger=0, tiredness=0):
        self.name = name
        self.hunger = hunger
        self.tiredness = tiredness
        self.mood = "szczęśliwy"

    def __str__(self):
        return "\nZwierz {}\nGłód: {}\nZmęczenie: {}".format(
            self.name, self.hunger, self.tiredness)

    def get_passage_of_time(self):
        self._passage_of_time()

    def _passage_of_time(self):
        self.hunger += 1
        self.tiredness += 1
        if (self.hunger + self.tiredness) < 5:
            self.mood = "szczęśliwy"
        elif (self.hunger + self.tiredness) <= 10:
            self.mood = "zadowolony"
        elif (self.hunger + self.tiredness) <= 15:
            self.mood = "podenerwowany"
        elif (self.hunger + self.tiredness) > 15:
            self.mood = "wściekły"

    def talk(self):
        self.get_passage_of_time()
        print("\nZwierz {} jest {}".format(self.name, self.mood))

    def eat(self, food=4):
        self.get_passage_of_time()
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        self.get_passage_of_time()
        self.tiredness -= 4
        if self.hunger < 0:
            self.hunger = 0


class Menu:
    """Menu"""

    def __init__(self):
        print("Witaj w symulatorze życia zwierza")
        name = input('Podaj imię dla swojego zwierza: ')
        self.pet = Pet(name)
        self.options = {'1': self.pet.talk,
                        '2': self.feed,
                        '3': self.fun,
                        '4': self.quit_simulator}
        self.run()

    def feed(self):
        while True:
            food = int(input('''\nCzym chcesz nakarmić zwierza?

    1. Soczystą trawką
    2. Pyszną marchewką
    3. Najwyższej jakości karmą dla każdego dzikiego zwierza
    4. KISIEL!!!

    Twój wybór: '''))
            if 0 < food < 5:
                break
            else:
                print("\nNie ma takiej opcji")
                continue
        self.pet.eat(food + 1)
        print("\nZwierz {} jest najedzony".format(self.pet.name))

    def fun(self):
        while True:
            choice = int(input('''\nJak chcesz rozbawić zwierza?

    1. Pobiegaj z nim
    2. Gili, gili
    3. Polowanie na motyle
    4. Popływaj z nim

    Twój wybór: '''))
            if 0 < choice < 5:
                break
            else:
                print("\nNie ma takiej opcji")
                continue
        self.pet.play()
        print("\nZwierz {} jest ucieszony".format(self.pet.name))

    def show_menu(self):
        string = '''
        1 - Pokaż informacje o Twoim zwierzu
        2 - Nakram zwierza
        3 - Pobaw się z zwierzem 
        4 - Zakończ
        '''
        print(string)

    def run(self):
        while True:
            self.show_menu()
            option = input('Twój wybór: ')
            if int(option) == 0:
                print(self.pet)
                continue
            action = self.options.get(option)
            if action:
                action()
            else:
                print('\nNie ma takiej opcji!')

    def quit_simulator(self):
        sys.exit()


if __name__ == "__main__":
    main = Menu()
