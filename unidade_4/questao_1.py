"""Escreva um programa que leia o nome de um dia da semana e verifique se é um dia útil ou um dia de fim de
semana. Caso seja um dia útil, imprima "Dia útil". Caso seja um dia de fim de semana, imprima "Fim de semana"."""

dia = input("Digite um dia da semana: ").lower()

match dia:
    case "segunda-feira":
        print("Dia útil")
    case "terça-feira":
        print("Dia útil")
    case "quarta-feira":
        print("Dia útil")
    case "quinta-feira":
        print("Dia útil")
    case "sexta-feira":
        print("Dia útil")
    case _:
        print("Fim de semana")
    