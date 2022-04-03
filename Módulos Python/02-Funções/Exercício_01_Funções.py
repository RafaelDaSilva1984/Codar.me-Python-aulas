
def e_primo(p):
    num = int(input('Digite um numero inteiro: '))     
    i = 1
    tdiv = 0
    while i <= num:              
        if (num % i) == 0:
            tdiv += 1
        i += 1      
    if tdiv == 2:
       print('O número',num,'É um número Primo')     
    else:
        print('O número',num,'Não é um número Primo')     
    return num
primo = e_primo(0)
print('Da',type(primo))


"""
Para escrever um programa de número primo com while,
vc deve ter uma variavel de inicio com valor = a 1
uma variavel total de divisões = a 0
a lógica baseia -se em enquanto o inicio for menor = a inicio
vc divide sem resto % a variável de entrada de valor pelo variavel inicio = a 1
se a mesma resposta for = a 0 soma  mais 1 no total de divisões
e soma mais 1 na variável início até que a mesma seja menor ou igual a entrada após
pare o looping de valores.
se o total de divisões for igual a duas divisões é número primm, se for maior ou menor não 
é um número primo.
obs: a lógica baseia-se na quantidade de divisões q u valor tem resto zero.
"""

