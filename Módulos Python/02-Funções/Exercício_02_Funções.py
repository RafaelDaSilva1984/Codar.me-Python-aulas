
from turtle import pos


def lista_valores(a):
    lista = (1, 23, 4, 74, 5)   
    max_value = max(lista)
    pos = lista.index(max_value)
    return max_value, pos
maior_pos = lista_valores(0)
print('(Maior Valor e Posição)',maior_pos,type(maior_pos))















