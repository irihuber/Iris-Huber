"""
# Methoden OHNE comprehension
def list_comprehension():
    # Zahlen von 1–10 jeweils Ausgabe ob "gerade" oder "ungerade"
    zahlen = []
    for i in range(1, 11):
        zahlen.append(i) # append fügt Element am Ende von Liste zu (Zahlen von 1-10)
    ergebnis = []
    for i in zahlen:
        if i % 2 == 0:
            ergebnis.append("gerade")
        else:
            ergebnis.append("ungerade")
    return ergebnis


def set_comprehension():
    # Ausschließlich gerade Zahlen von 1–10 in ein Set speichern
    ergebnis = set() # leeres Set
    for i in range(1, 11): # Zahlen von 1-10
        if i % 2 == 0: # nur gerade Zahlen: {2, 4, 6, 8, 10}
            ergebnis.add(i)
    return ergebnis


def dict_comprehension():
    # Quadratzahl der jeweiligen Zahl von 1-10 als Dictionary darstellen
    ergebnis = {i: i**2 for i in range(1, 6)}
    ergebnis = {}
    for i in range(1, 11): # Zahlen von 1-10
        ergebnis[i]= i*i # Zahl mit jeweiliger Potenz
    return ergebnis

"""
# Methoden MIT comprehension
def list_comprehension():
    # Zahlen von 1–10 jeweils Ausgabe ob "gerade" oder "ungerade"
    zahlen = [i for i in range(1, 11)]
    ergebnis = ["gerade" if i % 2 == 0 else "ungerade" for i in zahlen]
    return ergebnis


def set_comprehension():
    # Ausschließlich gerade Zahlen von 1–10 in ein Set speichern
    ergebnis = {i for i in range(1, 11) if i % 2 == 0} # nur gerade Zahlen: {2, 4, 6, 8, 10}
    return ergebnis


def dict_comprehension():
    # Quadratzahl der jeweiligen Zahl von 1-10 als Dictionary darstellen
    ergebnis = {i: i**2 for i in range(1, 11)}  # Zahl mit jeweiliger Potenz
    return ergebnis


if __name__ == "__main__":
    print("List Comprehension mit if-else:")
    print(list_comprehension())

    print("\nSet Comprehension mit if:")
    print(set_comprehension())

    print("\nDictionary Comprehension ohne if:")
    print(dict_comprehension())