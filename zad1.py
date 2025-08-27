# dodawanie
while True:
    try:
        liczba1 = int(input("Podaj liczbę INT: "))
        break
    except ValueError:
        print("Podaj liczbę !")
