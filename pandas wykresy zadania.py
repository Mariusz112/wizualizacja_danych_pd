import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# zad1
wiek = pd.ExcelFile('imiona.xlsx')
wykres = pd.read_excel(wiek, header=0)
dzieci = wykres.groupby(['Rok']).agg({'Liczba': ['sum']})
print(dzieci)
dzieci.plot()
plt.xticks(np.arange(2000, 2018, step=1))
plt.xticks(rotation=100)
plt.show()

# zad2
sdzieci = wykres.groupby(['Plec']).agg({'Liczba': ['sum']})
sdzieci.plot.bar()
print(sdzieci)

# zad4
zamowienia = pd.read_csv("zamowienia.csv",  sep=';')
zamowieniap = zamowienia.groupby('Sprzedawca').agg({'Utarg': ['sum']})
zamowieniap.plot.bar()
plt.show()

