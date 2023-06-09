from .interface import CommandInterface

class showPacientes(CommandInterface):

    def __init__(self, receptor: any, information: any) -> None:
        self.__receptor = receptor
        self.__message = self.__format_information(information)
    
    def show_allpacientes(self):
        return paciente.show_allpacientes()
