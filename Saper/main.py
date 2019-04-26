from board import Board


def main():
    print('Witaj w grze saper')
    # Tworzymy pierwszą planszę
    game = Board()
    won = 0
    lost = 0
    # funkcja game zwaraca True jeśli gracz wygra lub False jeśli przegra
    result = game.game()
    # dodajemy do statystyk wygraną lub przegraną
    if result:
        won = won + 1
    elif not result:
        lost = lost + 1
    else:
        print('Błąd...')
    print('\n\nWygranych:', won, '\nPrzegrane:', lost)
    # pętla dalszej rozgrywki aż do momentu jak gracz zechce zakończyć
    while True:
        choose = input('Czy chcesz zagrać ponownie(tak/nie): ')
        if choose == 'tak':
            # usuwam cały obiekt klasy, właściwie to nie wiem czy to dobrze robię
            del game
            # tworzę następną planszę (inną oczywiście)
            game = Board()
            result = game.game()
            if result:
                won = won + 1
            elif not result:
                lost = lost + 1
            else:
                print('Błąd...')
                break
            continue
        elif choose == 'nie':
            break
        else:
            print('Wpisz \"tak\" aby zagrać ponownie lub \"nie\" aby zakończyć')
            continue
    # jeśli gracz się znudził to kończymy grę i wypisujemy wyniki
    print('\nKoniec gry\nWygranych:', won, '\nPrzegrane:', lost)


if __name__ == "__main__":
    main()
