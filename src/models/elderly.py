from pacient import Paciente

class Idoso(Paciente):
    def __init__(self, nome, idade, peso, altura, endereço):
        super().__init__(nome, idade, peso, altura, endereço)
