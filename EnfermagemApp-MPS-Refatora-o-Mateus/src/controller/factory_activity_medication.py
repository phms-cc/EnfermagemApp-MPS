# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:08:25 2023

@author: filip
"""

from activity_medication import AtividadeMedicacao
from factory_activity import Atividade_Factory
from activity import Atividade

class AtividadeMedicacao_Factory(Atividade_Factory):
    def __init__(self):
        pass
    
    def getAtividade(self)->Atividade:
        atividade = AtividadeMedicacao()
        atividade.set_tipo(4)
        return atividade
