#Exercício 01 - PAR
num= int(input('Digite um valor: '))
resultado = num % 2
print("O valor {} é PAR:".format(num),resultado == 0)
print("O valor {} é IMPAR:".format(num), resultado != 0)
    
#Exercício 02 - True e False
a = 5
b = 10
x = True
y = False

print((x or y) and (a < b))
print((x or y) and not ( a < b)) #not inverte a expressão

#Exercício 03 - Parenteses 
resultado = 2 + 3 * 2 ** 2
print(resultado)
resultado = 2 + (3 * 2) ** 2
print(resultado)
resultado = ((2 + 3 )* 2 ) ** 2
print(resultado)

#Exercicio 04 - Desconto

valor = float(input("Valor da Compra R$: "))
frete = float(input("Valor do Frete R$: "))
cliente = str(input('Você é Cadastro como CLIENTE: Sim [S] ou Não [N]: ')).upper()
totalvalorfrete = (valor + frete)
if totalvalorfrete >= 100 or cliente == "S":
    print("Você PODE utilizar o cupom desconto.\n",totalvalorfrete >= 100 or cliente == "S")
else:
    print('Você NÃO PODE utilizar o cupom desconto.\n',totalvalorfrete >= 100 or cliente == "S")

