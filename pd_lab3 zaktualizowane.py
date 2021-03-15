import random
# zad1
a = [1 - x for x in range(11) if x >= 1]
b = [4 ** i for i in range(7)]
c = [x for x in b if x % 2 == 0]
print(a)
print(b)
print(c)
# zad2
lista1 = random.sample(range(10, 30), 10)
print(lista1)
d = [x for x in lista1 if x % 2 == 0]
print(d)
# zad3
'''
thisdict = {
    "jaja": "szt",
    "cukier": "kg",
    "mąka": "kg",
    "arbuz": "szt"
}
print(thisdict)
d = [thisdict]
print(d)
print("test")
'''
'''
x = 'szt'
if x in thisdict.values():
    print(x)
    '''
'''


def key_for_value(thisdict, szt):
    """Return a key in `d` having a value of `value`."""
    for k, v in thisdict.iteritems():
        if v == szt:
            return k


'''
# zad4
print("podaj boki trojkata")
aq = int(input())
bq = int(input())
cq = int(input())


def pro(aq, bq, cq):
    if (aq * aq) + (bq * bq) == (cq * cq):
        print("trojkat jest prostokatny")
    elif (aq * aq) + (bq * bq) != (cq * cq):
        print("trojkat nie jest prostokatny")


print(pro(aq, bq, cq))

# zad5
print("podaj boki trapezu i wysokosc")
a = int(input())
b = int(input())
h = int(input())


def tra(a, b, h):
    print((((a + b) * h) / 2))


print(tra(a, b, h))

# zad6
print("Podaj wartosc poczatkowa ciagu")
aw = int(input())
print("podaj wielkosc o ile mnozone sa kolejne elementy")
bw = int(input())
print("ile elementow ma mnozyc")
ileelementow = int(input())


def ciag(aw, bw, ileelementow):
    for i in range(0, ileelementow):
        curr_term = aw * pow(bw, i)
        print(curr_term, end=" ")


ciag(aw, bw, ileelementow)
ciag(1, 4, 10)

# zad7
a = 1
r = 4
dlugosc = 10


def ciag(a, r, dlugosc):
    if a != 0:
        geometric = [a * r ** (n - 1) for n in range(1, dlugosc + 1)]
        return geometric


print(ciag(a, r, dlugosc))
# [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144]

#zad 8 nie wiem

#zad9


print("Podaj wartosc poczatkowa ciagu")
aw = int(input())
print("podaj wielkosc o ile mnozone/zwiekszane sa kolejne elementy")
bw = int(input())
print("na ilu elementach ma operowac")
ileelementow = int(input())


def ciagg(aw, bw, ileelementow):
    for i in range(0, ileelementow):
        curr_term = aw * pow(bw, i)
        print(curr_term, end=" ")


def ciaga(aw, bw, ileelementow):
    for i in range(0, ileelementow):
        curr_term = aw + bw*i
        print(curr_term, end=" ")


ciagg(aw, bw, ileelementow)
ciaga(aw, bw, ileelementow)