from SingletonMeta import SingletonMeta

class FachadaMostraPaciente(metaclass=SingletonMeta):

  def list_paciente(self,paciente):
    print("Nome: " + paciente.getNome() + " idade:" + str(paciente.getIdade()),end = "")
    print(" peso:" + str(paciente.getPeso())+ " altura:" + str(paciente.getAltura()))
