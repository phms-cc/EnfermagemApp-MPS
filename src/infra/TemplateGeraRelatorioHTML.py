# -*- coding: utf-8 -*-
"""
Created on Sun May 14 17:27:00 2023

@author: filip
"""

from TemplateGeraRelatorio import GeraRelatorio
import datetime

class GeraRelatorioHTML(GeraRelatorio):
	def __init__(self,file_name,users):
		self.file_name = file_name
		self.users = users
		self.info = []
		self.file = None
        
	def create_file(self):
        #funcoes de criar e abrir arquivo
		file = self.file_name + ".html"
		self.file = open(file, 'w')
		pass
    
    
	def close_file(self):
		self.file.close()
		pass    

	def parseInfo(self):
		#funcao de gerar info no formato desejado
		pass
		head = """<html>
        <head>
        <title>Relatorio de Usuarios</title>
        </head>
        """
		x = datetime.datetime.now()
		infos = []
		i = []
		body1 = """<body>
        <h2>Welcome Relatorio de Usuario data""" + str(x) + """ </h2>"""
		for info in self.info:
            i = """ <p> """ + info + """ </p>"""
            infos.append(i)
		body2 = """</body> </html> """
		self.file.write(head)
		self.file.write(body1)
		self.file.write(infos)
		self.file.write(body2)