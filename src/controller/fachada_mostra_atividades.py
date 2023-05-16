from SingletonMeta import SingletonMeta

class FachadaMostraAtividades(metaclass=SingletonMeta):

    def show_atividades(self,paciente):
        atividades = paciente.get_atividades()
        print ("Atividades do Paciente " + paciente.getNome())
        for atividade in atividades:
            print ("Atividade do tipo " + atividade.get_tipo() + " Data: " + str(atividade.get_data()))
