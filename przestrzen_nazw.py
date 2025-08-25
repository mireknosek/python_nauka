a = [10]
def funkcja_A():
    print(f"Wewnątrz A: {a} - ID: {id(a)}")

def funkcja_B():
    a[0] = 20
    print(f"Wewnątrz B: {a} - ID: {id(a)}")

funkcja_A()
funkcja_B()
