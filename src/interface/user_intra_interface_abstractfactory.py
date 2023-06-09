from abc import ABC, abstractmethod

class UserIntraInterface_AbstractFactory(ABC):
    @abstractmethod
    def getUserIntraInter(self):
        pass
    
    def cadastrar_usuario(self,usuario):
        produto = self.getUserIntraInter()
        produto.cadastrar_usuario(usuario)
        pass
