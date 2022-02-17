import csv


#set the dictionary
houses = {
    "Hupplepuff": 0,
    "Gryffindor": 0,
    "Slytherin": 0
}

#opens and sets in "r" read mode the file and names it as file
with open("C:\\Users\\camie\\OneDrive\\Documentos\\Código\\VS Code\\python\\Text and csv files\\houses.csv", "r") as file:
    reader = csv.reader(file) #The csv method reads the file and stores it in reader
    for row in reader: #Creates a variable row and is going through each element of reader
        house = row[0] #The [0] represents the value of the row, and stores that in house
        houses[house] += 1 #Takes care of the stuff after the ":" and adds 1 to it
        print(house)

for sa in houses: #Every item reading the elements in the csv is now going through the dictionary, we can use a new variable
    #Stores the stuff ater the ":" in count
    print(f"{sa}: {houses[sa]}") #Fprints the current house and the current count
