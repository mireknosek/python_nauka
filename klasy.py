class Samochod:
    def __init__(self, model, kolor, silnik):
        self.model = model
        self.kolor = kolor
        self.silnik = silnik
        print(f"Powstał samochód: {model}, {kolor}, {silnik}")
    def opis(self):
        print(f"Samochód: {self.model} o kolorze: {self.kolor}")

sam1 = Samochod("Fiat", "czerwony", "benzyna")
print("\n")
sam1.opis()