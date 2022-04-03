#Exercício 02 (Calculadora)
num1 = float(input("Valor 1: "))
num2 = float(input("Valor 2: "))
num3 = float(input("Valor 3: "))
operador = float(input('''Escolha a opção de operador:
[1] soma
[2] subtração
[3] multiplicação
[4] divisão:\n '''))
if operador == 1:
    soma = (num1 + num2 + num3)
    print('Resultado',soma)
elif operador == 2:
    subtração = (num1 - num2 - num3)
    print('Resultado',subtração)
elif operador == 3:
    multiplicação = (num1 * num2 * num3)
    print('Resultado',multiplicação)
elif operador == 4:
    if num2 == 0:
        print("Não é possível fazer a divisão por Zero...")  
    divisão = (num1 / num2 / num3)
    print('Resultdo',divisão)  