"""Crie um programa que solicite ao usuário que insira 10 palavras. Armazene essas palavras em uma lista.
Depois:
a) Exiba a lista na ordem inversa.
b) Substitua todas as palavras que começam com a letra "a" por ***.
c) Exiba a lista modificada."""

palavras = []

for i in range(10):
    palavra = str(input("Insira dez palavras: "))
    palavras.append(palavra)
    palavras.reverse()
    print(palavras)
