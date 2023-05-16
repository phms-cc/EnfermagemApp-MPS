from models.activity import Atividade
from factory_activity import Atividade_Factory
from factory_activity_feeding import AtividadeAlimentacao_Factory
from factory_activity_hydration import AtividadeHidratacao_Factory
from factory_activity_hygiene import AtividadeHigiene_Factory
from factory_activity_medication import AtividadeMedicacao_Factory


class AtividadeController:

    
    def cria_atividade(self):
        factory = Atividade_Factory()
        return factory.getAtividade()
    
    def cria_atividade_alimentacao(self):
        factory = AtividadeAlimentacao_Factory()
        return factory.getAtividade()
    
    def cria_atividade_hidratacao(self):
        factory = AtividadeHidratacao_Factory()
        return factory.getAtividade()

    def cria_atividade_higiene(self):
        factory = AtividadeHigiene_Factory()
        return factory.getAtividade()

    def cria_atividade_medicacao(self):
        factory = AtividadeMedicacao_Factory()
        return factory.getAtividade()
      
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
        
