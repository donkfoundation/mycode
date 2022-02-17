while True:
    filetry = input('enter file name: ')
    if filetry == 'exit' or filetry == 'quit':
        quit()
    try: 
        file = open(filetry)
        break
    except:
        print("Enter a valid file name!")
        continue
        
count = 0
for line in file:
    count = count + 1
print(f"there were {count} lines")
