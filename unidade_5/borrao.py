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
print(soma)
