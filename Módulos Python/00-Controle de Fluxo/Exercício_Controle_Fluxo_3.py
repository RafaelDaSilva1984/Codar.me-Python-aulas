#Exercício 03 ( Senha)

usuario1 = str(input("Usuário: "))
senha1 = str(input("Senha: "))
usuario = "admin"
senha= "123123"
if usuario1 == usuario and senha1 == senha:
    print("Autenticação BEM Sucedida")
elif usuario1 != usuario and senha1 == senha:
    print("Nome de usuário não existe")
elif usuario1 == usuario and senha1 != senha:
    print("Senha Incorreta")
else:
    print('Dados Inválidos...')

