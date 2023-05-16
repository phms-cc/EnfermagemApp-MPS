# -*- coding: utf-8 -*-
"""
Created on Sun May 14 16:37:06 2023

@author: filip
"""

from abc import ABC, abstractmethod

class GeraRelatorio(ABC):
	def __init__(self,file_name,users):
		self.file_name = file_name
		self.users = users
		self.info = []
	def create_file(self):
		#funcoes de criar e abrir arquivo
		pass
	def close_file(self):
		#funcao de fechar arquivo
		pass
    
	def extract_info(self):
		info = None
		for user in self.users:
			info = user.get_login() + " " + str(user.get_lastonline()) + " " + str(user.get_time_online())
			#ou qualquer outra informacao que se deseje ter no relatorio
			self.info.append(info)
			info = None
    
	def geraRelatorio(self):
		#funcao de gerar relatorio
        self.create_file()
        self.extract_info()
        self.parseInfo()
        self.close_file()
		pass

    @abstractmethod
	def parseInfo(self):
		#funcao de gerar info no formato desejado
		pass