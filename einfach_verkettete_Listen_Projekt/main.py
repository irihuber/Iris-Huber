import random
from LinkedList import LinkedList

def ziehung(n, minimum, maximum): # Zufallszahlen ziehen/erstellen
    gezogene = []
    for i in range(n):
        gezogene.append(random.randint(minimum, maximum))
    return gezogene

def befuelle_liste(liste, zahlen):  # Liste mit Zufallszahlen befüllen
    for zahl in zahlen:
        liste.append(zahl)

def ausgabe_liste(liste):            # Ausgabe Liste
    print("Länge der Liste:", liste.length())
    print("\nAusgabe über ausgabe():")
    liste.ausgabe()
    print("\nAusgabe über Iterator:")
    for element in liste:
        print(element)

def main():
    anzahl   = 10
    minimum  = 0
    maximum  = 100
    zahlen = ziehung(anzahl, minimum, maximum)
    liste  = LinkedList()
    befuelle_liste(liste, zahlen)
    ausgabe_liste(liste)

if __name__ == "__main__":
    main()