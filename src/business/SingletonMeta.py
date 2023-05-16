# -*- coding: utf-8 -*-
"""
Created on Sun May 14 15:28:29 2023

@author: filip
"""

class SingletonMeta(type):


    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


