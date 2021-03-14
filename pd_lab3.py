# zad1
a = [1 - x for x in range(11) if x >= 1]
b = [4 ** i for i in range(7)]
c = [x for x in b if x % 2 == 0]
print(a)
print(b)
print(c)
# zad2
import random

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

a = int(input())
b = int(input())
h = int(input())


def tra(a, b, h):
    print((((a+b)*h)/2))


print(tra(a, b, h))

# zad6