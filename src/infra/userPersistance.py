class UserPersistencia:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.usuarios = []
        return cls._instance

    def gravar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def obter_usuarios(self):
        return self.usuarios