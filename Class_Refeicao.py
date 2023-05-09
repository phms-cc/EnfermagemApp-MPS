# -*- coding: utf-8 -*-
"""
Created on Tue May  9 10:07:58 2023

@author: filip
"""

from EnumAceitacaoRefeicao import AceitacaoRefeicao
from EnumTipoRefeicao import TipoRefeicao

class Refeicao:
    def __init__(self):
        self.descricao = None
        self.tipo = -1
        self.aceitacao = -1
    
    def set_descricao (self,descricao):
        self.descricao = descricao
        
    def get_descricao (self):
        return self.descricao
    
    def set_tipo_refeicao(self,tipo):
        if(isinstance (tipo,int)):
            self.tipo = tipo
        elif(tipo in TipoRefeicao.__members__):
            self.tipo = tipo
            
    def get_tipo_refeicao(self):
        return self.tipo
    
    def get_aceitacao(self):
        return self.aceitacao
    
    def set_aceitacao(self,aceitacao):
        if(isinstance (aceitacao,int)):
            self.aceitacao = aceitacao
        elif(aceitacao in AceitacaoRefeicao.__members__):
            self.aceitacao = aceitacao
        