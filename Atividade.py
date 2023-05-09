# -*- coding: utf-8 -*-
"""
Created on Sun May  7 16:00:45 2023

@author: filip
"""



# tipos de atividade:
#alimentação, hidratação, higiene e medicação
class Atividade:
    def __init__(self):
        self.anotacao = None
        self.data = None
        self.imagens = []
        self.alarme = None
    
    def get_anotacao(self):
        return self.anotacao
    def set_anotacao (self,anotacao):
        self.anotacao = anotacao
        
    def get_data(self):
        return self.data
    def set_data(self,data):
        self.data = data
    
    def add_imagem(self,imagem):
        self.imagens.append(imagem)
    def get_imagens(self):
        return self.imagens
    
    def set_alarme(self,alarme):
        self.alarme = alarme
    def get_alarme(self):
        return self.alarme
        