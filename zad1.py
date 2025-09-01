#

class Liczby:
    def __init__(self):
        self.count = 1
    
    def liczba(self):
        while True:
            try:
                liczba_wpr = float(input(f"POdaj liczbę float: "))
                self.count += 1
                return liczba_wpr
            except ValueError:
                print("Zła liczba")

licznik = Liczby()
l1 = licznik.liczba()
l2 = licznik.liczba()