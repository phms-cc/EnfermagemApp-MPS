# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:06:32 2023

@author: filip
"""

from activity_feeding import AtividadeAlimentacao
from factory_activity import Atividade_Factory
from activity import Atividade

class AtividadeAlimentacao_Factory(Atividade_Factory):
    def __init__(self):
        pass
    
    def getAtividade(self)->Atividade:
        atividade = AtividadeAlimentacao()
        atividade.set_tipo(1)
        return atividade
