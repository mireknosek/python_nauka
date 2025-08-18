class Samochod:
    def __init__(self, model, kolor, silnik):
        self.model = model
        self.kolor = kolor
        self.silnik = silnik
        print(f"Powstał samochód: {model}, {kolor}, {silnik}")
    def opis(self):
        print(f"Samochód: {self.model} o kolorze: {self.kolor}\n")
    def porownaj_silnik(self, obiekt):
        if self.silnik == obiekt.silnik:
            print("te same silniki")
        else:
            print("inne silniki")

def kolor(obiekt):
    print(f"Samochód: {obiekt.model}, a kolor to:  {obiekt.kolor}")
def porownaj(obiekt1 , obiekt2):
    if obiekt1.silnik == obiekt2.silnik:
        print("Te same silniki")
    else:
        print("inne silniki")


sam1 = Samochod("Fiat", "czerwony", "benzyna")
sam2 = Samochod("Audi", "czarny", "diesel")

sam1.opis()
sam2.opis()
kolor(sam1)
#porownaj(sam1, sam2)
sam1.porownaj_silnik(sam2)