# paletka
class Paletka:
    ilosc = 0
    __rodzaj = "Paletka do ping ponga"

    def __init__(self, kolor):
        self.kolor_obiektu = kolor
        Paletka.ilosc += 1
        print(f"\nStworzono paletkę nr: {Paletka.ilosc}, koloru: {self.kolor_obiektu} ID: {id(self)}")

    def info(self):
        print(f"\nKolor paletki to: {self.kolor_obiektu}")
        print(f"W klasie : {Paletka.__rodzaj}, stworzono obiektow łącznie: {Paletka.ilosc}")
    def zmien_rodzaj(self, nowy_rodzaj):
        Paletka.__rodzaj = nowy_rodzaj
        print(f"Zmieniono rodzaj paletki na {self.__rodzaj}")
    
paletka1 = Paletka("czerwona")
paletka1.info()
paletka2 = Paletka("biała")
print(f"Typ obiekt: {type(paletka1)}, metody: {dir(paletka1)}")
paletka2.info()
paletka1.zmien_rodzaj("Tenis")
print("---------------")
paletka1.info()