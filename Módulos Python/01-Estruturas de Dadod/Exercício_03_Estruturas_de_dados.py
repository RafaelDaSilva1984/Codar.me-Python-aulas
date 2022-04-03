notas = [1,10,20,35,22,12]
media_de_notas = 0
qtd = len(notas)
for soma in notas:
    media_de_notas +=  soma
    media = media_de_notas // qtd
print(media)
