
def argumento(lista, elemento):
    for valor in lista:
        if valor == elemento:
            return True
    return False
elemento = int(input('Digite número: '))
print(argumento([1, 2, 3],elemento))


