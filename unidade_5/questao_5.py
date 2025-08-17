"""Escreva um programa que leia uma sequência de números inteiros informados pelo usuário e imprima a
quantidade de números negativos."""

numeros = [[], []]
sequencia = 0

for i in range(1, 10000):
    sequencia = int(input("Digite uma sequência de números inteiros (0 para encerrar): "))
    if sequencia == 0:
        break
    if sequencia < 0:
        numeros[0].append(sequencia)
    else:
        numeros[1].append(sequencia)

print(f"Os números negativos informados foram: {numeros[0]}")
