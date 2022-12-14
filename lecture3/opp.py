class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

emirates = Flight(5)

people = ["Harry", "Ron", "Hermione","Marcus","George", "Gabriel", "Micheal"]

for person in people:
    if emirates.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"Flight full, can't add {person}")


