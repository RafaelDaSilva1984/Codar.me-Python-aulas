class Usuario:
    quantidade = 0

    def __init__(self,nome,email): #construtor
        self.nome = nome
        self.email = email
        Usuario.quantidade += 1

    def imprime_usuario(self): #instancia
       print(f'{self.nome} ({self.email})')
      






