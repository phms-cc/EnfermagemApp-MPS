from abc import ABC, abstractmethod


class Paciente(ABC):
    def __init__(self, nome, idade, peso, altura, endereço):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.endereço = endereço

    
    @abstractmethod
    def getID(self):
        pass
    
    @abstractmethod
    def compareID(self, i):
       pass
    
    @abstractmethod
    def getNome(self):
        pass
    
    @abstractmethod
    def setNome(self,nome):
        pass
    
    @abstractmethod
    def getIdade (self):
        pass
    
    @abstractmethod
    def setIdade(self,idade):
        pass
    
    @abstractmethod
    def getPeso(self):
        pass
    
    @abstractmethod
    def setPeso(self,peso):
        pass
    
    @abstractmethod
    def getAltura(self):
        pass
    
    @abstractmethod
    def setAltura(self):
        pass
    
    @abstractmethod
    def getEndereco(self):
        pass
    
    @abstractmethod
    def setEndereco(self):
        pass
    
    @abstractmethod
    def getComorbidades(self):
        pass
    
    @abstractmethod
    def addComorbidade(self):
        pass
    
    @abstractmethod
    def hasComorbidade(self):
        pass
    
    @abstractmethod
    def nComorbidades(self):
        pass
    
    @abstractmethod
    def removeComorbidade(self,comorbidade):
        pass
    
    @abstractmethod
    def add_atividade(self,atividade):
        pass
    @abstractmethod
    def get_atividades(self):
        pass
   
