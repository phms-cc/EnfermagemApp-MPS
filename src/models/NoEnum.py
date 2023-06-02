# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 19:16:51 2023

@author: filip
"""

class NoEnum:
    def __init__(self):
        pass
    
    def get_valor(self,valor,enum):
        if(valor in enum.__members__):
            return valor
        elif((isinstance (valor,int))and (valor <=(len(enum)))):
            return enum(valor).name
        else:
            return None
    
    
    def no_enum(self,valor,enum):
        if(valor in enum.__members__):
            return True
        elif((isinstance (valor,int))and (valor <=(len(enum)))):
            return True
        else:
            return False