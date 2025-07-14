"""Crie um programa que receba uma senha e verifique sua validade com base nas seguintes condições:
Deve ter pelo menos 8 caracteres.
Deve conter pelo menos uma letra maiúscula.
Deve conter pelo menos um número.
Não pode conter espaços em branco."""

senha = input("Digite sua senha com oito caracteres : ")

quantid_caracteres = len(senha)

letras = set(("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"))
numeros = set((1, 2, 3, 4, 5, 6, 7, 8, 9, 0))
caracteres_especial = set(("!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "\", "^", "{", "}"))

if quantid_caracteres < 8:
    print("Digite uma senha com no mínimo oito caracteres.")
elif senha == "1, 2, 3, 4, 5, 6, 7, 8, 9, 0":
        if senha == "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z":
            if senha == "!, #, $, %, &, ', (, ), *, +, -, ., /, :, ;, <, =, >, ?, @, [, \, ], ^, _, `, {, |, }, ~":
                 if quantid_caracteres >= 8:
                      print("Senha cadastrada com sucesso.")
else:
    print("Senha inválida.")
