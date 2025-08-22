zmienna_a = 10
def funkcja_A():
    print("Funkcja_A")
    print(f"Wewnątrz A: {zmienna_a}   ID: {id(zmienna_a)}")

def funkcja_B():
    global zmienna_a
    print("Funkcja_B")
    zmienna_a = 20
    print(f"Wewnątrz B: {zmienna_a}   ID: {id(zmienna_a)}")

#Test
print(f"Wartośc początkowa: {zmienna_a}  ID: {id(zmienna_a)}")

funkcja_A()
funkcja_B()

print(f"Wartośc końcowa: {zmienna_a}  ID: {id(zmienna_a)}")