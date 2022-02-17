smallest = 100
print(f'Before: {smallest}')
for num in [23, 88, 9, 12, 30, 41, 51, 15, 2, 89]:
	if num < smallest:
		smallest = num
	print(smallest, num)
print(f'After: {smallest}')

#/////////////
print('Antoher way to do this')

smallest = None
print(f'Before: {smallest}')
for value in [23, 88, 9, 12, 30, 41, 51, 15, 2, 89]:
	if smallest is None:
		smallest = value
	elif value < smallest:
		smallest = value
	print(smallest, value)
print(f'After: {smallest}')





