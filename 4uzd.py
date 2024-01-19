
title = input("Ievadiet faila nosaukumu: ")
format = input("Ievadiet faila formātu: ")


if title.endswith("." + format):
    with open(title, "r") as kranken:
        saturs = kranken.read()
        
       
        print("Faila saturs:")
        print(saturs)
else:
    print("Nepareizs formāts vai fails neeksistē!")
