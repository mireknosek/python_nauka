# bank_account.py
import random

class Rachunek:
    def __init__ (self, imie, coast):
        self.imie = imie
        self.coast = coast
        self.number = random.randint(10**11, 10**12 -1)
        print(f"\nRachunek o nr : {self.number} utworzono. {self.stan_coast()}")
    
    def stan_coast(self):
        print(f"Stan konta dla {self.imie}, wynosi: {self.coast} zł\n")

    def deposit(self, amount):
        self.coast += amount
        print(f"Wpływ na rachunek: {amount} zł")
        self.stan_coast()

    def withdraw(self, amount):
        if self.coast - amount < 0:
            print("Nie masz tylu środków na rachunku")
        else:
            self.coast -= amount
            print(f"Wydałeś: {amount} zł, stan rachunku {self.stan_coast()}")
            self.stan_coast
            

mirek  = Rachunek("Mirek", 100)
mirek.deposit(100)
mirek.withdraw(100)

print(mirek)