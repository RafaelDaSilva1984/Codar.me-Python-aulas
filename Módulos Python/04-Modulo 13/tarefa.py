from ast import Return
from datetime import timedelta


class Tarefa:    
    def __init__(self, titulo, descricao="", data=None, data_notificacao=None):
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.data_notificacao = data_notificacao
        self.concluido = False
    
    def concluir(self):                                                            
            self.concluida = True
        
    def adicionar_descricao(self, descricao):
           self.adicionada = descricao 
           
    def adiar_notificacao(self, minutos):
        if self.data_notificacao is None:
            return
        self.data_notificacao + timedelta(minutes=minutos) 
            
        
