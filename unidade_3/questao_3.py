"""Faça um Programa que pergunte ao usuário quanto você ganha por hora e o número de horas trabalhadas por dia,
considerando que se trabalha 5 dias por semana. Calcule e mostre o total do seu salário ao mês."""

hora_valor = float(input("Quanto você ganha por hora trabalhada? R$"))
hora_trab = int(input("Quantas horas você trabalha por dia? "))

sal = (hora_valor*hora_trab)*26

print(f"Seu salário é de R${sal}")
