# -*- coding: utf-8 -*-
"""
Created on Tue May  9 10:02:13 2023

@author: filip
"""

from enum import Enum
 
class TipoRefeicao(Enum):
    desejum = 1
    cafe = 2 #cafe da manha
    almoco = 3
    lanche  = 4 #lanche da tarde
    jantar = 5
    ceia = 6