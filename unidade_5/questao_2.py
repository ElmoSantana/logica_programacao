"""Escreva um programa que calcule o fatorial de um número inteiro informado pelo usuário."""

numero = int(input("Informe um número para saber o seu fatorial: "))
fatorial = 1

while numero > 0:
    fatorial = fatorial*numero
    numero = numero -1
print(f"O fatorial desse número é: {fatorial}")