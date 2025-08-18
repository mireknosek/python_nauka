class Samochod:
    def __init__(self, silnik):
        self.silnik_obiektu = silnik
        print(f"Utworzono pojazd z silnikiem: {self.silnik_obiektu}. ID obiektu to {id(self)}")

    def info(self, nazwa):
        print(f"Rodzaj silnika dla {nazwa}, to: {self.silnik_obiektu}")

def info2(obj, nazwa):
    print(f"Pojazd {nazwa} ma silnik {obj.silnik_obiektu}")

pojazd1 = Samochod("benzyna")
pojazd2 = Samochod("Diesel")
print("===============================")
print(info2(pojazd1, "Fiat"))