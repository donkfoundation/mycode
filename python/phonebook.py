import csv #imports working with comma separate values

with open("C:\\Users\\camie\\OneDrive\\Documentos\\Código\\VS Code\\python\\Text and csv files\\phonebook2.csv", "a") as file: #Opens the file in append mode (adds to the end) and names it value
    name = input("Name: ") #Stores in name
    number = input("Number: ") #Stores in number

    writer = csv.writer(file) #The writer method is stored in writer
    writer.writerow([name, number]) #The method writerow adds a row with the name and number (two values) as just one argument with [], because is a comma separate value (csv) 
