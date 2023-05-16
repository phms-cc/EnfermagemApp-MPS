from models.user import User
from interface.userFacade import UserFacade

class UserController:
    def criar_usuario(login, senha, nome):
        # Verificar as restrições do login
        if len(login) > 12 or len(login) == 0 or any(char.isdigit() for char in login):
            return False
        # Verificar as restrições da senha
        if (
            len(senha) > 20
            or len(senha) < 8
            or not any(char.isalpha() for char in senha)
            or sum(char.isdigit() for char in senha) < 2
        ):
            return False
        # Criar um novo usuário
        
        novo_usuario = User(login, senha, nome)
        salvar_user = UserFacade()
        salvar_user.cadastrar_usuario(novo_usuario)
        return novo_usuario