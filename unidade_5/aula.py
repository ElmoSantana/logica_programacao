frase = str(input("Digite uma frase: "))
for vogais in frase:
    if vogais.lower() in 'aãáàeéiíoõóuú':
        tamanho = len(vogais)
        print('O número de vogais nessa frase é de: ', tamanho)
