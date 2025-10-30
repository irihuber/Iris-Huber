"""
Pokerkarten modellieren:
 - Liste mit 52 Elementen
 - 5 zahlen nach Lotto-Prinzip ziehen
 selbe farbe?: zahl / 13 = 0Farbe zB schwarz; symbol 11%13 ist selbes symbol?
Zahl ziehen, 5 karten ziehen, 5 farben (/13), symbole (%13), = testwerte
Flasche Zb mit set; oder for mit hochzählen paare 0-vorletztes elemt und innere aktuell äußere bis; drillinge: counter wenn counter 2 dann 3 gleiche zahlen, straße, royal slash (ist flsche und straße); ob straße übers eck dabei ist muss mit internetabgabe überprürfen
Prozentabweichung von internet eventuell
Sollte auf 2 kommazahlen an prozent aus internet kommen
"""
import random

"""
Erstellen und Ziehen der Karten
"""
def pokerkarten_erstellen(kartenanzahl):
    pokerkarten = list(range(0, kartenanzahl))
    return pokerkarten

def zahlen_ziehung(kartenanzahl,zahlen): # Ziehung von 5 Zahlen
    counter = kartenanzahl-1
    pokerkarten = pokerkarten_erstellen(kartenanzahl)
    gezogene = [] # die gezogenen Pokerzahlen
    for i in range(zahlen):  # Pokerzahlen ziehen
        pzahl = random.randint(0, counter)
        gezogene.append(pokerkarten[i])
        pokerkarten[counter] = pokerkarten[pzahl]  # gezogene Zahl und counter (letzte, vorletzte, ... Zahl) wechseln Platz
        pokerkarten[pzahl] = counter
        counter -= 1
    return gezogene
def poker_ziehung():
    karten = list(range(52))   # 0–51
    counter = 51
    gezogene = []
    for _ in range(5):
        i = random.randint(0, counter)
        gezogene.append(karten[i])                      # richtige Karte merken
        karten[i], karten[counter] = karten[counter], karten[i]  # Werte tauschen
        counter -= 1
    return gezogene
def farbzuordnung(karten): # 0=Pik, 1=Herz, 2=Karo, 3=Kreuz
    farben = {}
    for i in range(len(karten)):
        farben[i] = karten[i] // 13 # ganzzahlig teilen für Farbe
    return farben
def symbolzuordnung(karten): # 0=Ass, 1=2, 2=3, ..., 10=Bube, 11=Dame, 12=König
    symbole = {}
    for i in range(len(karten)):
        symbole[i] = karten[i] % 13 # ganzzahlig teilen für Farbe
    return symbole

"""
Auswertungssyntax der gezogenen Karten
"""
"""
Pokerkombinationen / mögliche Hände:
     • Straße (Straight): Fünf aufeinanderfolgende Symbole, unabhängig von der Farbe (z. B. 5–6–7–8–9)
     • Flush: Fünf Karten derselben Farbe (z. B. alle Pik)
     • Full House: Kombination aus Drilling und Paar (z. B. drei Damen und zwei Siebener)
     • Vierling (Four of a Kind): Vier Karten mit gleichem Symbol (z. B. vier Buben)
     • Straight Flush: Fünf aufeinanderfolgende Karten derselben Farbe
     • Royal Flush: Die höchste Straße (10, Bube, Dame, König, Ass) derselben Farbe
     • Straße „über Eck“: Spezialfall, bei dem das Ass als niedrigste Karte verwendet wird (A–2–3–4–5)
       — muss geprüft werden, ob diese Variante erlaubt ist
       """
def paarsuche(symbole): # Paare werden gesucht
    paare = {}
    counter = 0
    for i in range(len(symbole)):
        for j in range(i + 1, len(symbole)):
            if symbole[i] == symbole[j]:
                if symbole[i] not in paare:
                    paare[symbole[i]] = 1
                if symbole[i] not in paare:
                    paare[symbole[i]] += 1
    for i in paare:
        if paare[i] == 1:
            counter += 1
    return counter

# Paar: Zwei Karten mit gleichem Symbol (z. B. zwei Damen)
def paar(counter):
    if counter == 1:
        return True
    return False
# Zwei Paare: Zwei verschiedene Symbolpaare (z. B. zwei Damen und zwei Achter)
def doppelpaar(counter):
    if counter == 2:
        return True
    return False
# Drilling: Drei Karten mit gleichem Symbol (z. B. drei Könige)
def drilling(counter):
    if counter == 3:
        return True
    return False



if __name__ == "__main__":
    pokerkarten_erstellen(52)
    zahlen_ziehung(52,5)
    karten = poker_ziehung()
    farben = farbzuordnung(karten)
    symbole = symbolzuordnung(karten)
    counter = paarsuche(symbole)
    print("Paar: ", paar(symbole))
    print("Farben: ", farben)
    print("Symbole: ", symbole)
    print("Paar: ",paar(counter))
    print("zwei Paare: ",doppelpaar(counter))
    print("Drilling: ",drilling(counter))


