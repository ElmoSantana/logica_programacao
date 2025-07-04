"""Escreva um programa que receba duas frases SEPARADAMENTE e imprima de maneira invertida, em adição, troque
as letras A por *."""

frase1 = input("Escreva uma frase: ")
frase2 = input("Escreva outra frase: ")
frase3 = frase1 + frase2

frase4 = frase3.replace("a", "*")

print(frase4[::-1])
