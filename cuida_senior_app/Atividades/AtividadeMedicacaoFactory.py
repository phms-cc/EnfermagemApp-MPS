# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:08:25 2023

@author: filip
"""

from AtividadeMedicacao import AtividadeMedicacao
from AtividadeFactory import Atividade_Factory
from Atividade import Atividade

class AtividadeHidratacao_Factory(Atividade_Factory):
    def __init__(self):
        pass
    
    def getAtividade(self)->Atividade:
        atividade = AtividadeMedicacao()
        return atividade