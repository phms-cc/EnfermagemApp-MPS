from SingletonMeta import SingletonMeta
from src.controller.userController import UserController
from src.controller.mealController import RefeicaoController
from src.controller.activityController import AtividadeController
from src.controller.patientController import PacienteController
from src.controller.iterator.ElderlyIterator import ElderlyIterator

class SystemFacade(metaclass=SingletonMeta):
    def __init__(self):
        
        self.user_controller = UserController;
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
        return self.user_controller.set_password(self.user_controller, login, old_password, new_password)

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
    
    def user_set_phone(self, login, phone):
        self.user_controller.set_phone(self.user_controller, login, phone)

    def user_get_phone(self, login):
        return self.user_controller.get_phone(self.user_controller, login)

    def user_set_name(self, login, name):
        self.user_controller.set_name(self.user_controller, login, name)

    def user_get_name(self, login):
        return self.user_controller.get_name(self.user_controller, login)
    
    def user_signup(self, login, senha, nome):
        return self.user_controller.signup(self.user_controller, login, senha, nome)
    
    def list_user_patients(self, login):
        iterator = ElderlyIterator(self.user_controller.get_pacientes(login))
        print(iterator.__next__().getNome())

    def create_patient(self, name, age, weight, height, address):
        return self.patient_controller.criar_paciente_idoso(
            self.patient_controller, 
            name,
            age,
            weight,
            height,
            address
            )

    def set_patient_name(self, patient, name):
        self.patient_controller.set_nome(self.patient_controller, patient, name)

    def get_patient_name(self, patient):
        return self.patient_controller.get_nome(self.patient_controller, patient)
    
    def set_patient_age(self, patient, age):
        self.patient_controller.set_nome(self.patient_controller, patient, age)

    def get_patient_age(self, patient):
        return self.patient_controller.get_idade(self.patient_controller, patient)
    
    def set_patient_height(self, patient, height):
        self.patient_controller.set_altura(self.patient_controller, patient, height)

    def get_patient_height(self, patient):
        return self.patient_controller.get_altura(self.patient_controller, patient)
    
    def set_patient_weight(self, patient, weight):
        self.patient_controller.set_peso(self.patient_controller, patient, weight)

    def get_patient_weight(self, patient):
        return self.patient_controller.get_peso(self.patient_controller, patient)
    
    def set_patient_address(self, patient, address):
        self.patient_controller.set_endereco(self.patient_controller, patient, address)

    def get_patient_address(self, patient):
        return self.patient_controller.get_endereco(self.patient_controller, patient)
    
    def add_patient_comorbidity(self, patient, comorbidity):
        self.patient_controller.add_comorbidade(self.patient_controller, patient, comorbidity)
    
    def remove_patient_comorbidity(self, patient, comorbidity):
        self.patient_controller.remove_comorbidade(self.patient_controller, patient, comorbidity)

    def list_patient_comorbidities(self, patient):
        comorbidades = patient.get_comorbidades(patient)
        for comorbidade in comorbidades:
            print(comorbidade, end = " ")

    def add_patient_activity(self, patient, activity):
        self.patient_controller.add_atividade(self.patient_controller, patient, activity)

    def remove_patient_activity(self, patient, activity):
        self.patient_controller.remove_atividade(self.patient_controller, patient, activity)

    def get_patient_activities(self, patient):
        return self.patient_controller.get_atividades(self.patient_controller, patient)
    
    def list_patient_activities(self, patient):
        atividades = patient.get_atividades()
        print ("Atividades do Paciente " + patient.getNome())
        for atividade in atividades:
            print ("Atividade do tipo " + atividade.get_tipo() + " Data: " + str(atividade.get_data()))