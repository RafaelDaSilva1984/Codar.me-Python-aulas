def maior_idade(pessoa):           
    if type(pessoa) == tuple:
        nome, idade = pessoa

        if idade >= 18:
            print('Maior Idade em Tupla')
        else:
            print('Menor Idade em Tupla ')

    elif type(pessoa) == dict:
        idade =  pessoa ['idade']

        if idade >= 18:
            print('Maior Idade em Dicionário')
        else:
            print('Menor Idade em Dicionário')
    
nome = str(input('Qual seu nome: '))   
idade = int(input('Qual sua Idade: '))    

pessoa_tuple = (nome, idade)
idade_tuple = maior_idade (pessoa_tuple)
print(pessoa_tuple)

pessoa_dict = {
'nome': nome,
'idade' : idade,
}
idade_dict = maior_idade(pessoa_dict)
print(pessoa_dict)