# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:04:23 2023

@author: filip
"""
from activity_hydration import AtividadeHidratacao
from factory_activity import Atividade_Factory
from activity import Atividade

class AtividadeHidratacao_Factory(Atividade_Factory):
    def __init__(self):
        pass
    
    def getAtividade(self)->Atividade:
        atividade = AtividadeHidratacao()
        atividade.set_tipo(2)
        return atividade
