import random
# zad1
lista1 = random.sample(range(1, 100), 10)
d = [x for x in lista1 if x % 4 == 0]
print(lista1)
print(d)
plik = open("lab4_zad1.txt", "w")
plik.writelines(str(d))
plik.close()
# zad2
plik = open("lab4_zad1.txt", "r")
print(plik.read())
# zad3
with open('lab4_zad2.txt', 'w') as plik:
    plik.write('hello world !')
with open("lab4_zad2.txt", "r") as plik:
    for linia in plik:
        print(linia, end=" ")
# zad4


class NaZakupy:
    nazwa_produktu = " "
    ilosc = 0
    jednostka_miary = " "
    cena_jed = 0

    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        print(self.ilosc, self.nazwa_produktu, self.jednostka_miary, self.cena_jed)

    def ile_produktu(self):
        print(str(self.ilosc) + " " + self.jednostka_miary)

    def ile_kosztuje(self):
        wartosc = self.cena_jed * self.ilosc
        return wartosc


zad4_produkt = NaZakupy("Cukier", 1, "Kg", 5)
zad4_produkt.wyswietl_produkt()
zad4_produkt.ile_produktu()
print(zad4_produkt.ile_kosztuje())
# zad 5


class ciagiarytmetyczne:
    an = 0
    roznica = 0
    ilewyrazow = 0
    wyrazyciagu = [an]

    def wyswietl_dane(self):
        print(self.wyrazyciagu)

    def pobierz_elementy(self, *n):
        pobrane_elementy = []
        for x in n:
            pobrane_elementy.append(self.wyrazyciagu[x-1])
        print(pobrane_elementy)

    def pobierz_parametry(self, an, roznica, ilewyrazow):
        self.an = an
        self.roznica = roznica
        self.ilewyrazow = ilewyrazow

    def policz_sume(self):
        suma = 0
        for x in self.wyrazyciagu:
            suma += x
        print(suma)

    def policz_elementy(self):
        if self.roznica != 0:
            a1 = self.an
            for x in range(self.ilewyrazow):
                an = a1 + self.roznica
                self.wyrazyciagu.append(an)
                a1 = an


zad5 = ciagiarytmetyczne()
zad5.wyswietl_dane()
zad5.pobierz_elementy()
zad5.pobierz_parametry(3, 6, 9)
zad5.policz_sume()
zad5.policz_elementy()
