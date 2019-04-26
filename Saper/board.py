import random

from cell import Cell


class Board:
    """Cała plansza i funkcje opowiadające za przebieg gry"""

    def __init__(self):
        self.mines = 0
        self.hidden = 0
        self.board = []
        self.number_of_mines = 0
        self.mines = []
        while True:
            width = input('Podaj szerokość planszy (3-24): ')
            if width.isdigit():
                width = int(width)
                if width < 3 or width > 24:
                    print('\nBłąd\t-\tPodaj liczbe z przedzialu (3;24)')
                    continue
                else:
                    break
            else:
                print('\nBłąd\t-\tPodaj liczbę')
                continue
        while True:
            height = input('Podaj wysokosc planszy (3-12): ')
            if height.isdigit():
                height = int(height)
                if height < 3 or height > 12:
                    print('Podaj liczbe z przedzialu (3;12)')
                    continue
                else:
                    break
            else:
                print('\nBłąd\t-\tPodaj liczbę')
                continue
        """Inicjujemy wielkoscia planszy (wymiary height * width) i tworzymy pustą planszę"""
        self.rows = height
        self.columns = width
        self.create_board()

    def __str__(self):
        return "Obiekt klasy Board (plansza)\nWymiary: {}x{}\nLiczba min: {}".format(self.rows, self.columns,
                                                                                     self.mines)

    def create_board(self):
        """Tworzymy listę list czyli macierz Y x X i inicjujemy domyślnymi
           wartościami komórek czyli -1"""
        self.board = []
        for i in range(0, self.rows):
            self.board.append([])
            for j in range(0, self.columns):
                cell = Cell(i, j)
                self.board[i].append(cell)

    def get_number_of_mines(self):
        """Pytamy gracza ile min chce wylosować, zgodnie z treścią zadania
           z przedziału od 1 do ilosc_min - 1"""
        fields = self.rows * self.columns
        while True:
            tmp = int(input("Podaj liczbę min(1 - %d): " % (fields - 1)))
            if 1 <= tmp < fields:
                self.number_of_mines = tmp
                self.hidden = (self.rows * self.columns) - self.number_of_mines
                break
            else:
                print("Podaj wartość z przedziału od 1 do ", fields - 1)
                continue

    def deploy_mines(self):
        """Losujemy wspołrzędne dla min (sprawdzając oczywiście czy się nie
           powtarzają)"""
        for z in range(0, self.number_of_mines):
            while True:
                free = True
                row = random.randint(0, self.rows - 1)
                col = random.randint(0, self.columns - 1)
                for mine in self.mines:
                    if mine == [row, col]:
                        free = False
                        break
                    else:
                        continue
                if free:
                    self.board[row][col].value = 9
                    self.mines.append([row, col])
                    break
        self.mines.sort()

    def print_board(self):
        """Rysowanie planszy zgodnie z podpowiedzią co do funkcji chr()"""
        rows = self.rows * 2 + 1
        columns = self.columns * 2 + 1
        print("\nW\K", end='')
        for col in range(1, self.columns + 1):
            if col < 10:
                print("  %d " % col, end='')
            else:
                print("  %d" % col, end='')
        print("\n   ", end='')
        for row in range(1, rows + 1):
            for col in range(1, columns + 1):
                if row == 1:
                    if col == 1:
                        print(chr(9556), end='')
                    elif col == columns:
                        print(chr(9559), end='')
                    elif col % 2 == 0:
                        print(chr(9552), end='')
                        print(chr(9552), end='')
                        print(chr(9552), end='')
                    else:
                        print(chr(9574), end='')
                elif row % 2 == 0:
                    if col % 2 == 0:
                        if self.board[int(row / 2 - 1)][int(col / 2 - 1)].value == 9 \
                                or self.board[int(row / 2 - 1)][int(col / 2 - 1)].value == -1:
                            print("   ", end='')
                        elif self.board[int(row / 2 - 1)][int(col / 2 - 1)].value == 0:
                            print(" - ", end='')
                        else:
                            print("", self.board[int(row / 2 - 1)][int(col / 2 - 1)].value, "", end='')
                    else:
                        print(chr(9553), end='')
                elif row == rows:
                    if col == 1:
                        print(chr(9562), end='')
                    elif col == columns:
                        print(chr(9565), end='')
                    elif col % 2 == 0:
                        print(chr(9552), end='')
                        print(chr(9552), end='')
                        print(chr(9552), end='')
                    else:
                        print(chr(9577), end='')
                else:
                    if col == 1:
                        print(chr(9568), end='')
                    elif col == columns:
                        print(chr(9571), end='')
                    elif col % 2 == 0:
                        print(chr(9552), end='')
                        print(chr(9552), end='')
                        print(chr(9552), end='')
                    else:
                        print(chr(9580), end='')

            if (row + 1) % 2 == 0 and row < rows - 1:
                if int(row / 2 + 1) < 10:
                    print('\n %d ' % (int(row / 2 + 1)), end='')
                else:
                    print('\n %d' % (int(row / 2 + 1)), end='')
            else:
                print('\n   ', end='')

    def print_board_end(self, flag):
        """Rysujemy planszę gdy gracz przegra, miny zamiast pustych pól
           będą wyświetlane jako 'X' jeśli wygra to 'O' """
        rows = self.rows * 2 + 1
        columns = self.columns * 2 + 1
        print("\nW\K", end='')
        for col in range(1, self.columns + 1):
            if col < 10:
                print("  %d " % col, end='')
            else:
                print("  %d" % col, end='')
        print("\n   ", end='')
        for row in range(1, rows + 1):
            for col in range(1, columns + 1):
                if row == 1:
                    if col == 1:
                        print(chr(9556), end='')
                    elif col == columns:
                        print(chr(9559), end='')
                    elif col % 2 == 0:
                        print(chr(9552), end='')
                        print(chr(9552), end='')
                        print(chr(9552), end='')
                    else:
                        print(chr(9574), end='')
                elif row % 2 == 0:
                    if col % 2 == 0:
                        if self.board[int(row / 2 - 1)][int(col / 2 - 1)].value == 9:
                            if not flag:
                                print(" X ", end='')
                            else:
                                print(" O ", end='')
                        elif self.board[int(row / 2 - 1)][int(col / 2 - 1)].value == -1:
                            print("   ", end='')
                        elif self.board[int(row / 2 - 1)][int(col / 2 - 1)].value == 0:
                            print(" - ", end='')
                        else:
                            print("", self.board[int(row / 2 - 1)][int(col / 2 - 1)].value, "", end='')
                    else:
                        print(chr(9553), end='')
                elif row == rows:
                    if col == 1:
                        print(chr(9562), end='')
                    elif col == columns:
                        print(chr(9565), end='')
                    elif col % 2 == 0:
                        print(chr(9552), end='')
                        print(chr(9552), end='')
                        print(chr(9552), end='')
                    else:
                        print(chr(9577), end='')
                else:
                    if col == 1:
                        print(chr(9568), end='')
                    elif col == columns:
                        print(chr(9571), end='')
                    elif col % 2 == 0:
                        print(chr(9552), end='')
                        print(chr(9552), end='')
                        print(chr(9552), end='')
                    else:
                        print(chr(9580), end='')

            if (row + 1) % 2 == 0 and row < rows - 1:
                if int(row / 2 + 1) < 10:
                    print('\n %d ' % (int(row / 2 + 1)), end='')
                else:
                    print('\n %d' % (int(row / 2 + 1)), end='')
            else:
                print('\n   ', end='')

    def reveal_squares(self, y, x):
        """Rekurencyjna funkcja odsłaniająca puste pola"""
        self.board[y][x].number_of_neighboring_mines(self.board)
        if self.board[y][x].counter == 0:
            self.board[y][x].value = 0
            self.hidden = self.hidden - 1
            for pos_y in range(-1, 2):
                for pos_x in range(-1, 2):
                    if pos_y == 0 and pos_x == 0:
                        continue
                    elif 0 <= y + pos_y < self.rows:
                        if 0 <= x + pos_x < len(self.board[y]):
                            if self.board[y + pos_y][x + pos_x].value == -1:
                                self.reveal_squares(y + pos_y, x + pos_x)
        else:
            self.board[y][x].value = self.board[y][x].counter
            self.hidden = self.hidden - 1

    def game(self):
        """Główna rozgrywka - pojedyńcza gra (inaczej 1 plansza)"""
        self.get_number_of_mines()
        self.deploy_mines()
        self.print_board()
        while True:
            if self.hidden == 0:
                print('\nWygrałeś!!!')
                self.print_board_end(True)
                return True
            while True:
                y = int(input('\nPodaj wiersz: '))
                if y < 0 or y > self.rows:
                    print('Podaj liczbe z przedzialu ({};{})'.format(1, self.rows))
                    continue
                else:
                    break
            while True:
                x = int(input('\nPodaj kolumnę: '))
                if x < 0 or x > self.columns:
                    print('Podaj liczbe z przedzialu ({};{})'.format(1, self.columns))
                    continue
                else:
                    break
            if self.board[y - 1][x - 1].value == 9:
                print('\nPrzegrałeś!')
                self.print_board_end(False)
                return False
            else:
                self.reveal_squares(y - 1, x - 1)
            self.print_board()
