stations = {
"la estrella": 1,
"sabaneta": 2,
"itagui": 3,
"envigado": 4,
"ayura": 5,
"aguacatala": 6,
"poblado": 7,
"industriales": 8,
"exposiciones": 9,
"alpujarra": 10,
"san antonio": 11,
"parque berrio": 12,
"prado": 13,
"hospital": 14,
"universidad": 15,
"caribe": 16,
"tricentenario": 17,
"acevedo": 18,
"madera": 19,
"bello": 20,
"niquia": 21
}

while True:
	currentstation = input("Where are you?\n>").lower()
	destinystation = input("Where do you wanna go?\n>").lower()
	if currentstation not in stations or destinystation not in stations:
		print(">>Revisa tu escritura w\n")
	else:
		break
if stations[currentstation] < stations[destinystation]:
	difference = stations[destinystation] - stations[currentstation]
	print(f"Go to the north in Niquia direction, {difference} stations")
elif stations[currentstation] > stations[destinystation]:
	difference = stations[currentstation] - stations[destinystation]
	print(f"Go to the south in La Estrella direction, {difference} stations")
else:
	print("You already here")

