choose = input('> ')

if choose == 'largest':
	largestnumber = max(input('> '))
	print(largestnumber)
elif choose == 'lowest':
	lowestnumber = min(input('> '))
	print(lowestnumber)
else:
	print('Write largest or lowest')


