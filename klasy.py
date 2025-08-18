class Samochod:
    def __init__(self, silnik):
        self.silnik_obiektu = silnik
        print(f"Utworzono pojazd z silnikiem: {self.silnik_obiektu}. ID obiektu to {id(self)}")

    def info(self):
        print(f"Rodzaj silnika, to: {self.silnik_obiektu}")

pojazd1 = Samochod("benzyna")
print("===============================")
pojazd1.info()