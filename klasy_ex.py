class Magazyn:
    produkty = []

    def __init__(self, produkt, ilosc):
        self.produkt = produkt
        self.ilosc = ilosc
        Magazyn.produkty.append(self)
        print(f"\nDodano {self.produkt}, szt. {self.ilosc} do magazynu")
    
    def __str__(self):
      return f"{self.produkt} | {self.ilosc}"

    def dodaj_produkt(self, produkt, ilosc):
       self.ilosc += ilosc
       print(f"zwiekszono stan: {produkt} do {self.ilosc}")  

    def wyswietl_magazyn(cls):
        print("\nStan magazynu:")
        for p in cls.produkty:
          print(f"{p.produkt} | ilość: {p.ilosc}")      
        

p1 = Magazyn("mlotek", 20)
p2 = Magazyn("kilof", 40)

p1.dodaj_produkt("mlotek", 0)

p1.wyswietl_magazyn()