# -*- coding: utf-8 -*-
"""
Created on Sun May  7 17:26:52 2023

@author: filip
"""
from Atividade import Atividade

class AtividadeHidratacao(Atividade):
    def __init__(self):
        super().__init__()
        self.quantidade_ingerida = 0
        
    def set_quantidade(self, quantidade):
        self.quantidade = quantidade
    def get_quantidade(self):
        return self.quantidade
    def reset_quantidade(self):
        self.set_quantidade(0)