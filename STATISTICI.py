#Scrieti un script care va primi ca parametru un path catre un fisier cu extensia .csv in care vor
#fi salvate pe coloane urmatoarele date : varsta, sex, IQ, nationalitate si care va calcula pentru
#o coloana la alegere media, mediana, deviatia standard, min, max, cvartile, covarianta si
#coeficientul de corelatie dintre varsta si IQ si va afisa relatia dintre cele doua variabile folosind
#un “plot”.

import os
import statistics
from statistics import covariance
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def medie(matrix,column):
    suma = ct = 0
    for i in range(0, len(matrix[column])):
        suma = suma + int(matrix[i][column])
        ct = ct + 1
    if ct == 0:
        print(0)
    else:
        print(suma//ct)

def mediana(matrix,column):
    ans = matrix[column].sort()
    print(statistics.median(ans))

def standard_deviation(matrix, column):
    ans = matrix[column].sort()
    print(np.std(ans))

def min_max(matrix,column):
    ans = matrix[column].sort()
    print(ans[0], ans[len(ans) - 1])

def quantile_(matrix, column):
    ans = matrix[column].sort()
    ans.quantile([0.25,0.5,0.75])

def corelatie(matrix):
    ansIQ = matrix[0].sort()
    ansAge = matrix[1].sort()
    print(covariance(ansIQ,ansAge))

def corrcoef_(matrix):
    ansIQ = matrix[0].sort()
    ansAge = matrix[1].sort()
    print(np.corrcoef(ansIQ, ansAge))

def SaveEachColumn():
    #column_input = input("Coloana : ")
    #if column_input == "Age":
     #   column = 0
    #elif column_input == "IQ":
     #   column = 1
    #elif column_input == "Sex":
     #   column = 2
    #elif column_input == "Nationality":
     #   column = 3

    plt.rcParams["figure.figsize"] = [10.50, 5.50]
    plt.rcParams["figure.autolayout"] = True
    headers = ['varsta', 'IQ']
    df = pd.read_csv('info.csv', usecols=headers)
    print(df)
    plt.plot(df.varsta, df.IQ)
    #plt.show()
    x = pd.Series(df.varsta)
    y = pd.Series(df.IQ)
    correlation = x.corr(y)
    print(correlation)
    plt.scatter(x, y)
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))
    (np.unique(x)), color='red')


SaveEachColumn()

