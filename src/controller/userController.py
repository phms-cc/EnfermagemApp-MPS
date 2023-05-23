from models.user import User
from interface.user_intra_interface_factory import UserIntraInterfaceFactory

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
        return novo_usuario
    
    def salvar_usuario(self,usuario):
        factory  = UserIntraInterfaceFactory()
        salvar_user = factory.getUserIntraInter()
        salvar_user.cadastrar_usuario(usuario)
        
        
    def get_user(self,login):
        factory  = UserIntraInterfaceFactory()
        salvar_user = factory.getUserIntraInter()
        user = salvar_user.obter_usuario(login)
        return user
        
    def delete_usuario(self,login):
        pass

    def change_user_password(self,login,new_password):
        user = self.get_user(login)
        user.set_password(new_password)
                
    def used_login(self,login):
        if (self.get_user(login) == None):
            return False
        return True
    
    def user_get_password(self,login):
        user = self.get_user(login)
        return user.get_password()

    def user_compare_password(self,user, password):
        return ((self.user_get_password())== (password))

    def user_get_email(self,login):
        user = self.get_user(login)
        return user.get_email()

    def user_set_email(self,login,email):
        user = self.get_user(login)
        user.set_email(email)

    def user_get_telefone(self,login):
        user = self.get_user(login)
        return user.get_telefone()

    def user_set_telefone(self,login,telefone):
        user = self.get_user(login)
        user.set_telefone(telefone)

    def user_get_nome(self,login):
        user = self.get_user(login)
        return user.get_nome()

    def user_set_nome(self,login,nome):
        user = self.get_user(login)
        user.set_nome(nome)
