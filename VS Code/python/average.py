
lista = []
while True:
	inp = input('Enter number: > ')
	if inp == 'done' or inp == 'Done':
		break
	value = int(inp)
	lista.append(value)

average = sum(lista) / len(lista)
print(f'The average is {average}')

