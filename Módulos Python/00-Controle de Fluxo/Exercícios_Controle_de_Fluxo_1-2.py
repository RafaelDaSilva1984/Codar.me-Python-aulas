
#Exercício 01 (Condicionais)
num=int(input("Digite um número: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0:
    print("Fizz")
else:
    print("...")

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

#Exercício 03 ( Senha)
usuario = str(input("Usuário: "))
senha = str(input("Senha: "))
usuario = "admin"
senha = "123123"
if usuario == usuario and senha == senha:
    print("Autenticação BEM Sucedida")
