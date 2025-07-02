"""Escreva um algoritmo que receba do usuário dois números e retorne a soma, a subtração, a multiplicação e a
divisão entre eles."""

num1 = int(input("Escreva um número: "))
num2 = int(input("Escreva outro número: "))

adicao = num1+num2
subtracao = num1-num2
multiplicacao = num1*num2
divisao = num1/num2

print(f"Os resultados são:\n soma {adicao}\n subtração {subtracao}\n multiplicação {multiplicacao}\n divisão {divisao}")
