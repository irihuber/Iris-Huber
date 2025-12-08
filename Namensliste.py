"""
names = ["Anna", "Bernd", "Claudia", "Dirk", "Eva"]
ages = [23, 17, 34, 15, 29]
scores = [88, 92, 75, 64, 91]

Erzeuge aus diesen Listen eine gefilterte Liste von Personen, die folgende Bedingungen erfüllt:
    Alter ≥ 18 und Score ≥ 80
müssen verwendet werden:
 - zip – kombiniere die drei Listen so, dass jeder Eintrag ein Tupel (name, age, score) ist.
 - filter + lambda – filtere alle Personen heraus, die beide Bedingungen erfüllen.
 - map + lambda – forme jedes Tupel in ein Dictionary der Form {"name": ..., "age": ..., "score": ...} um.
   {"name": "Anna", "age": 23, "score": 88}
"""

def filtern(ages, scores, names):
    werte = zip(ages, scores, names)
    return list(filter(lambda wert: wert[0]>= 18 and wert[1]>= 80 and wert[2], werte))


def umstrukturieren(gefiltert):
    return list(map(lambda w: {"name":w[2], "age":w[0], "score":w[1]}, gefiltert))


if __name__ == "__main__":
    names = ["Anna", "Bernd", "Claudia", "Dirk", "Eva"]
    ages = [23, 17, 34, 15, 29]
    scores = [88, 92, 75, 64, 91]
    gefiltert = filtern(ages, scores, names)
    print(umstrukturieren(gefiltert))

