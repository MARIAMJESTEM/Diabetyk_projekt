#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import pandas as pd
import time
from datetime import date
from csv import writer
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from os import system, name
from time import sleep
from shutil import copyfile
import os

document = pd.read_csv('dane.csv')

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

def new_position():
    now = date.today()
    new_measure=int(input('Podaj nową wartość pomiaru cukru'))
    new_row =[now,new_measure]
    append_list_as_row('dane.csv', new_row)

    print('Twoja wartość cukru została dodana!')

    if new_measure < 100:
        print('Prawidłowy poziom cukru')
    elif 100 <= new_measure <= 125:
        print('Podwyższony poziom cukru. Musisz uważać!')
    elif new_measure > 125:
        print('Zbyt wysoki poziom cukru')

    sleep(6)
    system("cls")
    return 0

def plot():
    count_row = document.shape[0]
    x = document.loc[0:count_row,'data']
    y = document.loc[0:count_row,'pomiar']
    plt.bar(x, y)
    plt.title('Wykres zależności pomiaru od daty')
    plt.xlabel('Data pomiaru')
    plt.ylabel('Wartość pomiaru cukru')
    plt.show()
    print(x)

    system("cls")
    return 0

def old_measure():
    choice = int(input('Wybierz: \n 1. Jeśli chcesz wyszukać po dacie\n 2. Jeśli chcesz wyszukać po wartości pomiaru'))
    sleep(1)
    system("cls")
    if choice == 1:
        old_data = str(input('Podaj datę w formacie YYYY-MM-DD z której pomiar  chcesz wyszukać'))
        filt_first = (document['data']== old_data)
        print(document[filt_first])
    elif choice == 2:
        old_measure = int(input('Podaj wartość pomiaru, dla którego datę chcesz otrzymać'))
        filt_secound = (document['pomiar'] == old_measure)
        print(document[filt_secound])
    else:
        print('Podałeś złą wartość')

    sleep(6)
    system("cls")
    return 0

def warning():
    positive_result = 0
    for i in range(1, 4):
        if document.iloc[-i, 1] > 125:
            continue
        else:
            positive_result = 1
            break
    if positive_result == 0:
        print('!!! W ciągu ostatnich trzech dni Twój poziom cukru był zbyt wysoki. Powinieneś skontaktować się z lekarzem !!!')

def zapis():
    sciezka = input('Podaj dokładną ścieżkę do pliku z rozszerzeniem csv do którego chcesz zapisac dotychczasowe dane(ma to być ścieżka do katalogu i nazwa nowego pliku): ')
    if not os.path.isfile(sciezka):
        f = open(sciezka, "w")
    copyfile( 'dane.csv', sciezka)
    print('Utworzyłeś nowy plik z danymi!')
    sleep(6)
    system("cls")
    return 0
    

def  menu(args):
    while True:
        print('Witaj w dzienniku diabetyka!')
        warning()
        wybor=int(input("Wybierz:\n 1 jeśli chcesz dodać nową pozycje poziomu cukru \n 2 jeśli chcesz zobaczyć starszą pozycję \n 3 jesli chcesz zobaczyć wykres zależności poziomu cukru od daty \n 4 jesli chcesz zapisać dane w nowym pliku \n 5 jesli chcesz opuścić program"))
        if wybor == 1:
           print("Teraz dodamy nowa pozycję cukru")
           sleep(1)
           system("cls")
           new_position()
        elif wybor == 2:
            sleep(1)
            system("cls")
            old_measure()
        elif wybor == 3:
            print("Teraz zobaczymy wykres naszych danych od czasu ich dodawania")
            sleep(1)
            system("cls")
            plot()
        elif wybor == 4:
            print("Zapiszemy dotychczasowe dane w nowym pliku")
            sleep(1)
            system("cls")
            zapis()
        elif wybor == 5:
            print("Do zobaczenia wkrótce!")
            sys.exit(0)
        else:
            print('Nie podałeś poprawnej wartości, spróbuj ponownie uruchomic program')

    return 0

def main(args):
    menu(args)

    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
