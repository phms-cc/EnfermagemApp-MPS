from models.elderly import Idoso
from SingletonMeta import SingletonMeta

class PacienteController(metaclass=SingletonMeta):
    def criar_paciente_idoso(self, nome, idade, peso, altura, endereço):
        # Criar um novo paciente idoso
        novo_paciente = Idoso(nome, idade, peso, altura, endereço)
        
        return novo_paciente
   
    def list_comorbidades(self,paciente):
        comorbidades = paciente.getComorbidades()
        for comorbidade in comorbidades:
            print(comorbidade, end = " ")

    def list_paciente(self,paciente):
        print("Nome: " + paciente.getNome() + " idade:" + str(paciente.getIdade()),end = "")
        print(" peso:" + str(paciente.getPeso())+ " altura:" + str(paciente.getAltura()))
        
    def list_pacientes(self,pacientes):
        for paciente in pacientes:
            self.list_paciente(paciente)
            
    def delete_paciente(self,i):
        pass             
            
    def paciente_getNome(self,paciente):
        paciente.getNome()

    def paciente_setNome(self,paciente,nome):
        paciente.setNome(nome)

    def paciente_getIdade(self,paciente):
        paciente.getIdade()

    def paciente_setIdade(self,paciente,idade):
        paciente.setIdade(idade)

    def paciente_getAltura(self,paciente):
        paciente.getAltura()

    def paciente_setAltura(self,paciente,altura):
        paciente.setAltura(altura)

    def paciente_getPeso(self,paciente):
        paciente.getPeso()

    def paciente_setPeso(self,paciente,peso):
        paciente.setPeso(peso)
    
    def paciente_getEndereco(self,paciente):
        paciente.getEndereco()

    def paciente_setEndereco(self,paciente,endereco):
        paciente.setPeso(endereco)
