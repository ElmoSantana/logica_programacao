"""Peça ao usuário para inserir uma frase. Usando um laço for conte e exiba quantas vogais
existem na frase. Lembre de verificar a documentação do módulo String em busca de métodos que facilitem a
verificação da letra ser vogal."""

texto = input("Digite uma frase: ")
vogais = 'aãáàeéiíoõóuú'
contador = 0
for letra in texto:
    if letra in vogais:
        contador += 1
        print("Existe {} vogais nesta frase que são: {}".format(contador, letra))
