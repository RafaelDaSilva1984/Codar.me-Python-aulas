
def fatorial(numero):
    if numero == 0:
        return 1
    return numero * fatorial(numero - 1)
numero = int(input('Digite o valor desejado: '))
print(fatorial(numero))
