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

suma = Liczby()
suma.liczba()

        