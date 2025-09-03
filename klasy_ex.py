class Magazyn:
    produkty = []

    def __init__(self, produkt, ilosc):
        self.produkt = produkt
        self.ilosc = ilosc
        Magazyn.produkty.append(self)
        print(f"\nDodano {self.produkt}, szt. {self.ilosc} do magazynu")
    
    def __str__(self):
      return f"{self.produkt} | {self.ilosc}"

    def dodaj_produkt(self, ilosc):
       self.ilosc += ilosc
       print(f"zwiekszono stan: {self.produkt} do {self.ilosc}")

    def usun_produkt(self, ilosc):
        print(f"\nUsun_produkt: {self.produkt}")
        if self.ilosc - ilosc < 0:
          print(f"Możesz usunąć tylko: {self.ilosc} {self.produkt}")
        else:
          self.ilosc -= ilosc
          self.wyswietl_produkt()
    
    @classmethod
    def wyswietl_magazyn(cls):
        print("\nStan magazynu:")
        for p in cls.produkty:
          print(f"{p.produkt} | ilość: {p.ilosc}")    

    def wyswietl_produkt(self):
       print(f"{self.produkt}, stan: {self.ilosc}")  
        

mlotek = Magazyn("mlotek", 20)
kilof = Magazyn("kilof", 40)

mlotek.dodaj_produkt(10)
Magazyn.wyswietl_magazyn()
mlotek.usun_produkt(309)
mlotek.wyswietl_produkt()
