from abc import ABC, abstractmethod

class UserIntraInterfaceAbstract(ABC):

    @abstractmethod
    def cadastrar_usuario(self,usuario):
        pass

    @abstractmethod
    def obter_usuarios(self):
        pass
  
    @abstractmethod
    def obter_usuario(self, login):
        pass
