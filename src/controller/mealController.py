from models.meal import Refeicao
from models.EnumAceitacaoRefeicao import AceitacaoRefeicao
from models.EnumTipoRefeicao import TipoRefeicao
from models.NoEnum import NoEnum

class RefeicaoController:
    def __init__(self):
        pass
        
    def cria_refeicao(*args):
        pass
        if (len(args) == 0):
            refeicao = Refeicao()
        elif (len(args) == 1):
            refeicao = Refeicao()
            self.set_tipo_refeicao(refeicao,args[1])
        return refeicao
        

    def get_tipo_refeicao(self,refeicao):
        return refeicao.get_tipo()
    
    def set_tipo_refeicao(self,refeicao,tipo):
        no_enum = NoEnum()
        if no_enum.no_enum(tipo,TipoRefeicao):
	        refeicao.set_tipo(no_enum.get_valor(tipo,TipoRefeicao)))
        
    def set_aceitacao_refeicao(self,refeicao,aceitacao):
        no_enum = NoEnum()
        if no_enum.no_enum(aceitacao,AceitacaoRefeicao):
	        refeicao.set_tipo(no_enum.get_valor(aceitacao,AceitacaoRefeicao)))
        
    def get_aceitacao_refeicao(self,refeicao):
        return refeicao.get_aceitacao()
        
    def set_descricao_refeicao(self,refeicao,descricao):
        refeicao.set_descricao(descricao)
        
    def get_descricao_refeicao(self,refeicao):
        refeicao.get_descricao()
