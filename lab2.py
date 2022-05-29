password = "Sztuczna inteligencja jest tak bardzo do super!"

def function(password):
    for a in password:
        if a <= 5:
            return "Hasło jest za slabe"

print("Wynik czy hasło jest silne ")
print(function(password))

a = open("notatnik.txt", 'w')
lista = ["Python", "C#", "C++", "C", "PHP", "SQL"]
for element in lista:
    a.write(element + "\n")

a.close()

b = open("notatnik.txt", 'r')
print(b.read())

li = ["Warszawa", "Gdańsk", "Poznań"]
x = map(lambda n: n[:3], li)
print(list(x))

lista_file = [".exe", ".py"]

def funkcja_do_zwracania(lista):
    wynik = []
    if lista.endswith('txt'):
        return lista

#funkcja_do_zwracania(lista_file)
