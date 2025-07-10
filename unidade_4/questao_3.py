"""Escreva um programa que receba o salário de uma pessoa e diga quanto ela pagará apenas de Imposto de Renda.
Considere as seguintes faixas de incidência do imposto:
até R$ 2.259,20 – isento;
- de R$ 2.259,21 a R$ 2.826,65 – 7,5%;
- de R$ 2.826,66 a R$ 3.751,05 – 15%
- de R$ 3.751,06 a 4.664,68 – 22,5%; e
- acima de R$ 4.664,68 – 27,5%."""

salario = float(input("Informe o seu salário R$: "))

if salario <= 2.25920:
    print("Isento")
elif salario == 2.25921 or salario <= 2.82665:
    print(f"Você pagará R${salario*(7.5/100)}")
elif salario == 2.82666 or salario <= 3.75105:
    print(f"Você pagará R${salario*(15/100)}")
elif salario == 3.75105 or salario <= 4.66468:
    print(f"Você pagará R${salario*(22.5/100)}")
elif salario >= 4.66468:
    print(f"Você pagará R${salario*(27.5/100)}")
else:
    print("Impossível calcular.")
