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
from collections import Counter

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
        gezogene.append(pokerkarten[pzahl])
        pokerkarten[counter] = pokerkarten[pzahl]  # gezogene Zahl und counter (letzte, vorletzte, ... Zahl) wechseln Platz
        pokerkarten[pzahl] = counter
        counter -= 1
    return gezogene
def poker_ziehung():
    karten = list(range(52))   # 0–51
    counter = 51
    gezogene = []
    for i in range(5):
        i = random.randint(0, counter)
        gezogene.append(karten[i])                      # richtige Karte merken
        karten[i], karten[counter] = karten[counter], karten[i]  # Werte tauschen
        counter -= 1
    return gezogene
def farbzuordnung(karten): # 0=Pik, 1=Herz, 2=Karo, 3=Kreuz
    """farben = {}
    for karte in karten:
        farben[karte] = karten[karte] // 13 # ganzzahlig teilen für Farbe
    return farben"""
    return [karte // 13 for karte in karten]
def symbolzuordnung(karten): # 0=Ass, 1=2, 2=3, ..., 10=Bube, 11=Dame, 12=König
    """symbole = {}
    for i in range(len(karten)):
        symbole[i] = karten[i] % 13 # ganzzahlig teilen für Farbe
    return symbole"""
    return [symbol % 13 for symbol in karten]

"""
Auswertungssyntax der gezogenen Karten
"""

# Symbole und Farben zaehlen
def symbolezaehlen(symbole):
    return dict(Counter(symbole).items()) # Ausgabe von Counter: Counter({3: 3, 2: 2})
def farbenzaehlen(farben):
    return dict(Counter(farben).items())

# Paaranzahl zaehlen
def paaranzahl(symbol_anzahl):
    paar_anzahl = 0
    for anzahl in symbol_anzahl.values(): # values liefert nur Werte von Dictionary
        if anzahl == 2:
            paar_anzahl += 1
    return paar_anzahl
# Paar: Zwei Karten mit gleichem Symbol (z. B. zwei Damen)
def paar(paar_anzahl):
    return paar_anzahl == 1
# Zwei Paare: Zwei verschiedene Symbolpaare (z. B. zwei Damen und zwei Achter)
def doppelpaar(paar_anzahl):
    return paar_anzahl == 2
# Drilling: Drei Karten mit gleichem Symbol (z. B. drei Könige)
def drilling(symbol_anzahl):
    for anzahl in symbol_anzahl.values():  # values liefert nur Werte von Dictionary
        if anzahl == 3:
            return True
    return False
# Vierling (Four of a Kind): Vier Karten mit gleichem Symbol (z. B. vier Buben)
def vierling(symbol_anzahl):
    for anzahl in symbol_anzahl.values():  # values liefert nur Werte von Dictionary
        if anzahl == 4:
            return True
    return False

# Straße (Straight): Fünf aufeinanderfolgende Symbole, unabhängig von der Farbe (z. B. 5–6–7–8–9)
def strasse(symbole):
    if len(set(symbole)) != 5:  #5 verschiedene Symbole
        return False
    symbole_sortiert = sorted(set(symbole))
    # Normale Straße: 5 aufeinanderfolgende Zahlen
    ist_strasse = True
    for i in range(4):
        if symbole_sortiert[i + 1] != symbole_sortiert[i] + 1:
            ist_strasse = False
            break
    if ist_strasse:
        return True
    # Straße übers Eck: A-2-3-4-5 (als [0,1,2,3,12])
    if symbole_sortiert == [0, 1, 2, 3, 12]:
        return True
    return False

# Full House: Kombination aus Drilling und Paar (z. B. drei Damen und zwei Siebener)
def fullhouse(paar_anzahl, symbol_anzahl):
    return drilling(symbol_anzahl) and paar(paar_anzahl)

# Flush: Fünf Karten derselben Farbe (z. B. alle Pik)
def flush(farbenanzahlen):
    for i in farbenanzahlen.keys():
        if farbenanzahlen[i] == 5:  # genau 5 Karten einer Farbe
            return True
    return False
# Straight Flush: Fünf aufeinanderfolgende Karten derselben Farbe
def straight_flush(farbenanzahlen, symbole):
    return flush(farbenanzahlen) and strasse(symbole)
# Royal Flush: Die höchste Straße (10, Bube, Dame, König, Ass) derselben Farbe
def royal_flush(farbenanzahlen,symbole):
    return flush(farbenanzahlen) and sorted(set(symbole)) == [0, 9, 10, 11, 12] # set entfernt doppelte Symbole

def auswertung(royal_flush_c, straight_flush_c, vierling_c, fullhouse_c, flush_c, strasse_c, drilling_c, doppelp_c, paar_c):
    # notwendigen Variablen definieren
    karten = poker_ziehung()
    farben = farbzuordnung(karten)
    farb_anzahl = farbenzaehlen(farben)
    symbole = symbolzuordnung(karten)
    symbol_anzahl = symbolezaehlen(symbole)
    paar_anzahl = paaranzahl(symbol_anzahl)
    # auswerten
    if royal_flush(farb_anzahl, symbole):
        royal_flush_c += 1
    elif straight_flush(farb_anzahl, symbole):
        straight_flush_c += 1
    elif vierling(symbol_anzahl):
        vierling_c += 1
    elif fullhouse(paar_anzahl, symbol_anzahl):
        fullhouse_c += 1
    elif flush(farb_anzahl):
        flush_c += 1
    elif strasse(symbole):
        strasse_c += 1
    elif drilling(symbol_anzahl):
        drilling_c += 1
    elif doppelpaar(paar_anzahl):
        doppelp_c += 1
    elif paar(paar_anzahl):
        paar_c += 1
    return royal_flush_c, straight_flush_c, vierling_c, fullhouse_c, flush_c, strasse_c, drilling_c, doppelp_c, paar_c

def poker_wahr(spielanzahl): # Poker Wahrscheinlichkeiten
    royal_flush_c = 0
    straight_flush_c = 0
    vierling_c = 0
    fullhouse_c = 0
    flush_c = 0
    strasse_c = 0
    drilling_c = 0
    doppelp_c = 0
    paar_c = 0
    for i in range(spielanzahl):
        royal_flush_c, straight_flush_c, vierling_c, fullhouse_c, flush_c, strasse_c, drilling_c, doppelp_c, paar_c = \
            (auswertung(royal_flush_c, straight_flush_c, vierling_c, fullhouse_c, flush_c, strasse_c, drilling_c, doppelp_c, paar_c))
    return (f"Bei {spielanzahl} Pokerspielen ergeben sich folgende Wahrscheinlichkeiten \n"
            f"Royal Flush: {royal_flush_c/spielanzahl*100:.4f}% \n" #*100:.4f weil Prozent und 4 Kommastellen
            f"Straight_Flush: {straight_flush_c/spielanzahl*100:.4f}% \n"
            f"Vierling: {vierling_c/spielanzahl*100:.4f}% \n"
            f"Fullhouse: {fullhouse_c/spielanzahl*100:.4f}% \n"
            f"Flush: {flush_c/spielanzahl*100:.4f}% \n"
            f"Strasse: {strasse_c/spielanzahl*100:.4f}% \n"
            f"Drilling: {drilling_c/spielanzahl*100:.4f}% \n"
            f"Doppelpaar: {doppelp_c/spielanzahl*100:.4f}% \n"
            f"Paar: {paar_c/spielanzahl*100:.4f}% \n")

if __name__ == "__main__":
    pokerkarten_erstellen(52)
    zahlen_ziehung(52,5)
    print(poker_wahr(1000000))






