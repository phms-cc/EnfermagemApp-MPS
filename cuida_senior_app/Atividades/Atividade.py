# -*- coding: utf-8 -*-
"""
Created on Sun May  7 16:00:45 2023

@author: filip
"""


from EnumTipoAtividade import TipoAtividade
# tipos de atividade:
#alimentação, hidratação, higiene e medicação
class Atividade:
    def __init__(self):
        self.anotacao = None
        self.data = None
        self.imagens = []
        self.alarme = None
    
    def get_anotacao(self):
        return self.anotacao
    def set_anotacao (self,anotacao):
        self.anotacao = anotacao
        
    def get_data(self):
        return self.data
    def set_data(self,data):
        self.data = data
    
    def add_imagem(self,imagem):
        self.imagens.append(imagem)
    def get_imagens(self):
        return self.imagens
    
    def set_alarme(self,alarme):
        self.alarme = alarme
    def get_alarme(self):
        return self.alarme
        
    def set_tipo(self,tipo):
          
        if(tipo in TipoAtividade.__members__):
            self.tipo = tipo
        elif((isinstance (tipo,int))and (tipo <=(len(TipoAtividade)))):
            self.tipo = TipoAtividade(tipo).name
            
    def get_tipo(self):
        return self.tipo        

class AtividadeControl:
    def __init__(self):
        pass
    
    def get_anotacao(self,atividade):
        return atividade.get_anotacao()
    
    def set_anotacao(self,atividade,anotacao):
        atividade.set_anotacao(anotacao)
        
    def get_data(self,atividade):
        atividade.get_data()
        
    def set_data(self,atividade,data):
        atividade.set_data(data)
    
    def add_imagem(self,atividade,imagem):
        atividade.add_imagem(imagem)
        
    def get_imagens(self,atividade):
        atividade.get_imagens()
        
        
