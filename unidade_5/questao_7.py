"""Peça ao usuário para inserir uma frase. Usando um laço for conte e exiba quantas vogais
existem na frase. Lembre de verificar a documentação do módulo String em busca de métodos que facilitem a
verificação da letra ser vogal."""

texto = input("Digite uma frase: ")
vogais = 'aãáàeéiíoõóuú'
for letra in texto:
    if letra in vogais:
        print(f"Existem {texto.count(letra)} vogais nesta frase que são: {letra}")
