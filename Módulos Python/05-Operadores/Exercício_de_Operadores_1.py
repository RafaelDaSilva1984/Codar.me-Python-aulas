#Exercício 01 - PAR
num= int(input('Digite um valor: '))
resultado = num % 2
print("O valor {} é PAR:".format(num),resultado == 0)
print("O valor {} é IMPAR:".format(num), resultado != 0)