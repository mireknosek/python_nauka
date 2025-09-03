class Magazyn:
    def __init__(self, produkt, ilosc):
        self.produkt = produkt
        self.ilosc = ilosc
        print(f"\nDodano {self.produkt}, szt. {self.ilosc} do magazynu")

p1 = Magazyn("mlotek", 20)