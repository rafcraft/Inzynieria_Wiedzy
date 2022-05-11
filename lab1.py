# zadanie 1 pobierz z konsoli swoje imie z konsoli i dodaj "cześć"
name = "Paweł"
print("cześć " + name)

print("###############")

a = 10
b = 0.1
print(str(type(name)))
print(str(type(a)))
print(str(type(b)))

lista = ["Cześć ", " jestem ", " paweł"]
lista1 = '#'.join(lista)
print(lista1)

lista2 = lista1.split()
print(lista2)

x = input("Podaj słowo: ")
print(x)
print(x.lower())
print(x.replace("Paweł", "Pawel"))
print(x.replace(" ", ""))
sett = set(x)
print(sett)
print(len(sett))

b = "Cześć"
c = "Paweł"
xyz = (b, c)
print(type(xyz))
print(x.index('Python'))

xx = ["Python", "C#", "C++", "C", "PHP"]
print(len(xx))

# #############################################################
# #Przypomnieć sobie obliczania wyznacznika macierzy w pythonie
# #############################################################

y = ["R", "Java"]
print(xx, y)
print(xx + y)
print(xx.extend(xx))

slow = {"Warszaaz":"Polska", "Moskwa":"Rosja", "Czechy":"Praga"}
print(slow.values())
sortSlow = sorted(slow.values())
print(sortSlow)

print(bool(" "))
print(bool(""))
print(bool(1))
print(bool(0))
print(bool(["", ""]))

zdanie = "Ala ma kota a kot ma ale"
zdanie2 = len(zdanie)

if "j" in zdanie:
    print("Znajduje się 'j' w zdaniu")
else:
    print("Niema 'j' w zdaniu")

for x in range(1, 11):
    print(x)

lista = ["Cześć ", " jestem ", " paweł"]
x = '#'.join(lista)
print(x)
