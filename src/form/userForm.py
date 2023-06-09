from business.userController import UserController

class UserForm:
    def __init__(self):
        self.login = None
        self.senha = None
        self.nome = None

    def preencher_formulario(self):
        self.nome = input("Digite o nome do usuário: ")
        self.login = input("Digite o login do usuário: ")
        self.senha = input("Digite a senha do usuário: ")
        self.cadastrar()

    def cadastrar(self):
        usuario = UserController.criar_usuario(self.login, self.senha, self.nome)
        
        print("Usuário cadastrado com sucesso!")