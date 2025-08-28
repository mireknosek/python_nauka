# dodawanie
def dodaj():
    while True:
        try:
            liczba = float(input("Podaj liczbę INT: "))
            return liczba
            break
        except ValueError:
            print("Podaj liczbę !")

liczba1 = dodaj()
liczba2 = dodaj()
print(f"Suma {liczba1} + {liczba2} = {liczba1 + liczba2}")