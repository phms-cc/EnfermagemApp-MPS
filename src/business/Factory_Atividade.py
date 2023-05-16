# -*- coding: utf-8 -*-
"""
Created on Tue May  9 21:18:18 2023

@author: filip
"""
from Atividade import Atividade
from abc import ABC, abstractmethod

class Atividade_Factory(ABC):
    @abstractmethod
    def __init__(self):
        #https://refactoring.guru/design-patterns/factory-method/python/example

        pass
    
    @abstractmethod
    def getAtividade(self) ->Atividade:
        pass
    
  