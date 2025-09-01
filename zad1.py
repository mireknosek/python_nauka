# liczby

class Numbers:
    
    def __init__(self):
        self.count = 0

    def number(self):
        while True:
            try:
                l = float(input("Podaj liczbę float: "))
                self.count += 1
                print(f"Obiekt nr.: {self.count} to: {l}")
                return l
         
            except ValueError:
                print("Złą liczba! Spróbuj ponownie.")

numer = Numbers()
n1 = numer.number()
n2 = numer.number()   