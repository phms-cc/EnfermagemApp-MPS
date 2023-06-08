from models.user import User
from interface.user_intra_interface_factory import UserIntraInterfaceFactory
from iterator.ElderlyIterator import ElderlyIterator

class UserController:
    def create(login, senha, nome):
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
    
    def save(self,usuario):
        factory  = UserIntraInterfaceFactory()
        salvar_user = factory.getUserIntraInter()
        salvar_user.cadastrar_usuario(usuario)
        
        
    def get(self,login):
        factory  = UserIntraInterfaceFactory()
        salvar_user = factory.getUserIntraInter()
        user = salvar_user.get_user_by_login(login)
        return user
    
    def get_all(self):
        factory = UserIntraInterfaceFactory()
        user_intra_inter = factory.getUserIntraInter()
        return user_intra_inter.obter_usuarios()
        
    def delete(self,login):
        factory  = UserIntraInterfaceFactory()
        user_intra_inter = factory.getUserIntraInter()
        user = user_intra_inter.get_user_by_login(login)
        ~user
        pass

    def signup(self, login, senha, nome):
        user = self.get(login)
        if (user is None):
            usuario = self.create(login,senha,nome)
            return self.save(usuario)
        return self.get(user)

    def set_password(self, login, old_password, new_password):
        password_validate = self.compare_password(old_password)
        
        if(password_validate == True):
            return self.edit_password(self, login, new_password)
        
        print("Invalid password")
        return 0
                
    def used_login(self,login):
        if (self.get_user(login) == None):
            return False
        return True
    
    def get_login(self, email):
        factory = UserIntraInterfaceFactory()
        user_intra_inter = factory.getUserIntraInter()
        user = user_intra_inter.get_user_by_email(email)
        return user.get_login()
    
    def set_login(self, email, new_login):
        factory = UserIntraInterfaceFactory()
        user_intra_inter = factory.getUserIntraInter()
        user = user_intra_inter.get_user_by_email(email)
        user.set_login(new_login)
    
    def get_password(self,login):
        user = self.get_user(login)
        return user.get_password()

    def compare_password(self, password):
        return ((self.get_password())== (password))

    def get_email(self,login):
        user = self.get_user(login)
        return user.get_email()

    def set_email(self,login,email):
        user = self.get_user(login)
        user.set_email(email)

    def get_phone(self,login):
        user = self.get_user(login)
        return user.get_phone()

    def set_phone(self,login,telefone):
        user = self.get_user(login)
        user.set_phone(telefone)

    def get_name(self,login):
        user = self.get_user(login)
        return user.get_name()

    def set_name(self,login,nome):
        user = self.get_user(login)
        user.set_name(nome)

    def get_pacientes(self,login):
        user = self.get_user(login)
        return user.get_pacientes()
    
    def set_pacientes(self,login,pacientes):
        user = self.get_user(login)
        user.set_pacientes(pacientes)

    def add_paciente(self, login, paciente):
        user = self.get_user(login)
        user.pacientes.append(paciente)

    def remove_paciente(self, login, paciente):
        user = self.get_user(login)
        user.pacientes.remove(paciente)

    def get_paciente(self, login, nome):
        pacientes = self.get_pacientes(login)
        iterator = ElderlyIterator(pacientes)
        iterator.__next__() if value.getNome() != nome else StopIteration
        return pacientes[iterator._position].getNome()
