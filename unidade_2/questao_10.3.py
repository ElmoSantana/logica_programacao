# Crie dois conjuntos: alunos_python e alunos_java. Coloque 3 nomes em cada e:
# Mostre todos os alunos (sem repetição).

alunos_python = {'Elmo', 'Fernanda', 'Samuel'}
alunos_java = {'Raquel', 'Elisângela', 'Rômulo'}

uniao = alunos_python | alunos_java

print(f"A lista com todos os alunos é: {uniao}")
