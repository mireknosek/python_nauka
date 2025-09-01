# liczby

class Liczby:
    def __init__(self):
        self.count = 1

    def liczba(self):
        while True:
            try:
                l = float(input("Podaj liczbę float: "))
                print(f"Nr :{self.count} = {l}")
                self.count += 1
                return l
            except ValueError:
                print("Zła liczba")

liczba = Liczby()
l1 = liczba.liczba()
l2 = liczba.liczba()

print(l1, l2)


def pobierz_liczby(ile):
    liczby = []
    for i in range(ile):
        while True:
            try:
                l = float(input("Podaj liczbę: "))
                liczby.append(l)
                break
            except ValueError:
                print("Podaj poprwaną float!")
    return liczby

#pobierz_liczby(2)
print(pobierz_liczby(2))
