from EnumTipoAtividade import TipoAtividade

class Atividade:
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
          
        if(tipo in TipoAtividade.__members__):
            self.tipo = tipo
        elif((isinstance (tipo,int))and (tipo <=(len(TipoAtividade)))):
            self.tipo = TipoAtividade(tipo).name
            
    def get_tipo(self):
        return self.tipo
