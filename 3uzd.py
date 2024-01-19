yoo = open("3uzd.txt", "r", encoding='UTF-8')
rows = yoo.readlines()
if len(rows) >= 3:
    print(rows[2])



