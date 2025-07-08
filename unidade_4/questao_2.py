"""No mundo de The Witcher, criaturas diferentes apresentam características únicas. Baseado nas pistas abaixo,
escreva um programa que identifique o tipo de criatura que Geralt está enfrentando:
- Se o monstro aparece à noite, tem garras e evita prata, é um Lobisomem.
- Se aparece durante o dia ou à noite, é rápido e ataca em grupo, é um Nekker.
- Se aparece em qualquer horário, não tem olhos, mas imita vozes humanas, é um Mímico.
- Se nenhuma dessas combinações for satisfeita, o programa deve imprimir:
"Criatura desconhecida. Prepare-se para o pior."
O usuário irá informar:
- "horario" → "dia" ou "noite"
- "caracteristica1" → ex: "garras", "rápido", "não tem olhos", etc.
- "caracteristica2" → ex: "evita prata", "ataca em grupo", "imita vozes humanas", etc."""

horario = input("Informe o horário em que o monstro aparece [D] dia [N] noite: ").lower()
caracteristica1 = input("Informe a característica que o monstro possue [G] garras [R] rápido [NTO] não tem olhos: ").lower()
caracteristica2 = input("Informe outra característica que o monstro possue [EP] evita prata [AG] ataca em grupo [IVH] imita vozes humanas: ").lower()

if horario == "N" and caracteristica1 == "G" and caracteristica2 == "EP":
    print("Lobisomen")

elif horario == "D" or "N" and caracteristica1 == "R" and caracteristica2 == "AG":
    print("Nekker")

elif horario == "D" or "N" and caracteristica1 == "NTO" and caracteristica2 == "IVH":
    print("Mímico")

else:
    print("Criatura desconhecida. Prepare-se para o pior!")
