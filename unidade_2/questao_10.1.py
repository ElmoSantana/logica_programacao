# Crie dois conjuntos: alunos_python e alunos_java. Coloque 3 nomes em cada e:
# Mostre os alunos que fazem as duas linguagens.

alunos_python = {'Elmo', 'Fernanda', 'Samuel'}
alunos_java = {'Raquel', 'Elisângela', 'Rômulo'}

uniao = alunos_python | alunos_java

print(f"Os alunos que fazem as duas linguagens são: {uniao}")
