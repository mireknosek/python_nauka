# sklep
class Produkt:
    def __init__(self, nazwa, cena, ilosc):
        self.nazwa = str(nazwa)
        self.cena = float(cena)
        self.ilosc = int(ilosc)

    def __str__(self):
        return f"{self.nazwa} | {self.cena:.2f} | {self.ilosc}"
    
    def wartosc(self):
        return f"Warość {self.nazwa} = {self.cena}"
    
    def zmien_ilosc(self, nowa_ilosc):
        self.ilosc = nowa_ilosc
        print(f"Zmieniono ilosc {self.nazwa} na {self.ilosc}")
        
class Koszyk:
    def __init__(self):
        self.zawartosc = []
        print("\nZabrałeś koszyk\n")

    def dodaj_produkt(self, produkt, ilosc):
        if not isinstance(produkt, Produkt):
            raise TypeError("Tylko produkty z magazynu")
        if produkt.ilosc - ilosc < 0:
                raise TypeError("Brak produkt")
        produkt.ilosc -= ilosc
        self.zawartosc.append(produkt)
        print(f"Dodano: {produkt.nazwa} w ilości: {ilosc} do koszyka")
        print(f"Ilosć: {produkt.nazwa} w magazynie {produkt.ilosc}")
        print(produkt)

    def usun_produkt(self, produkt, ilosc):
        if isinstance(produkt, Koszyk):
            self.zawartosc.remove(produkt)
            produkt.ilosc += ilosc
            print(produkt)
        else:
            print(f"Nie masz {produkt} w koszyku")

               
arbuz = Produkt("arbuz", 12.60, 2)
#print(arbuz)
print(arbuz.wartosc())
arbuz.zmien_ilosc(100)

klient = Koszyk()
klient.dodaj_produkt(arbuz, 10)

klient.usun_produkt(arbuz, 44)