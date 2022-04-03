def maior_idade(n):
    nome = str(input('Qual seu nome: '))
    idade= int(input('Qual seu nome: '))
    if idade >= 18:
        print(nome,'é Maior de Idade','sua idade é',idade,'anos')
    else:
        print(nome,'é Menor de Idade','sua idade é',idade,'anos')
    return nome, idade
maior = maior_idade(18)
print(maior,type(maior))


