usint = input("number:" )
try:
	usintint = int(usint)
except:
	print("type a number")
print("first", usintint)

usint = "123"
try:
	usintint = int(usint)
except:
	usintint = 2
print("second", usintint) 
