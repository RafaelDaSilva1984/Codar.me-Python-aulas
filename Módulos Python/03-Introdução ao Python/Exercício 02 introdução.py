#_Exercício 02 - #_Variáveis 
compras = float(input("Qual valor do compras R$:"))
desconto = float(input("Qual a porcentagem de desconto %:"))
itens = int(input("Quantos itens você comprou: "))
valorcomdesconto = compras - (compras * desconto/100)
médio = (valorcomdesconto) / itens
print("O valor final das suas compras foi de R$ {:.2f}".format(valorcomdesconto))
print("O custo médio de suas compras foram de R$ {:.2f}".format(médio))

