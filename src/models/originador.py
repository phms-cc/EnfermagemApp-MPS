from models.memento import Memento

class Originador:
    def __init__(self):
        self.pacientes = []

    def adicionar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def remover_paciente(self, paciente):
        self.pacientes.remove(paciente)

    def get_pacientes(self):
        return self.pacientes

    def salvar_estado(self):
        return Memento(self.pacientes.copy())