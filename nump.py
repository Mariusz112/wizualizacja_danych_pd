import numpy as np
'''
# zad1
a = np.arange(15)
print((a+1)*3)
# zad2
a = np.array([1.2, 4.3])
print(a)
b = a.astype('int64')
print(b)
print(b.dtype)
# zad3

n = int(input("Wprowadź liczbę całkowitą n"))
c = np.arange(n*n)
print(c+1)

# zad4
d = int(input("poda 1 liczbe calkowita"))
e = int(input("poda 2 liczbe calkowita"))
f = np.arange(e)
print(d**(f+1))
'''
# zad 5
n = int(input("Wprowadź liczbę całkowitą n"))
print("")
wektor = np.diag([a for a in range(n)], 0)
res = wektor[::-1]
print(res)