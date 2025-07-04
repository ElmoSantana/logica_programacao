"""Escreva um programa que peça ao usuário para digitar a temperatura em Fahrenheit e converta para Celsius e
Kelvin, imprimindo o resultado na tela."""

fahren = float(input("Digite a temperatura em Fahrenheit: "))

Celsius = (fahren - 32) * 5 / 9
Kelvin = (fahren - 32) * 5 / 9 + 273.15

print(f"Celsius: {Celsius:.2f}° Kelvin: {Kelvin:.2f}°")
