# -*- coding: utf-8 -*-
"""
Created on Sun May 14 17:55:29 2023

@author: filip
"""

from TemplateGeraRelatorio import GeraRelatorio
import datetime

class GeraRelatorioPDF(GeraRelatorio):
    def __init__(self,file_name,users):
        super().__init__(file_name,users)
	self.file = None
        
    def create_file(self):
        #funcoes de criar e abrir arquivo
		file = self.file_name + ".pdf"
		self.file = open(file, 'w')
		pass
    

    def close_file(self):
		self.file.close()
    

    def parseInfo(self):
        #metodo de criar a informacao no estilo documento pdf
    
    
    
