class User:
    def __init__(self, login, senha, nome):
        self.login = login
        self.senha = senha
        self.nome = nome
        self.pacientes = []

    def adicionar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def remover_paciente(self, paciente):
        self.pacientes.remove(paciente)