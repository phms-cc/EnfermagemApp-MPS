# -*- coding: utf-8 -*-
"""
Created on Tue May  9 09:55:41 2023

@author: filip
"""

from enum import Enum
 
class AceitacaoRefeicao(Enum):
    recusou = 0
    baixa = 1
    moderada = 2
    completa = 3