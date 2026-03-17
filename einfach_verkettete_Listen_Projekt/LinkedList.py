from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None # wenn leere Liste None, sonst Node(5) zB.
    def __iter__(self): # iterator protokoll implementieren
        current = self.head
        while current is not None:
            yield current.value # Gibt Wert, aber merkt wo war (braucht für "for x in liste")
            current = current.next

    def append(self, value): # value ist Ganzzahl
        new_node = Node(value)
        if self.head is None: # Fall1: Liste ist leer
            self.head = new_node
            return
        current = self.head
        while current.next is not None: # Fall2: Liste hat Elemente
            current = current.next
        current.next = new_node

    def length(self): # Ausgabe der Länge der Datenstruktur
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def ausgabe(self): # Ausgabe aller Elemente
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
