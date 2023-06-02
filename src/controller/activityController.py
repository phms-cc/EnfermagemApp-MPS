from models.activity import Atividade
from factory_activity import Atividade_Factory
from factory_activity_feeding import AtividadeAlimentacao_Factory
from factory_activity_hydration import AtividadeHidratacao_Factory
from factory_activity_hygiene import AtividadeHigiene_Factory
from factory_activity_medication import AtividadeMedicacao_Factory
from EnumTipoAtividade import TipoAtividade

from models.show_image import MostraImagem
from models.EnumTipoAtividade import TipoAtividade
from models.NoEnum import NoEnum

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
    
    def mostra_imagem(self,imagem,argumentos):	
        adaptador = AdaptadorImagem()
        mostrador = MostraImagem()
        adaptador.mostra_imagem(mostrador,imagem,argumentos)
        
    def show_atividades(self,paciente):
        atividades = paciente.get_atividades()
        print ("Atividades do Paciente " + paciente.getNome())
        for atividade in atividades:
            print ("Atividade do tipo " + atividade.get_tipo() + " Data: " + str(atividade.get_data()))
                      
    def set_tipo(self,atividade,tipo):
        no_enum = NoEnum()
        if no_enum.no_enum(tipo,TipoAtividade):
	        atividade.set_tipo(no_enum.get_valor(tipo,TipoAtividade))
        
    def get_tipo(self,atividade):
        return atividade.get_tipo()
    
    def alimentacao_add_refeicao (self,alimentacao,refeicao):
        alimentacao.add_refeicao(refeicao)
    
    def alimentacao_cria_refeicao(self,alimentacao,*args):
        return alimentacao.cria_refeicao(*args)
        
    def alimentacao_get_refeicao(self,alimentacao,x):
        return alimentacao.get_refeicao(x)
        
    def cria_add_refeicao(self,alimentacao,*args):
        alimentacao.cria_add_refeicao(*args)
        
    def alimentacao_ordena_refeicoes(self,alimentacao):
        alimentacao.ordena_refeicoes()
    
    def alimentacao_set_aceitacao_refeicao(self,alimentacao,x,aceitacao):
        alimentacao.set_aceitacao_refeicao(x,aceitacao)
        
    def alimentacao_get_aceitacao_refeicao(self,alimentacao,x):
        return alimentacao.get_aceitacao_refeicao(x)
    
    def alimentacao_set_descricao_refeicao(self,alimentacao,x,descricao):
        alimentacao.set_descricao_refeicao(x,descricao)
        
    def alimentacao_get_descricao_refeicao(self,alimentacao,x):
        return alimentacao.get_descricao_refeicao(x)
        
    def hidratacao_set_quantidade(self,hidratacao,x):
        hidratacao.set_quantidade(x)
        
    def hidratacao_get_quantidade(self,hidratacao):
        return hidratacao.get_quantidade()
    
    def hidratacao_reset_quantidade(self,hidratacao):
        hidratacao.reset_quantidade()
        
    def higiene_set_quantidade_banhos(self,higiene,banhos):
        higiene.set_quantidade_banhos(banhos)
    
    def higiene_get_quantidade_banhos(self,higiene):
        return higiene.get_quantidade_banhos()
    
    def higiene_set_quantidade_frauda(self,higiene,qtd):
        higiene.set_quantidade_frauda(qtd)
        
    def higiene_get_quantidade_frauda(self,higiene):
        return higiene.get_quantidade_frauda()
    
    def higiene_set_quantidade_higiene_intima(self, higiene,quantidade):
        higiene.set_quantidade_higiene_intima(quantidade)
    
    def higiene_get_quantidade_higiene_intima (self,higiene):
        return higiene.quantidade_higiene_intima ()
    
    def higiene_set_areaslavadas_inicio(self,higiene):
        higiene.set_areaslavadas_inicio()
    
    def higiene_add_arealavada(self,higiene, arealavada):
        higiene.add_arealavada(arealavada)
            
    def higiene_remove_arealavada(self, higiene,arealavada):
        higiene.remove_arealavada(arealavada)
            
    def medicamento_set_nome_medicamento(self,medicamento,nome):
        medicamento.set_nome_medicamento(nome)
    
    def medicamento_get_nome_medicamento(self,medicamento):
        return medicamento.get_nome_medicamento()
    
    def medicamento_set_quantidade_ingerida(self,medicamento,qtd):
        medicamento.set_quantidade_ingerida(qtd)
        
    def medicamento_get_quantidade_ingerida(self,medicamento):
        return medicamento.get_quantidade_ingerida()
    
    def medicamento_set_quantidade_recomendada(self,medicamento,qtd):
        medicamento.set_quantidade_recomendada = qtd
        
    def medicamento_get_quantidada_recomendada(self,medicamento):
        return medicamento.get_quantidade_recomendada()
    
    def medicamento_get_horario(self,medicamento):
        return medicamento.get_horario
    
    def medicamento_set_horario(self,medicamento,horario):
        medicamento.set_horario(horario)
    
    
    
    
