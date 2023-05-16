from infra.userPersistance import UserPersistencia

class UserIntraInterface:
    def __init__(self):
        self.persistencia = UserPersistencia()

    def cadastrar_usuario(self, usuario):
        self.persistencia.gravar_usuario(usuario)

    def obter_usuarios(self):
        return self.persistencia.obter_usuarios()
    
    def obter_usuario(self, login):
        usuarios = self.obter_usuarios()
        for usuario in usuarios:
            if (usuario.get_login() == login):
                return usuario
        return None
