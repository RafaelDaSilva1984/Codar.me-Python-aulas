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