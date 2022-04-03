#Exercício_01
'''
num = float(input("Digite um valor\n"))
n = 0
total = 0
while n < num :
    print(n)
    n = n + 1
    total = total + n
print(total)   

#Exercício 02
num = int(input("Digite um valor\n"))
n = 0
while n < num :
    if n % 2 == 0:
        print(n)
    n = n + 1
print(n)
  
#Exercício 03 (Primo)
# qtd de vezes que numero  pode ser divido = 2 vezes
num = int(input("Digite um valor inteiro: "))
i = 1 
div = 0    
while i <= num: # enquanto false continua
    if (num % i ) == 0:
        div += 1
    i += 1
if div == 2:
    print('Primo') 
else:
    print('Não Primo')    
print(i <= num)
print(num % i)
print(div == 2)
print(i)
print(div)
'''
#Exercício 04 "jogo Acerte número"

print('Qual número estou pensando entre 0 a 10!!!!')
comp = 8
max = 3 
tentativas = 1 # determina o inicio do while com numero inteiro apartir do 1
cont=(tentativas) 
while tentativas <= max:
    jogador = int(input('Tente adivinhar: ')) # o input tem que ser depois do while para não ficar se repetindo    
    if jogador == comp:
        print('Parabéns você adivinhou... o número escondido!!!','Jogador',jogador,'e','Computador',comp,'Ambos Igual')
        break # para o programa após acertar o número do computador
    elif jogador > comp:
        print('Número escondido é Menor...Tentativa',cont,'de 3')
        cont = cont + 1
    elif jogador < comp:
        print('Número escondido é Maior...Tentativa',cont,'de 3')
        cont = cont + 1
    if tentativas == max:
        print('Você perdeu meu número escondido é: ',comp)
    tentativas += 1 # somas o número de tentativas até o max indicado

    

    

    
