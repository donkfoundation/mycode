def lol():
	first_number = -1
	print('before', first_number)
	for the_number in [21, 12, 24, 37, 12, 81, 12, 99, 2]:
		if the_number > first_number:
			first_number = the_number
		print(first_number, the_number)
	print('after', first_number)

def write(text):
	print(text)

