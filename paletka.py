class Paletka:
    ilosc = 0
    def __init__(self, kolor):
        Paletka.ilosc += 1
        self.kolor_paletki = kolor
        print(f"Utworzono paletkę nr: {Paletka.ilosc} ID obiektu: {id(self)}")
    
    def __del__(self):
        Paletka.ilosc -= 1
        print(f"Usunięto obiekt ID: {id(self)}")

    def info(self):
        print("----------------------------------")
        print(f"Kolor dla obiektu to: {self.kolor_paletki}")
        print(f"w klasie jest obiektów: {Paletka.ilosc}")

paletka_a = Paletka("Red")
paletka_b = Paletka("Green")

paletka_a.info()
paletka_b.info()

del paletka_b

paletka_a.info()
paletka_b.info()