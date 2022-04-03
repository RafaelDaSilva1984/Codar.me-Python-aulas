#Exercícios Base

class Usuario:
    quantidade = 0

    def __init__(self,nome,email): #construtor
        self.nome = nome
        self.email = email
        Usuario.quantidade += 1

    def imprime_usuario(self): #instancia
       print(f'{self.nome} ({self.email})')

class Adiministrador(Usuario):
    def imprime_usuario(self):
        print(f'{self.nome} ({self.email})')

u = Usuario('Gabriel', 'gabriel@exemplo.com')
a = Adiministrador('Admin', 'admin@exemplo.com')
u.imprime_usuario()
print(Usuario)
a.imprime_usuario()
print(Adiministrador)
print('Quantidade de Usuários é ->',Usuario.quantidade)
