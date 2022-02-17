handle = open(input("Enter file: ")) #opens a file typed by the user

counts = dict() # creates an empty dict
for namedline in handle: #for each line in handle
	words = namedline.split() #split the current line and store it in a list named words
	for namedword in words: #for each word in words
		counts[namedword] = counts.get(namedword, 0) + 1 #if the word is in the dict add 1 if not add it with a default value of 0

currentcount = None #the current count of the word is none
currentword = None #so is the word
for word, count in counts.items(): #for 2 variables named word and count are goint through the items  e.g [{(the) which is the current key} whose variable name is word] and {(0) count} its value
	if currentcount is None or currentcount < count: #if currentcount is None which it is start saving the results in currentword and currentcount and currentcount is storing the highest value so far comparing it to count which is looping through the dictonary values
		currentword = word #the word is always changed
		currentcount = count #if the current value is higher than currentcount currentcount is going to be replaced with the new count variable value
print(f"The most repeated word is '{currentword}' with {currentcount} repetitions") #prints all that stuff
