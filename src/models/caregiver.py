from user import User


class Cuidador(User):
    def __init__(self, login, senha, nome):
        super().__init__(login, senha, nome)
        self.pacientes = []

    def adicionar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def remover_paciente(self, paciente):
        self.pacientes.remove(paciente)
