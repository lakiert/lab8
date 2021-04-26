import numpy as np
import pandas as pd
import xlrd
import openpyxl

# zad1

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
#print(df)

# zad2

# print(df[df['Liczba'] < 1000])
# print('')
# print(df[df.Imie == 'ALEKSANDRA'])
# print('')
# print(sum(df['Liczba']))
# print('')
# print(sum(df['Liczba'] & ((df.Rok) > 2004) & ((df.Rok) < 2011) ))
# print('')
# print(sum(df['Liczba'] & ((df.Plec) == 'M') & ((df.Rok) == 2000) ))
# print('')
# dziewczynki = df[(df.Plec == 'K')]
# chlopcy = df[(df.Plec == 'M')]
# print(df.Imie[df.Liczba == max(chlopcy.Liczba)])
# print(df.Imie[df.Liczba == max(dziewczynki.Liczba)])