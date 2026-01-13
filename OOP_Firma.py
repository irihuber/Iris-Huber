"""
programmiere in Python:
- UML-Klassendiagramm zeichnen
- eine Firma
- Es gibt Personen, Mitarbeiter, Abteilungsleiter
- Es gibt mehrere Abteilungen, jede(r) Mitarbeiter ist in einer Abteilung
- Es gibt beide Geschlechter
- es gibt nur einen Abteilungsleiter pro Abteilung
- Mitarbeiter gehören immer zu einer Abteilung
- ein Abteilungsleiter ist auch ein Mitarbeiter
- modelliere die Objekte über Vererbung
- erzeuge zum Schluss ein Firmenobjekt

 programmiere folgende Methoden:
 - man muss alle Objekte instanzieren können
 - wieviele Mitarbeiter, Abteilungsleiter gibts in der Firma
 - wieviel Abteilungen gibt es
 - welche Abteilung hat die größte Mitarbeiterstärke
 - wie ist der Prozentanteil Frauen Männer

Maximiere die Logik-Kapselung...Methoden und Datenstrukturen sollten in den passenden Klassen implementiert werden.
"""
from datetime import date
from enum import Enum

class Gender(Enum):
    MALE = 1
    FEMALE = 2
class Person:
    def __init__(self,id:int,firstname:str,lastname:str,gender:Gender,birthdate:date):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.birthdate = birthdate
class Mitarbeiter(Person):
    def __init__(self,id:int,firstname:str,lastname:str,gender:Gender,birthdate:date,mail:str,abteilung):
        super().__init__(id,firstname,lastname,gender,birthdate)
        self.mail = mail
        self.abteilung = abteilung
class Abteilungsleiter(Mitarbeiter):
    pass
class Firma:
    def __init__(self, id:int, name:str, location:str, abteilung):
        self.id = id
        self.name = name
        self.location = location
        self.abteilung = abteilung

    # wie viele Mitarbeiter gibt's in der Firma
    def anzahl_mitarbeiter(self):
        anzahl = 0
        for a in self.abteilung:
            anzahl += len(a.mitarbeiter)
        return f"Mitarbeiter: {anzahl}"
    # wie viele Abteilungsleiter gibt's in der Firma
    def anzahl_abteilungsleiter(self):
        return f"Abteilungsleiter: {len(self.abteilung)}"
    # wie viele Abteilungen gibt es
    def anzahl_abteilungen(self):
        return f"Abteilungen: {len(self.abteilung)}"
    # welche Abteilung hat die größte Mitarbeiterstärke
    def abteilungen_mitarbeiter(self):
        anzahl = 0
        abt = ""
        for a in self.abteilung:
            if(len(a.mitarbeiter) > anzahl):
                anzahl = len(a.mitarbeiter)
                abt = a
        return f"{abt.name} ({anzahl} Mitarbeiter)"
    # Wie ist der Prozentanteil bei Frauen/Männern
    def frauen_maenner(self):
        m=sum(abt.anzahl_maenner() for abt in self.abteilung)
        f=sum(abt.anzahl_frauen() for abt in self.abteilung)
        return f"Prozentuelle Aufteilung: {(f/(f+m))*100}% Frauen, {(m/(f+m))*100}% Männer"

class Abteilung:
    def __init__(self, id:int, name:str, mitarbeiter, abteilungsleiter):
        self.id = id
        self.name = name
        self.mitarbeiter = mitarbeiter
        self.abteilungsleiter = abteilungsleiter
    def anzahl_mitarbeiter(self):
        return len(self.mitarbeiter)
    def anzahl_frauen(self):
        return sum(1 for m in self.mitarbeiter if m.gender == Gender.FEMALE)
    def anzahl_maenner(self):
        return sum(1 for m in self.mitarbeiter if m.gender == Gender.MALE)


# Personen
p1 = Person(0,"Tom","Turner",Gender.MALE,date(2005, 3, 15))
p2 = Person(1,"Julia","Langer",Gender.FEMALE,date(1994, 1, 30))
p3 = Person(2,"Niklas","Neumann",Gender.MALE,date(1988, 8, 2))
p4 = Person(3,"Gerhard","Grossinger",Gender.MALE,date(1990, 8, 14))
p5 = Person(4,"Susi","Singer",Gender.FEMALE,date(1994, 5, 18))
#Mitarbeiter - Abteilung IT
m1=Mitarbeiter(p5.id,p5.firstname,p5.lastname,p5.gender,p5.birthdate,"susisinger@gmail.com","IT")
m2=Mitarbeiter(p1.id,p1.firstname,p1.lastname,p1.gender,p1.birthdate,"tomturner@gmail.com","IT")
m3=Mitarbeiter(p2.id,p2.firstname,p2.lastname,p2.gender,p2.birthdate,"julialanger@gmail.com","IT")
#Mitarbeiter - Abteilung Marketing
m4=Mitarbeiter(p3.id,p3.firstname,p3.lastname,p3.gender,p3.birthdate,"nickineumann@gmail.com","MK")
m5=Mitarbeiter(p4.id,p4.firstname,p4.lastname,p4.gender,p4.birthdate,"gerhardgross@gmail.com","MK")
#Abteilungsleiter
a1=Abteilungsleiter(m4.id,m4.firstname,m4.lastname,m4.gender,m4.birthdate,m4.mail,"MK")
a2=Abteilungsleiter(m1.id,m1.firstname,m1.lastname,m1.gender,m1.birthdate,m1.mail,"IT")
#Abteilungen
it=Abteilung(0,"IT",[m1,m2,m3],a2)
mk=Abteilung(1,"MK",[m4,m5],a1)
# Firma
firma = Firma(0,"Firma","Innsbruck",[it,mk])

print(firma.anzahl_mitarbeiter())
print(firma.anzahl_abteilungsleiter())
print(firma.anzahl_abteilungen())
print(firma.abteilungen_mitarbeiter())
print(firma.frauen_maenner())