# paletka
class Paletka:
    ilosc = 0
    #rodzaj = "Paletka do ping ponga"

    def __init__(self, kolor, rodzaj):
        self.kolor_obiektu = kolor
        self.rodzaj_paletki = rodzaj
        Paletka.ilosc += 1
        print(f"\nStworzono paletkę nr: {Paletka.ilosc}, koloru: {self.kolor_obiektu} ID: {id(self)}")

    def info(self):
        print(f"\nKolor paletki to: {self.kolor_obiektu}, ilość: {Paletka.ilosc}, rodzaju: {self.rodzaj_paletki}, stworzono obiektow łącznie: {Paletka.ilosc}")
       
    
paletka1 = Paletka("czerwona", "ping pong")
paletka1.info()
paletka2 = Paletka("biała", "tenis")
print(f"Typ obiekt: {type(paletka1)}, metody: {dir(paletka1)}")
paletka2.info()