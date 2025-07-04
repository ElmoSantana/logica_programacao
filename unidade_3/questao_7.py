"""Escreva um programa que informe a quantidade de 1’s que estão em um string. Exemplo: ´ 1011001.
A string será recebida de um usuário."""

sequencia = input("Digite uma sequência de números que contenha o número 1 (um) em qualquer posição: ")

quantidade = sequencia.count("1")

print(f"O número 1 aparece {quantidade} vezes")
