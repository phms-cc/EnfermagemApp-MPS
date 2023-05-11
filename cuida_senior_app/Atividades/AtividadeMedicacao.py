# -*- coding: utf-8 -*-
"""
Created on Sun May  7 19:25:17 2023

@author: filip
"""

from Atividade import Atividade

class AtividadeMedicacao(Atividade):
    def __init__(self):
        super().__init__()
        self.nome_medicamento = None
        self.quantidade_ingerida = 0
        #quanto foi tomado
        self.quantidade_recomendada =0
        #quanto eh pra ser tomado
        self.quantidade_dose = 0
        #quantas doses a pessoa tomou
        self.horario = 0
        
    def set_nome_medicamento(self,nome):
        self.nome_medicamento = nome
    
    def get_nome_medicamento(self):
        return self.nome_medicamento
    
    def set_quantidade_ingerida(self,qtd):
        self.quantidade_ingerida = qtd
        
    def get_quantidade_ingerida(self):
        return self.quantidade_ingerida
    
    def set_quantidade_recomendada(self,qtd):
        self.quantidade_recomendada = qtd
        
    def get_quantidada_recomendada(self):
        return self.quantidade_recomendada
    
    def get_horario(self):
        return self.horario
    
    def set_horario(self,horario):
        self.horario = horario
        
        
