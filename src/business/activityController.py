from models.activity import Atividade


class AtividadeController:

    
    def cria_atividade(self):
        atividade = Atividade()
        return atividade
    
    def get_atividade(self):
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
        
