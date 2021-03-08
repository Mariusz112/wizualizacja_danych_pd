# Mariusz Raś

# zad1
lista = ["film1", "film2", "film3", "film4", "film5"]
lista.sort(reverse=True)
lista2 = ["film6", "film7", "film8", "film9", "film10"]
lista.extend(lista2)
print(lista)
# zad2
slownik = {
    "film1": "Cos",
    "rezyser": "Ktos",
    "aktor": "Ktosiowa",
    "rok": 2021
}
print(slownik)
# zad3
slownik1 = {
    "komputerowe wspomaganie programowania": "CAD",
    "Wizualizacja danych": "WD",
    "Przedmioty humanizujące": "PH",
    "Język angielski": "j.ang",
    "Rachunek różniczkowy i całkowy": "RRIC",
    "Elementy matematyki dyskretnej": "EMD",
    "Programowanie strukturalne": "PS"
}
elementslownik1 = len(slownik1)
print(elementslownik1)

# zad4
liczba = int(input("program wczyta liczbę dowolnego typu i podniesie ją do tej samej potęgi"))
x = pow(liczba, liczba)
print(x)

# zad5
print('podaj ciag znakow, program zliczy wystapienia litery a')
ciag = input()
zad5 = ciag.count('a')
print(zad5)

# zad6
print('Podaj 3 liczby calkowite program sprawdzi czy liczba a jest parzysta oraz czy jednocześnie b>c ')
a = int(input("podaj a"))
b = int(input("podaj b"))
c = int(input("podaj c"))
if a % 2 == 0 and b > c:
    print("podane liczby spelniaja warunek")
else:
    print("podane liczby nie spelniaja warunku")

#zad7
print("podaj 2 liczby, program je zsumuje ")
q = int(input("podaj q"))
w = float(input("podaj w"))
i = 1
while i < 2:
  print(q+w)
  i += 1

# zad8
print("Program wczyta 10 liczb, ale doda do listy tylko liczby calkowite")
S = input()
L = []
i = 0
while i < 10:
    L.append(S)
    S = input()
    i += 1
print(L)
list_2 = [x for x in L if type(x) == int]
'''
# zad9 nie wiem
zad8 = [1,2,3,4,5,6]
for x in zad8:
  print(x)
'''
# zad10
print("Program wczyta znak i sprawdzi czy jest liczba")
def check_is_digit(input_str):
    if input_str.strip().isdigit():
        print("Podany znak to liczba")
    else:
        print("Blad, podany znak nie jest liczba")
num1 = input("Wprowadz znak")
check_is_digit(num1)