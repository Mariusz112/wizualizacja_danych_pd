##Mariusz Raś
#zad1
lista = ["film1","film2","film3","film4","film5"]
lista.sort(reverse = True)
lista2 = ["film6","film7","film8","film9","film10"]
lista.extend(lista2)
print(lista)
#zad2
slownik =	{
    "film1": "Cos",
    "rezyser": "Ktos",
    "aktor": "Ktosiowa",
    "rok": 2021
}
print(slownik)
#zad3
slownik1= {
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
##zad4
liczba = int(input("program wczyta liczbę dowolnego typu i podniesie ją do tej samej potęgi"))
x = pow(liczba, liczba)
print(x)