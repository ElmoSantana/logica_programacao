"""Crie um programa que receba uma senha e verifique sua validade com base nas seguintes condições:
Deve ter pelo menos 8 caracteres.
Deve conter pelo menos uma letra maiúscula.
Deve conter pelo menos um número.
Não pode conter espaços em branco."""

while True:
    
    senha = str(input("Digite os caracteres para criar sua senha: "))

    if len(senha) <7:
        print("A senha deve conter pelo menos 8 (oito) caracteres: ")
        if senha.islower():
            print("A senha deve conter pelo menos um dos caracteres MAIÚSCULO: ")
            if senha.isalnum():
                print("A senha deve conter pelo menos um número: ")
                if senha.isalpha ():
                    print("A senha deve conter pelo menos um caractere especial: ")

print("Senha cadastrada com sucesso!")
    
