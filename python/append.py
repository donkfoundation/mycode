notes = []
num1 = int(input('> '))
num2 = int(input('> '))
notes.append(num1)
notes.append(num2)
quantity = len(notes)
numbers = notes[0] + notes[1]
print(f"Average is: {numbers / quantity}")
