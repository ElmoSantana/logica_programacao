"""Escreva um programa que leia uma sequência de números inteiros informados pelo usuário e imprima os números
ímpares dessa sequência."""

numeros = [[], []]
sequencia = 0

for i in range(1, 1000):
    sequencia = int(input("Digite uma sequência de números inteiros (0 para encerrar): "))
    if sequencia == 0:
        break
    if sequencia % 2 == 0:
        numeros[0].append(sequencia)
    else:
        numeros[1].append(sequencia)

print(f"Os números ímpares informados foram: {numeros[1]}")
