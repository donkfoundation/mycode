from sys import exit

for i in range(5):
	print(i)
	if i > 2:
		print("bigger than 2")
	print("done with i", i)
print("all done")

lowest = min(input("write:"))
print(lowest)

analyze = input('> ')

if analyze == 'y':
	print('Ok')
	friends = ['Sandra', 'Pamela']
	def add(friend):
		if friend in friends:
			print("You have it bro")
			add()
		else:
			friends.append(friend)
			print("You've got a new friend bro")
			add()
elif analyze == 'n':
	exit()
