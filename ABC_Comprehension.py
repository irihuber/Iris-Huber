
def abc_comprehension():
    # dictionary comprehension, Schlüssel ist alle Buchstaben von ABC und Values ist die laufende Nummer vom ABC
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    ergebnis = {abc[i]: i for i in range(len(abc))}
    return ergebnis

if __name__ == "__main__":
    print("\nDictionary mit ABC:")
    print(abc_comprehension())