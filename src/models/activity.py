from EnumTipoAtividade import TipoAtividade
from inter.iprototype import IPrototype
import copy

class Atividade(IPrototype):
    def __init__(self):
        self.anotacao = None
        self.data = None
        self.imagens = []
        self.alarme = None
        self.tipo = None
    
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
        self.tipo = tipo
            
    def get_tipo(self):
        return self.tipo

    def clone(self):
        clone = copy.deepcopy(self) 
        return clone
