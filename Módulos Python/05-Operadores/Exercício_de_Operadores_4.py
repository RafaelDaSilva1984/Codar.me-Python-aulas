#Exercicio 04 - Desconto

valor = float(input("Valor da Compra R$: "))
frete = float(input("Valor do Frete R$: "))
cliente = str(input('Você é Cadstro como CLIENTE: Sim [S] ou Não [N]: ')).upper()
totalvalorfrete = (valor + frete)
if totalvalorfrete >= 100 or cliente == "S":
    print("Você PODE utilizar o cupom desconto.\n",totalvalorfrete >= 100 or cliente == "S")
else:
    print('Você NÃO PODE utilizar o cupom desconto.\n',totalvalorfrete >= 100 or cliente == "S")