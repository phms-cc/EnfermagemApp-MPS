# -*- coding: utf-8 -*-
"""
Created on Sun May  7 19:30:25 2023

@author: filip
"""

from Atividade import Atividade
from Control_Refeicao import RefeicaoControle

class AtividadeAlimentacao(Atividade):
    def __init__(self):
        super().__init__()
        self.refeicoes = RefeicaoControle()
    

    
    