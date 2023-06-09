from business.pacientController import PacienteController

class FormulárioCadastroPaciente:
    def __init__(self):
        self.nome = None
        self.idade = None
        self.peso = None
        self.altura = None
        self.endereço = None

    def preencher_formulário(self):
        self.nome = input("Digite o nome do paciente: ")
        self.idade = input("Digite a idade do paciente: ")
        self.peso = input("Digite o peso do paciente: ")
        self.altura = input("Digite a altura do paciente: ")
        self.endereço = input("Digite o endereço do paciente: ")

    def cadastrar(self, usuário):
        paciente = PacienteController.criar_paciente_idoso(self.nome, self.idade, self.peso, self.altura, self.endereço)
        usuário.adicionar_paciente(paciente)
        print("Paciente cadastrado com sucesso!")