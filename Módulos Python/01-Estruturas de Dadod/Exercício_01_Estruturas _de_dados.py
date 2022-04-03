print('Insira valor positivo para formar a lista, e valor negativo para finalizar')
num = 0
lista = []
while num >= 0:
    num = int(input('Insira valor : ')) 
    if num >= 0:
         lista.append(num)
    else:
        print('Valor Negativo Vc finalizou a lista...')
print('Sua lista é:\n',lista)   

   