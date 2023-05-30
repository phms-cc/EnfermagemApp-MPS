from SingletonMeta import SingletonMeta
from src.controller.userController import UserController
from src.controller.mealController import RefeicaoController
from src.controller.activityController import AtividadeController
from src.controller.patientController import PacienteController

class SystemFacade(metaclass=SingletonMeta):
    def __init__(self):
        
        self.user_controller = UserController();
        self.meal_controller = RefeicaoController;
        self.activity_controller = AtividadeController;
        self.patient_controller = PacienteController;

    def create_user(self, login, senha, nome):
        return self.user_controller.create(login, senha, nome)
    
    def get_user(self,login):
        return self.user_controller.get(self.user_controller, login)
    
    def get_all_users(self):
        return self.user_controller.get_all(self.user_controller)
    
    def save_user(self,usuario):
        return self.user_controller.save(self.user_controller,usuario)
    
    def delete_user(self, login):
        return self.user_controller.delete(self, login)
    
    def get_user_password(self, login):
        return self.user_controller.get_password(self.user_controller, login)
    
    def set_user_password(self, login, old_password, new_password):
        # comentar com o professor se é melhor usar o controller ou chamar o
        # método da própria fachada.
        password_validate = self.compare_user_password(old_password)
        
        if(password_validate == True):
            return self.user_controller.edit_password(self.user_controller, login, new_password)
        
        print("Invalid password")
        return 0

    def compare_user_password(self, password):
        return self.user_controller.compare_password(self.user_controller, password)

    def user_get_email(self, login):
        return self.user_controller.get_email(self.user_controller, login)
    
    def user_set_email(self, login, email):
        self.user_controller.set_email(self.user_controller, login, email)

    def user_used_login(self, login):
        return self.user_controller.used_login(self.user_controller, login)
    
    def user_set_login(self, email, login):
        self.user_controller.set_login(self.user_controller, email, login)
    
    def user_get_login(self, email):
        return self.user_controller.get_login(self.user_controller, email)
    
    def user_set_telefone(self, login, telefone):
        self.user_controller.set_telefone(self.user_controller, login, telefone)

    def user_get_telefone(self, login):
        self.user_controller.get_telefone(self.user_controller, login)

    def user_set_nome(self, login, nome):
        self.user_controller.set_nome(self.user_controller, login, nome)

    def user_get_nome(self, login):
        self.user_controller.get_nome(self.user_controller, login)
    
    def user_signup(self, login, senha, nome):
        user = self.user_controller.get(login)
        if (user is None):
            usuario = self.user_controller.create(login,senha,nome)
            return self.user_controller.save(usuario)
        return self.user_controller.get(user)

    
