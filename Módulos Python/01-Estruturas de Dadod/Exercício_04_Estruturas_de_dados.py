
print('Média de Notas com Lista')

alunos = [
    ('Alice',8),
    ('Bob', 7),
    ('Carlo', 9),]
nome0 , nota0 = (alunos[0])
nome1 , nota1 = (alunos[1])
nome2 , nota2 = (alunos[2])
qtd = len(alunos,)
soma = nota0 +nota1 +nota2
media = soma / qtd
print('A média de notas dos {}, {}, {} Alunos é:'.format(nome0, nome1, 'e', nome2),media)


