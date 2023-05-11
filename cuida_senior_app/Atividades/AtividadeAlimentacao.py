# -*- coding: utf-8 -*-
"""
Created on Sun May  7 19:30:25 2023

@author: filip
"""

from Atividade import Atividade

class AtividadeAlimentacao(Atividade):
    def __init__(self):
        super().__init__()
        self.refeicoes = []
    
    def add_refeicao(self,refeicao):
        x = refeicao.get_tipo_refeicao()
        self.refeicoes[x] = refeicao
    
    def get_refeicao (self,x):
        return self.refeicoes[x]
    
    