"""Escreva um programa que leia uma sequência de números inteiros informados pelo usuário e imprima os números
primos dessa sequência."""

cont = 0

for i in range(1, 1000):
    num = int(input('Digite um sequência de números >>> '))
    if num == 0:
        break
    if num % i == 0:
        cont += 1

if cont == 2:
    print(f'{cont} São números primos!')
else:
    print('Não é primo.')
    print(f'Ele é divisível por {cont} números.')
