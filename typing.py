# -*- coding: utf-8 -*-
"""typing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14IM4LTuC_BH-DZwHDsvFusGqNCertmxl
"""

import random


def przywitaj(name, surname):
    powitanie = f"Cześć {name} {surname}!"
    return powitanie


imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
wynik = przywitaj(imie, nazwisko)
print(wynik)


def pomnoz(a, b):
    return a * b


liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
wynik = pomnoz(liczba1, liczba2)

print(f"Wynik mnożenia to: {wynik}")


def czy_parzysta(liczba):
    return liczba % 2 == 0


liczba_do_sprawdzenia = int(input("Podaj liczbę: "))
jest_parzysta = czy_parzysta(liczba_do_sprawdzenia)
if jest_parzysta:
    print("Liczba parzysta")

else:

    print("Liczba nieparzysta")


def czy_suma_wieksza_lub_rowna(a, b, c):
    return (a + b) >= c


liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
liczba3 = int(input("Podaj trzecią liczbę: "))
wynik = czy_suma_wieksza_lub_rowna(liczba1, liczba2, liczba3)
print(wynik)


def czy_zawiera_wartosc(lista, wartosc):
    return wartosc in lista


lista_wejsciowa = [random.randint(0, 100) for _ in range(10)]
print(f"Wygenerowana lista: {lista_wejsciowa}")


wartosc_do_sprawdzenia = int(input("Podaj wartość do sprawdzenia: "))
wynik = czy_zawiera_wartosc(lista_wejsciowa, wartosc_do_sprawdzenia)
print(f"Czy lista zawiera wartość {wartosc_do_sprawdzenia}? {wynik}")


def polacz_i_poteguj(lista1, lista2):
    polaczone_bez_duplikatow = list(set(lista1 + lista2))
    wynik = [element ** 3 for element in polaczone_bez_duplikatow]
    return wynik


lista_a = [1, 2, 3, 4, 5]
lista_b = [3, 4, 5, 6, 7]
wynikowa_lista = polacz_i_poteguj(lista_a, lista_b)
print(wynikowa_lista)
