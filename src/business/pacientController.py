from models.elderly import Idoso

class PacienteController:
    def criar_paciente_idoso(self, nome, idade, peso, altura, endereço):
        # Criar um novo paciente idoso
        novo_paciente = Idoso(nome, idade, peso, altura, endereço)
        
        return novo_paciente