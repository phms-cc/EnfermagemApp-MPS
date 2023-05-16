

#https://pt.stackoverflow.com/questions/72685/existe-interfaces-no-python

from abc import ABC, abstractmethod
 



class Paciente(ABC):

    @abstractmethod
    def getID(self):
        raise NotImplementedError()
    
    @abstractmethod
    def compareID(self, i):
        raise NotImplementedError()
    
    @abstractmethod
    def getNome(self):
        raise NotImplementedError()
    
    @abstractmethod
    def setNome(self,nome):
        raise NotImplementedError()
    
    @abstractmethod
    def getIdade (self):
        raise NotImplementedError()
    
    @abstractmethod
    def setIdade(self,idade):
        raise NotImplementedError()
    
    @abstractmethod
    def getPeso(self):
        raise NotImplementedError()
    
    @abstractmethod
    def setPeso(self,peso):
        raise NotImplementedError()
    
    @abstractmethod
    def getAltura(self):
        raise NotImplementedError()
    
    @abstractmethod
    def setAltura(self):
        raise NotImplementedError()
    
    @abstractmethod
    def getEndereco(self):
        raise NotImplementedError()
    
    @abstractmethod
    def setEndereco(self):
        raise NotImplementedError()
    
    @abstractmethod
    def getComorbidades(self):
        raise NotImplementedError()
    
    @abstractmethod
    def addComorbidade(self):
        raise NotImplementedError()
    
    @abstractmethod
    def hasComorbidade(self):
        raise NotImplementedError()
    
    @abstractmethod
    def nComorbidades(self):
        raise NotImplementedError()
    
    @abstractmethod
    def removeComorbidade(self,comorbidade):
        raise NotImplementedError()

