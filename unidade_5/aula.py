def separar (lista):

lista_numeros = []

while(True):
    usuario_numero = int(input("Informe uma sequência de números (0 para encerrar): "))
    if (usuario_numero == 0):
        return 
    
    lista_numeros.append(usuario_numero)

print(lista_numeros)


