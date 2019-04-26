class Pupil:
    """Klasa Pupil zawierająca dane o uczniu oraz jego ocenach i wagach"""
    grades = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]

    def __init__(self, name="Nieznane", surname="Nieznane"):
        self.name = name
        self.surname = surname
        self.marks = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) >= 3 and new_name.isalpha():
            self._name = new_name
        else:
            print('Imię musi składać się z co najmniej 3 liter i ' +
                  'zawierać tylko litery\nUstawiono "Nieznane"')
            self._name = "Nieznane"

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, new_surname):
        if len(new_surname) >= 3 and new_surname.isalpha():
            self._surname = new_surname
        else:
            print('Nazwisko musi składać się z co najmniej 3 liter i ' +
                  'zawierać tylko litery\nUstawiono "Nieznane"')
            self._surname = "Nieznane"

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, new_marks):
        tmp = {}
        for mark in new_marks:
            if new_marks[mark] in Pupil.grades:
                tmp[mark] = new_marks[mark]
            else:
                print("Dla przedmiotu", mark,
                      "ocena była niepoprawna, nie dodano do dziennika!")
        self._marks = tmp

    @marks.deleter
    def marks(self):
        self._marks = {}

    def complete_marks(self, new_marks):
        tmp = {}
        for mark in new_marks:
            if new_marks[mark] in Pupil.grades:
                tmp[mark] = new_marks[mark]
            else:
                print("Dla przedmiotu", mark,
                      "ocena była niepoprawna, nie dodano do dziennika!")
        self._marks = tmp

    def print_marks(self):
        print("Oceny:\n")
        for mark in self.marks:
            print(str(mark) + ": " + str(self.marks[mark]))

    def mean(self):
        if self.marks:
            return sum(self.marks.values()) / len(self.marks.values())
        else:
            return "Dziennik jest pusty!"

    def __repr__(self):
        values = ', '.join(('{} = {!r}'.format(k.lstrip('_'), v)
                            for k, v in self.__dict__.items()))
        return '{}({})'.format(self.__class__.__name__, values)

    def __str__(self):
        description = "Imię:\t\t{0.name}\nNazwisko:\t{0.surname}\n".format(self)
        description += "Średnia ocen:\t{}".format(self.mean())
        return description


class Student(Pupil):
    def __init__(self, name="Nieznane", surname="Nieznane", weights=None):
        super().__init__(name, surname)
        if weights is None:
            weights = {}
        self.weights = weights

    @property
    def weights(self):
        return self._weights

    @weights.setter
    def weights(self, new_weights):
        tmp = {}
        for mark in new_weights:
            if isinstance(new_weights[mark], float) and (0 < float(new_weights[mark]) <= 1):
                tmp[mark] = new_weights[mark]
            else:
                print("Dla przedmiotu ", mark, " waga była niepoprawna, nie dodano do dziennika!")
        self._weights = tmp

    @weights.deleter
    def weights(self):
        self._weights = {}

    def complete_weights(self, new_weights):
        for mark in new_weights:
            if 0 < new_weights[mark] <= 1:
                self._weights[mark] = new_weights[mark]
            else:
                print("Dla przedmiotu ", mark, " waga była niepoprawna, nie dodano do dziennika!")

    def mean(self):
        if self.marks:
            avg_sum = 0.0
            avg_wei = 0.0
            for mark in self.marks:
                if mark in self.weights and self.weights[mark]:
                    avg_sum += self.marks[mark] * self.weights[mark]
                    avg_wei += self.weights[mark]
                else:
                    print("Brak wagi dla przedmiotu ", mark, "\nDodaję z wagą 0.5")
                    avg_sum += self.marks[mark] * 0.5
                    avg_wei += 0.5
            return avg_sum / avg_wei
        else:
            return "Dziennik jest pusty!"


def main():
    jozef = Pupil("Jozef", "Kowalski")
    jozef.marks = {
        "Chemia": 4.0,
        "Biologia": 3.5,
        "Matematyka": 5.5,
        "Informatyka": 6.0,
        "WF": 5.0
    }
    print(jozef)
    print()
    frank = Student("Franciszek", "Nowak")
    frank.marks = {
        "Chemia": 4.0,
        "Biologia": 3.5,
        "Matematyka": 5.5,
        "Informatyka": 6.0,
        "WF": 5.0
    }
    frank.weights = {
        "Chemia": 0.3,
        "Biologia": 0.673684,
        "Matematyka": 1.0,
        "Informatyka": 0.987654321,
        "WF": 0.4
    }
    print(frank)


if __name__ == "__main__":
    main()
