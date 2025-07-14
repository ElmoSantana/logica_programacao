"""Escreva um programa que peça ao usuário um número entre 1 e 100. O programa deve verificar:
Se o número é divisível por 3, exiba "Número divisível por 3".
Se o número é divisível por 5, exiba "Número divisível por 5".
Se o número é divisível por 3 e 5, exiba "Número divisível por 3 e por 5.".
Caso contrário, exiba "Número comum"."""

numero = int(input("Digite um número entre 1 e 100: "))

if numero %3 == 0 and numero %5 == 0:
    print("Número divisível por 3 e 5.")
elif numero %3 == 0:
    print("Número divisível por 3.")
elif numero %5 == 0:
    print("Número divisível por 5.")
else:
    print("Número comum.")
