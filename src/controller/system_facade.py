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
    
    def edit_user_password(self, login, newpassword):
        return self.user_controller.edit_password(self.user_controller, login, newpassword)
    
    def compare_user_password(self, password):
        return self.user_controller.compare_password(self.user_controller, password)

    def user_used_login(self, login):
        return self.user_controller.used_login(self.user_controller, login)
    
