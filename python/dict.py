count = {} #empty dict
names = ["asd", "zxc", "qwerty", "asd", "zxc"] #words we'll go through
for name in names:
	if name not in count: #if current item in names is not in count add it and give it a value of 1
		count[name] = 1
	else:
		count[name] +=1 #if it's sum 1 to it
print(f"The total is: {count}")

######### another way of doing it

cuenta = dict() #empty dict
nombres = ["sdf", "xcv", "wertyu", "sdf", "xcv"] #list of words
for nombre in nombres:
	cuenta[nombre] = cuenta.get(nombre, 0) + 1
	print(cuenta)
print(f"Total: {cuenta}")
