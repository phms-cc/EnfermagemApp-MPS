from infra.userPersistance import UserPersistencia
from user_intra_interface_abstract import UserIntraInterfaceAbstract

class UserIntraInterface(UserIntraInterfaceAbstract):
    def __init__(self):
        self.persistencia = UserPersistencia()

    def cadastrar_usuario(self, usuario):
        self.persistencia.gravar_usuario(usuario)

    def obter_usuarios(self):
        return self.persistencia.obter_usuarios()
    
    def get_user_by_login(self, login):
        usuarios = self.obter_usuarios()
        for usuario in usuarios:
            if (usuario.get_login() == login):
                return usuario
        return None
    
    def get_user_by_email(self, email):
        usuarios = self.obter_usuarios()
        for usuario in usuarios:
            if (usuario.get_email() == email):
                return usuario
        return None
