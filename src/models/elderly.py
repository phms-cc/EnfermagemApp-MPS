from pacient import Paciente

class Idoso(Paciente):
    def __init__(self, nome, idade, peso, altura, endereço, alguma_propriedade_adicional):
        super().__init__(nome, idade, peso, altura, endereço)
        self.alguma_propriedade_adicional = alguma_propriedade_adicional