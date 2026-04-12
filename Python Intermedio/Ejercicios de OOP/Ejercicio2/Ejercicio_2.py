import Person
class Bus:
    def __init__(self, max_passengers):
        self.passengers = []
        self.max_passengers = max_passengers
    def add_passenger(self, person: Person):
        if len(self.passengers) >= self.max_passengers:
            print(f"Lo sentimos, el máximo permitido es de {self.max_passengers} y ya el bus está lleno")
        else:
            self.passengers.append(person)
            print(f"Se subió {person.name}")
    def remove_passenger(self):
        person = self.passengers.pop()
        print(f"Se bajó {person.name}")
