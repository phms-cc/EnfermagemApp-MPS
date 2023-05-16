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
        self.refeicoes = []
       
    def cria_refeicao(*args):
        pass
        if (len(args) == 0):
            refeicao = Refeicao()
        elif (len(args) == 1):
            refeicao = Refeicao()
            refeicao.set_tipo_refeicao(args[1])
        return refeicao
        
    def add_refeicao(self,refeicao):
        x = False
        for ref in self.refeicoes:
            if (ref.get_tipo_refeicao() == refeicao.get_tipo_refeicao()):
                x = True
                break
        if (x==False):
            self.refeicoes.append(refeicao)
            self.ordena_refeicoes()
    
    def get_refeicao (self,x):
        if (x in TipoRefeicao.__members__):
            for ref in self.refeicoes:
                if (ref.get_tipo_refeicao() == x):
                    return ref
        elif((isinstance (x,int))and (x <=(len(TipoRefeicao)))):
            return self.refeicoes[x]
        
    
    def cria_add_refeicao(self,*args):
        x = self.cria_refeicao(*args)
        self.add_refeicao(x)
        
    def ordena_refeicoes(self):
        self.refeicoes = sorted(self.refeicoes,key = lambda x: (x.tipo),reverse = False)
    
    def set_aceitacao_refeicao(self,x,aceitacao):
        refeicao = self.get_refeicao(x)
        refeicao.set_aceitacao(aceitacao)
        
    def get_aceitacao_refeicao(self,x):
        refeicao = self.get_refeicao(x)
        refeicao.get_aceitacao()
        
    def set_descricao_refeicao(self,x,descricao):
        refeicao = self.get_refeicao(x)
        refeicao.set_descricao(descricao)
        
    def get_descricao_refeicao(self,x):
        refeicao = self.get_refeicao(x)
        refeicao.get_descricao()

    
    
