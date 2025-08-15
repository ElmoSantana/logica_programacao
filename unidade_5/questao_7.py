"""Peça ao usuário para inserir uma frase. Usando um laço for conte e exiba quantas vogais
existem na frase. Lembre de verificar a documentação do módulo String em busca de métodos que facilitem a
verificação da letra ser vogal."""

def verificacaoVogal(i):
    vogais = 'aáàãeéiíoóõuú'
    if (i in vogais):
        return True
    else:
        return False

frase = str(input("Digite uma frase: "))
frase = frase.lower()
soma = 0
for i in frase:
    if (verificacaoVogal(i)==True):
        soma+=1

for vogais in frase:
    if vogais.lower() in 'aãáàeéiíoõóuú':
        print(f"As vogais desta frase são {vogais} em uma quatidade de {soma} vogais.", end=' ')
