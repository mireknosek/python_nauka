class Paletka():
    ilosc = 0
    _producent = "Firma A"
    def __init__(self, kolor, rozmiar, nazwa="Nazwa domyslna"):
        self.kolor_obiektu = kolor
        self.rozmiar_obiektu = rozmiar
        self.nazwa_obiektu = nazwa
        print(f"Utworzono obiekt o kolorze {self.kolor_obiektu}, o ID: {id(self)}")
        Paletka.ilosc += 1
    def __del__(self):
        # Destruktor
        Paletka.ilosc -= 1
        #print(f"Usunięto paletkę: {self}")

    def info(self):
        print("------------------------------------")
        print(f"Nazwa obiektu: {self.nazwa_obiektu}")
        print(f"Rozmiar obiektu: {self.rozmiar_obiektu}")
        print(f"W klasie jest obiektów: {Paletka.ilosc}")

paletka_a = Paletka("Czerwony", "XL", "Strong")
paletka_b = Paletka("Niebieski", "Large", "XL")

paletka_a.info()
del paletka_a
paletka_b.info
