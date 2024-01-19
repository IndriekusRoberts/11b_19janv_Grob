yoo = input("Tavs vārds šeit: ")

try:
    with open("5uzd.txt", "w") as crank:
        crank.write(yoo)
except (FileExistsError, ValueError):
    print("Error: Invalid file type")
with open("5uzd.txt", "r") as sup:
    name = sup.read()

print("Labdien, " + yoo + ".")