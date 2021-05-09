import pandas as pd

# Zad1
DataFrame = pd.read_excel('imiona.xlsx', header=0)
print(DataFrame)
# Zad2
print(DataFrame.loc[DataFrame['Liczba'] < 1000])
print(DataFrame.loc[DataFrame['Imie'] == 'Mariusz'])
print(DataFrame['Liczba'].sum())
dzieci = DataFrame.loc[(DataFrame['Rok'] > 2000) & (DataFrame['Rok'] < 2005)]
print(dzieci['Liczba'].sum())
# Zad3
datasets = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal=',')
print(datasets['Sprzedawca'].drop_duplicates())
wzamowienia = datasets['Utarg']
