class Cell:
    """Pojedyńcza komórka w planszy sapera"""

    def __init__(self, pos_y, pos_x):
        """Inicjujemy współrzędnymi oraz domyślnie ustawiamy wartość na -1"""
        self.y = pos_y
        self.x = pos_x
        self.value = -1
        self.counter = 0

    def __str__(self):
        return 'Komorka o współrzędnych: ({};{}) i wartości: {}'.format(self.y, self.x, self.value)

    def number_of_neighboring_mines(self, board):
        """Sprawdza iloś min w otoczeniu komórki"""
        for y in range(-1, 2):
            for x in range(-1, 2):
                if y == 0 and x == 0:
                    continue
                elif (0 <= self.y + y < len(board)) and (0 <= self.x + x < len(board[self.y])):
                    if board[self.y + y][self.x + x].value == 9:
                        self.counter = self.counter + 1
                else:
                    continue
