"""
- Magic methods
- len(a) = a.__len__()
- Auto Klasse erzeugen
- PS als attribut vergeben
- wenn a1 50PS hat und a2 60PS und a1+a2 rechnet soll direkt 110 ausgegeben werden
- subtraktion und multiplikation soll auf den auto-objekten möglich sein
- achtung überprüfen ob geegnete objekte addiert, subtrahiert usw. werden
- EQ,LT,GT vergleichsoperationen abbilden
- für alle magicmethods testzeilen angeben
"""
class Auto:
    def __init__(self, hersteller, baujahr, ps, sitze): # PS als attribut vergeben
        self.hersteller = hersteller
        self.baujahr = baujahr
        self.ps = ps
        self.sitze = sitze
    def __str__(self):
        return f"Diese Auto hat {self.ps} PS."
    def __add__(self, other):
        if isinstance(other, Auto): # braucht kein isinstance(self, Auto) weil self immer Auto ist weil ja Methode von Klasse Auto ist also nur dann aufgeruft wird
            return self.ps+other.ps
        else:
            return NotImplemented
    def __sub__(self, other):
        if isinstance(other, Auto):
            return self.ps-other.ps
        else:
            return NotImplemented
    def __mul__(self, other):
        if isinstance(other, Auto):
            return self.ps * other.ps
        else:
            return NotImplemented
    def __eq__(self, other):  # ==
        if isinstance(other, Auto):
            return self.ps == other.ps
        else:
            return NotImplemented
    def __lt__(self, other): # <
        if isinstance(other, Auto):
            return self.ps < other.ps
        else:
            return NotImplemented
    def __gt__(self, other):# >
        if isinstance(other, Auto):
            return self.ps > other.ps
        else:
            return NotImplemented
    def __len__(self):
        return self.ps


if __name__ == "__main__":
    a1 = Auto( hersteller="Volkswagen", baujahr=2020, ps=156, sitze=7)
    a2 = Auto(hersteller="Toyota", baujahr=2020, ps=150, sitze=5)
    print("a1+a2=", a1+a2)
    print("a1-a2=", a1 - a2)
    print("a1*a2=", a1 * a2)
    print("a1 == a2:", a1 == a2)
    print("a1 < a2=", a1 < a2)
    print("a1 > a2=", a1 > a2)
    print("Länge a1: ",len(a1))
