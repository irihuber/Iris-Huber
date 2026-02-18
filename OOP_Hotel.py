# Bsp: Hotel mit Räumen, verwalten ob bestimmte Zimmer frei oder nicht frei sind
from enum import Enum

from Kontrollstrukturen import count


class Betttyp(Enum):
    EIN_EINZEL=0
    ZWEI_EINZEL=1
    DOPPEL_EINZEL=2
    DOPPEL=3

class Zimmer:
    def __init__ (self, nr, frei, preis, betttyp):
        self.nr = nr
        self.frei = frei
        self.preis = preis
        self.betttyp = betttyp
    def __str__(self):
        return f"Zimmer {self.nr} | {self.frei} | {self.betttyp} | {self.preis} €"

class Hotel:
    def __init__ (self, name, zimmer, adresse):
        self.name = name
        self.zimmer = zimmer
        self.adresse = adresse
    def __str__(self):
        return f"Hotel {self.name} | {self.zimmer,count} | {self.adresse} "
    def freiezimer(self, hotel):
        f_zimmer={z for z in hotel.zimmer if z.frei==True}
        print("Freie Zimmer:")
        for z in f_zimmer:
            print(z)

if __name__ == "__main__":
    z1 = Zimmer(1,True,33,Betttyp.EIN_EINZEL)
    z2 = Zimmer(2, True, 50, Betttyp.DOPPEL)
    z3 = Zimmer(3, False, 70, Betttyp.DOPPEL_EINZEL)
    h1 = Hotel("Inn-Hotel",{z1,z2,z3},"Museumsstraße 17. 6020 Innsbruck")
    print(h1.freiezimer(h1))
    print(h1)