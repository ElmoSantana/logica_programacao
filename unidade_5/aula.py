"""Programa que lê uma matriz 3x3 digitada pelo usuário e conta quantos números pares existem na matriz,
imprimindo na tela o resultado e a matiz."""

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        msg = f"Número da célula [{i}] [{j}]?"
        linha.append(int(input(msg)))
    matriz.append(linha)

pares = 0
for linha in matriz:
    for e in linha:
        if e % 2 == 0:
            pares += 1

for linha in matriz:
    print(linha)

print(f"A matriz contém {pares} numeros pares.")
