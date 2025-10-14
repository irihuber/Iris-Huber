import random

def ziehung(d): # führt das Ziehen der 6 Lottozahlen durch
    counter = 44
    maxzahl = 46
    zahlen = 6
    numbers = list(range(1, maxzahl))  # [1, 2, 3, 4, ..., 45]
    for j in range(zahlen):  # Lottozahlen ziehen
        lzahl = random.randint(0, counter)
        numbers[counter] = numbers[lzahl]  # gezogene Zahl und counter (letzte, vorletzte, ... Zahl) wechseln Platz
        numbers[lzahl] = counter
        counter -= 1
        d[lzahl + 1] += 1  # Zahl an dieser Stelle wurde als Lottozahl gezogen

def wiederholung(): # Ziehung wird 1000 Mal durchgeführt um zu sehen wie oft die Zahlen jeweils aufgerufen wurden
    ziehungen = 1000
    maxzahl = 46
    d = {i: 0 for i in range(1, maxzahl)}  # {1:0,2:0,3:0,4:0,5:0,6:0,7:0,...,45:0}
    for i in range(ziehungen):
        ziehung(d)
    return d


if __name__ == "__main__":
    print(wiederholung())