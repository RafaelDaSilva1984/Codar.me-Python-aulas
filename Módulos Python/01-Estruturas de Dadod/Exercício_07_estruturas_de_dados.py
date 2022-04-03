'''
frase = str(input('Digite algo: '))
qtd = len(frase)
qtd_caracteres = {}
for caracteres in frase:
    try:
        quantidade = qtd_caracteres[caracteres]+1
    except:
        quantidade = 1
    qtd_caracteres[caracteres] = quantidade

print(qtd_caracteres)
print('A quantidade de caracteres é: ',qtd)
'''

lista = input('Digite uma palavra: ').lower()

lista_caracteres: dict[str, int] = {}

for caracteres in lista:
    if caracteres in lista_caracteres:
       lista_caracteres[caracteres] += 1
    else:
        lista_caracteres[caracteres] = 1

print(lista_caracteres)





