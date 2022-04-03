from usuario import Usuario

class Adiministrador(Usuario):
    def imprime_usuario(self):
        print(f'{self.nome} ({self.email}) - Administrador')
        
