# średia ocen

import matplotlib.pyplot as plt

oceny = [1, 2, 4, 2, 6, 6, 6, 6, 6]

def srednia_ocen(oceny):
    if type(oceny) is not list:
        return f"Niewłaściwy format: {type(oceny)}"
    suma = sum(oceny)
    if  oceny.count(5) > 4 or oceny.count(6) > 4:
        suma += 4
    srednia = suma / len(oceny)
    return round(srednia, 2)
wystepowanie = [oceny.count(x) for x in range(1, len(oceny))]
print(f"oceny: {oceny}")
print(f"występowanie: {wystepowanie}")

def wykres(wystepowanie):
    plt

for i in range (1, 7):
    if oceny.count(i)>0:
        print(f"Ocena {i} występuje {oceny.count(i)} razy" )
    
#print(srednia_ocen([1, 2, 4, 2, 6, 6]))#
#print(srednia_ocen([1, 2, 4, 2, 6, 6, 6, 6, 6]))