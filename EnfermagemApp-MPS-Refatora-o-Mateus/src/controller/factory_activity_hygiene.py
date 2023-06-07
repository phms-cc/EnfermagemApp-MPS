# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:07:29 2023

@author: filip
"""

from activity_hygiene import AtividadeHigiene
from factory_activity import Atividade_Factory
from activity import Atividade

class AtividadeHigiene_Factory(Atividade_Factory):
    def __init__(self):
        pass
    
    def getAtividade(self)->Atividade:
        atividade = AtividadeHigiene()
        atividade.set_tipo(3)
        return atividade
