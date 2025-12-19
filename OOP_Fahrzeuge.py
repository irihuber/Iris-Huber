class Fahrzeug:
    def __init__(self, hersteller, baujahr):
        self.hersteller = hersteller
        self.baujahr = baujahr
    def starten(self):
        return 'Fahrzeug wird gestartet.'
    def __str__(self):
        return (f'Hersteller: {self.hersteller}'
                f'\nBaujahr: {self.baujahr}')

class Motorfahrzeug(Fahrzeug):
    def __init__(self, hersteller, baujahr, motorleistung, kraftstoffart):
        super().__init__(hersteller, baujahr)
        self.motorleistung = motorleistung
        self.kraftstoffart = kraftstoffart
    def starten(self):
        return f'Fahrzeug mit Motorleistung {self.motorleistung} wird gestartet.'
    def verbrauch_berechnen(self, kilometer, durchschnittsverbrauch):
        return f'Verbrauch für {kilometer} km ist {(kilometer/100)*durchschnittsverbrauch} Liter'

class Motorrad(Motorfahrzeug):
    def __init__(self, hersteller, baujahr, motorleistung, kraftstoffart, hat_beiwagen):
        super().__init__(hersteller, baujahr, motorleistung,kraftstoffart)
        self.raeder = 2
        self.hat_beiwagen = hat_beiwagen
    def __str__(self):
        return (f'Hersteller: {self.hersteller}'
                f'\nBaujahr: {self.baujahr}'
                f'\nKraftstoffart: {self.kraftstoffart}'
                f'\nMotorleistung: {self.motorleistung}'
                f'\n Anzahl der Räder: {self.raeder}'
                f'\n Beiwagen: {self.hat_beiwagen} ')
    def wheelie(self):
        return 'Das Motorrad macht einen Wheelie'


if __name__ == "__main__":
    motorrad = Motorrad(
        hersteller="Yamaha",
        baujahr=2020,
        motorleistung=150,  # PS
        kraftstoffart="Benzin",
        hat_beiwagen=False
    )
    print("--- Motorrad: ---")
    print(motorrad)
    print("Motorrad starten: ",motorrad.starten())
    print("Verbrauch berechnen:",motorrad.verbrauch_berechnen(150,5))
    print("Wheelie: ",motorrad.wheelie())
