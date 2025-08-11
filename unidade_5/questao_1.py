"""Escreva um programa que imprima a tabuada (Multiplicação) de um número inteiro informado pelo usuário.
Imprima a tabuada de maneira organizada."""

numero = int(input("Informe um número: "))
multiplic = 1

for i in range (1, 11):
    print("{} x {} = {}".format(numero, multiplic, numero*multiplic))
    multiplic = multiplic +1
