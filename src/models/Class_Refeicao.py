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
        self.tipo = None
        self.aceitacao = None
    
    def set_descricao (self,descricao):
        self.descricao = descricao
        
    def get_descricao (self):
        return self.descricao
    
    def set_tipo_refeicao(self,tipo):
        if(tipo in TipoRefeicao.__members__):
            self.tipo = tipo
        elif((isinstance (tipo,int))and (tipo <=(len(TipoRefeicao)))):
            self.tipo = TipoRefeicao(tipo).name
            
    def get_tipo_refeicao(self):
        return self.tipo
    
    def get_aceitacao(self):
        return self.aceitacao
    
    def set_aceitacao(self,aceitacao):
        if(aceitacao in AceitacaoRefeicao.__members__):
            self.aceitacao = aceitacao
        elif((isinstance (aceitacao,int))and (aceitacao <(len(AceitacaoRefeicao)))):
            self.aceitacao = AceitacaoRefeicao(aceitacao).name
        else: 
            self.aceitacao = None
        