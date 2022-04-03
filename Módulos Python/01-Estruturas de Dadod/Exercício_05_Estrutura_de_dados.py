print('Média de Notas com Dicionários')

alunos = [
 {
    'nome' : 'Alice',
    'nota' : 8,
},
{
    'nome' : 'Bob',
    'nota' : 7,
},
{
    'nome' : 'Carlos',
    'nota' : 9,
}
]
soma = ((alunos[0]['nota']) + (alunos[1]['nota']) + (alunos[2]['nota']))
qtd = len(alunos)
media = soma / qtd
print('A média de notas dos alunos:\n',(alunos[0]['nome']),',',(alunos[1]['nome']),'e',(alunos[2]['nome']),'é:''\n',media)



