import numpy as np

#Zad 1
a = 4*np.arange(20)
print(a)
# Zad 2
a = np.arange(10, dtype='float')
print(a)
b = a.astype('int32')
print(b)
#Zad 3
def powerOf2Array(n : int):
    a = 2**np.mgrid[1:n+1, 1:n+1]
    return a

    print(powerOf2Array(20))

