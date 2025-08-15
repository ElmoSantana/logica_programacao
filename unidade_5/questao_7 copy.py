"""Peça ao usuário para inserir uma frase. Usando um laço for conte e exiba quantas vogais
existem na frase. Lembre de verificar a documentação do módulo String em busca de métodos que facilitem a
verificação da letra ser vogal."""

frase = str(input("Digite uma frase: "))
ocorrencias = frase.count
for letra in frase:
    if letra.lower() in 'aãáàeéiíoõóuú':
        print("A quantidade de vogais nesta frase é de: ", len(letra))
