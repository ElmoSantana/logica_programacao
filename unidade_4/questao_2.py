# No mundo de The Witcher, criaturas diferentes apresentam características únicas. Baseado nas pistas abaixo,
# escreva um programa que identifique o tipo de criatura que Geralt está enfrentando:
# - Se o monstro aparece à noite, tem garras e evita prata, é um Lobisomem.
# - Se aparece durante o dia ou à noite, é rápido e ataca em grupo, é um Nekker.
# - Se aparece em qualquer horário, não tem olhos, mas imita vozes humanas, é um Mímico.
# - Se nenhuma dessas combinações for satisfeita, o programa deve imprimir:
# Criatura desconhecida. Prepare-se para o pior.
# O usuário irá informar:
# - horario → dia ou noite
# - caracteristica1 → ex: garras, rápido, não tem olhos, etc.
# - caracteristica2 → ex: evita prata, ataca em grupo, imita vozes humanas, etc."""

horario = input("Informe o horário em que o monstro aparece. Dia ou noite: ").lower()
caracteristica1 = input("Informe a característica que o monstro possue. Garras, rápido ou não tem olhos: ").lower()
caracteristica2 = input("Informe outra característica que o monstro possue. Evita prata, ataca em grupo ou imita vozes humanas: ").lower()

if horario == "noite":
    if caracteristica1 == "garras":
        if caracteristica2 == "evita prata":
            print("Lobisomen")
if horario == "dia" or "noite":
    if caracteristica1 == "rápido":
        if caracteristica2 == "ataca em grupo":
            print("Nekker")
if horario == "dia" or "noite":
    if caracteristica1 == "não tem olhos":
        if caracteristica2 == "imita vozes humanas":
            print("Mímico")

print("Criatura desconhecida. Espere pelo pior!")
