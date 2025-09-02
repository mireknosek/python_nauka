# bank_account.py
import random

class Rachunek:
    def __init__ (self, imie, coast):
        self.imie = imie
        self.coast = coast
        self.number = random.randint(10**11, 10**12 -1)
        print(f"\n* Rachunek o nr : {self.number} utworzono. Stan konta: {self.coast} *\n")
    
    def __str__(self):
       return f"{self.imie}, {self.number}, {self.coast}"

    def stan_coast(self):
        print(f"Stan konta dla {self.imie}, wynosi: {self.coast} zł\n")

    def deposit(self, amount):
        self.coast += amount
        print(f"Wpływ na rachunek: {amount} zł")
        self.stan_coast()

    def withdraw(self, amount):
        if self.coast - amount < 0:
            print(f"Chcesz wydać {amount}, a nie masz tylu środków na rachunku!\n")
        else:
            self.coast -= amount
            print(f"Wydałeś: {amount} zł")
            self.stan_coast()
            

mirek  = Rachunek("Mirek", 100)

mirek.deposit(100)
mirek.withdraw(210)

print(mirek)