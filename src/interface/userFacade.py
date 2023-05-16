from infra.userPersistance import UserPersistencia

class UserFacade:
    def __init__(self):
        self.persistencia = UserPersistencia()

    def cadastrar_usuario(self, usuario):
        self.persistencia.gravar_usuario(usuario)

    def obter_usuarios(self):
        return self.persistencia.obter_usuarios()
