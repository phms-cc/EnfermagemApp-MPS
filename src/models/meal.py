# -*- coding: utf-8 -*-
"""
Created on Tue May  9 10:07:58 2023

@author: filip
"""

class Refeicao:
    def __init__(self):
        self.descricao = None
        self.tipo = None
        self.aceitacao = None
    
    def set_descricao (self,descricao):
        self.descricao = descricao
        
    def get_descricao (self):
        return self.descricao
    
    def set_tipo_refeicao(self,tipo):
        self.tipo = tipo
            
    def get_tipo_refeicao(self):
        return self.tipo
    
    def get_aceitacao(self):
        return self.aceitacao
    
    def set_aceitacao(self,aceitacao):
        self.aceitacao = aceitacao
        
