# -*- coding: utf-8 -*-
"""
Created on Sun May  7 18:24:09 2023

@author: filip
"""

from Atividade import Atividade
from EnumAreasLavadas import AreasLavadas

class AtividadeHigiene(Atividade):
    def __init__(self):
        super().__init__()
        self.quantidade_banhos = 0
        self.quantidade_troca_frauda = 0
        self.quantidade_higiene_intima = 0
        self.areaslavadas = []
        
    def set_quantidade_banho(self, quantidade):
        self.quantidade_banhos = quantidade
        if(quantidade>5):
            self.quantidade_banhos = 5
    
    def get_quantidade_banho(self):
        return self.quantidade_banhos

    
    def set_quantidade_frauda(self, quantidade):
        self.quantidade_troca_frauda = quantidade
        if(quantidade>5):
            self.quantidade_troca_frauda = 5
        
    def get_quantidade_frauda(self):
        return self.quantidade_troca_frauda
    
    def set_quantidade_higiene_intima(self, quantidade):
        self.quantidade_higiene_intima = quantidade
        if(quantidade>5):
            self.quantidade_higiene_intima  = 5
    
    def get_quantidade_higiene_intima (self):
        return self.quantidade_higiene_intima 
    
    def set_areaslavadas_inicio(self):
        for x in range (len(AreasLavadas)):
            self.areaslavadas.append(False)
            #inicialmente, para cada area que pode ser lavada, temos false
    
    def add_arealavada(self, arealavada):
        #verificar se foi passado um valor ou
        #um membro do ENUM AreasLavadas
        
        if(isinstance (arealavada,int)):
            self.areaslavadas[arealavada] = True
        elif(arealavada in AreasLavadas.__members__):
            x = AreasLavadas[arealavada].value
            self.areaslavadas[x] = True
        else:
            pass
            #ou seila, levantar um erro
            
        
        
    def remove_arealavada(self, arealavada):
        #verificar se foi passado um valor ou
        #um membro do ENUM AreasLavadas
        
        if(isinstance (arealavada,int)):
            self.areaslavadas[arealavada] = False
        elif(arealavada in AreasLavadas.__members__):
            x = AreasLavadas[arealavada].value
            self.areaslavadas[x] = False
        else:
            pass
            #ou seila, levantar um erro