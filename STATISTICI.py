#Scrieti un script care va primi ca parametru un path catre un fisier cu extensia .csv in care vor
#fi salvate pe coloane urmatoarele date : varsta, sex, IQ, nationalitate si care va calcula pentru
#o coloana la alegere media, mediana, deviatia standard, min, max, cvartile, covarianta si
#coeficientul de corelatie dintre varsta si IQ si va afisa relatia dintre cele doua variabile folosind
#un “plot”.

import os
import statistics
from statistics import covariance
from statistics import median
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def medie(column):
    suma = ct = 0
    for i in range(0, len(column)):
        suma = suma + int(column[i])
        ct = ct + 1
    if ct == 0:
        print(0)
    else:
        print(suma//ct)

def mediana(column):
    ans = sorted(column)
    print(median(list(ans)))

def standard_deviation(column):
    ans = sorted(column)
    print(np.std(ans))

def min_max(column):
    ans = sorted(column)
    print(ans[0], ans[len(ans) - 1])

def quantile_(column):
    ans = sorted(column)
    print(np.quantile(ans, q=np.arange(0.25, 0.5, 0.75)))

def corelatie(column1, column2):
    ansAge = sorted(column1)
    ansIQ = sorted(column2)
    print(covariance(ansIQ,ansAge))

def corrcoef_(column1, column2):
    ansAge = sorted(column1)
    ansIQ = sorted(column2)
    print(np.corrcoef(ansIQ, ansAge))

def main():
    column_input = input("Coloana : ")
    if column_input == "age":
        column = 0
    elif column_input == "IQ":
        column = 1
    elif column_input == "sex":
        column = 2
    elif column_input == "nationality":
        column = 3

    if column == 2 or column == 3:
        print("Nu se poate calcula")
        plt.rcParams["figure.figsize"] = [7.50, 4.50]
        plt.rcParams["figure.autolayout"] = True
        header = ['sex','nationalitate']
        df = pd.read_csv('info.csv', usecols=header)
        if column == 2:
            x = pd.Series(df.sex)
            sex = list(x)
            print(sex)
            plt.hist(sex)
            plt.show()
        else:
            x = pd.Series(df.nationalitate)
            nat = list(x)
            print(nat)
            plt.hist(nat)
            plt.show()

    else:
        plt.rcParams["figure.figsize"] = [10.50, 5.50]
        plt.rcParams["figure.autolayout"] = True
        headers = ['varsta', 'IQ']
        df = pd.read_csv('info.csv', usecols=headers)
        print(df)
        x = pd.Series(df.varsta)
        varsta = list(x)
        y = pd.Series(df.IQ)
        iq = list(y)
        if column == 0:
            medie(varsta)
            mediana(varsta)
            standard_deviation(varsta)
            min_max(varsta)
            quantile_(varsta)
        else:
            medie(iq)
            mediana(iq)
            standard_deviation(iq)
            min_max(iq)
            quantile_(iq)
        correlation = x.corr(y)
        print(correlation)
        plt.scatter(x, y)
        plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color='red')
        plt.show()


main()

