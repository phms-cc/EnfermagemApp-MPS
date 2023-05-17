from models.meal import Refeicao
from EnumTipoRefeicao import TipoRefeicao

class RefeicaoController:
    def __init__(self):
        pass
        
    def cria_refeicao(*args):
        pass
        if (len(args) == 0):
            refeicao = Refeicao()
        elif (len(args) == 1):
            refeicao = Refeicao()
            refeicao.set_tipo_refeicao(args[1])
        return refeicao
        

    def get_tipo_refeicao(self,refeicao):
        return refeicao.get_tipo()
    
    def set_tipo_refeicao(self,refeicao,tipo):
        refeicao.set_tipo_refeicao(tipo)
        
    def set_aceitacao_refeicao(self,refeicao,aceitacao):
        refeicao.set_aceitacao(aceitacao)
        
    def get_aceitacao_refeicao(self,refeicao):
        refeicao.get_aceitacao()
        
    def set_descricao_refeicao(self,refeicao,descricao):
        refeicao.set_descricao(descricao)
        
    def get_descricao_refeicao(self,refeicao):
        refeicao.get_descricao()
