class Flight():
	def __init__(self, capacity):
		self.capacity = capacity
		self.passengers = []
	def add_passengers(self, name):
		if not self.open_seats():
			return False
		self.passengers.append(name)
		return True
	def open_seats(self):
		return self.capacity - len(self.passengers)

flight = Flight(3)
people = ["Harry", "Hermione", "Ron", "Ginny"]
for person in people:
	if flight.add_passengers(person):
		print(f"{person} added to the flight")
	else:
		print(f"Couldn't add {person} to the flight")

print(flight.passengers)
