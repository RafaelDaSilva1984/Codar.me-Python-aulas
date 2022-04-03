from usuario import Usuario
from administrador import Adiministrador

u = Usuario('Gabriel', 'Grabriel@exemplo.com')
a = Adiministrador('Admin', 'admin@exemplo.com')
u.imprime_usuario()
a.imprime_usuario()
print(Usuario.quantidade)

