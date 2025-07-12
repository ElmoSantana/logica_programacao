"""Escreva um programa que receba o salário de uma pessoa e diga quanto ela pagará apenas de Imposto de Renda.
Considere as seguintes faixas de incidência do imposto:
até R$ 2.259,20 – isento;
- de R$ 2.259,21 a R$ 2.826,65 – 7,5%;
- de R$ 2.826,66 a R$ 3.751,05 – 15%
- de R$ 3.751,06 a 4.664,68 – 22,5%; e
- acima de R$ 4.664,68 – 27,5%."""

salario = float(input("Informe o seu salário em R$: "))

faixa1 = "isento"
faixa2 = salario*7.5/100
faixa3 = salario*15/100
faixa4 = salario*22.5/100
faixa5 = salario*27/100

if salario <= 2259.20:
    print(f"{faixa1}")
elif salario <= 2826.65:
    print(f"{faixa2:.2f}")
elif salario <= 3751.05:
    print(f"{faixa3:.2f}")
elif salario <= 4664.68:
    print(f"{faixa4:.2f}")
else:
    print(f"{faixa5:.2f}")
