"""Jogo de Adivinhação Crie um jogo onde o programa escolhe um número aleatório entre 1 e 100. O jogador deve
tentar adivinhar o número. Obs. Pesquisa como importar e usar o módulo random para gerar o número aleatório em
questão.
A cada tentativa, o programa deve dizer se o número é maior ou menor que a tentativa.
O jogo termina quando o jogador adivinhar o número correto."""

import random
from random import randint

computador = randint (1, 100)
print("Tente adivinhar em qual número pensei.")
jogador = int(input("Escolha um número entre 1 e 100: "))

if jogador >computador:
    print("Seu número é maior que o meu. Tente novamente.")    
    
elif jogador <computador:
    print("Seu número é menor que o meu. Tente novamente.")

else:
    print("Parabéns! Você conseguiu adivinhar o número.")
