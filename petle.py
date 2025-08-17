class Paletka:
    def __init__(self, kolor):
        self.kolor_obiektu = kolor
        print(f"Utworzyliśmy napis o kolorze: {self.kolor_obiektu} ID: {id(self)}")
    
    def info(self):
        print(f"Kolor dla obiektu: {self.kolor_obiektu}")
              
    def info_ex(self, nazwa):
        print(f"Kolor dla obiektu {nazwa}, to {self.kolor_obiektu}")

paletka_a = Paletka("czerwony")
paletka_b = Paletka("niebieski")
print(paletka_a)
paletka_a.info()
print("====================================")
print(paletka_b.info_ex)
