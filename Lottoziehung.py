#1000 mal Lottoziehung
#dictionary (werte 1-45), schlüssel von jeweiliger gezogenen Lottozahl wird +1 gesetzt
# Zahl von random stelle mit zahl an letzter, vorletzter, ... stelle tauschen -> shuffeln
import random

d = {i: 0 for i in range(1, 46)}   #{1:0,2:0,3:0,4:0,5:0,6:0,7:0,...,45:0}
z1=0
z2=0

for z in range(1000):
    zahlen = list(range(1, 46))  # [0, 1, 2, 3, 4, ..., 45]
    zaehler = 44
    for z in zahlen: # liste mit durchgeschaffelten zahlen
        rdnzahl = random.randint(0, zaehler)
        z1=zahlen[zaehler]
        z2=zahlen[rdnzahl]
        zahlen[zaehler] = z2
        zahlen[rdnzahl] = z1
        zaehler -= 1
    for i in range(6): # 6 Lottozahlen ziehen
        lzstelle = random.randint(0, len(zahlen)-1) # stelle wird von zahlen gewählt
        lzahl = zahlen[lzstelle] # lottozahl ist wo rnd stelle gewählt wurde
        d[lzahl] += 1 # Zahl +1 zählen
print(d)