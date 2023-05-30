from models.elderly import Idoso

class PacienteController:
    def criar_paciente_idoso(self, nome, idade, peso, altura, endereço):
        # Criar um novo paciente idoso
        novo_paciente = Idoso(nome, idade, peso, altura, endereço)
        
        return novo_paciente
    
    def list_pacientes(self,pacientes):
        for paciente in pacientes:
            print("Nome: " + paciente.getNome() + " idade:" + str(paciente.getIdade()),end = "")
            print(" peso:" + str(paciente.getPeso())+ " altura:" + str(paciente.getAltura()))
            
    def delete_paciente(self):
        pass             
            
    def get_nome(self,paciente):
        return paciente.getNome()

    def set_nome(self,paciente,nome):
        paciente.setNome(nome)

    def get_idade(self,paciente):
        return paciente.getIdade()

    def set_idade(self,paciente,idade):
        paciente.setIdade(idade)

    def get_altura(self,paciente):
        return paciente.getAltura()

    def set_altura(self,paciente,altura):
        paciente.setAltura(altura)

    def get_peso(self,paciente):
        return paciente.getPeso()

    def set_peso(self,paciente,peso):
        paciente.setPeso(peso)
    
    def get_endereco(self,paciente):
        return paciente.getEndereco()

    def set_endereco(self,paciente,endereco):
        paciente.setPeso(endereco)

    def get_comorbidades(self, paciente):
        return paciente.getComorbidades()
    
    def list_comorbidades(self,paciente):
        comorbidades = get_comorbidades(paciente)
        for comorbidade in comorbidades:
            print(comorbidade, end = " ")