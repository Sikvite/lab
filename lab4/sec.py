file = open('book.txt', "r")
data = file.read()
nubchar = len(data)
data2 = file.read().replace(" ", "")
nubochar = len(data2)
print(nubchar)
print(nubochar)

