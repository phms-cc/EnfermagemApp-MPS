
from SingletonMeta import SingletonMeta

class FachadaCadastroUsuario(metaclass=SingletonMeta): 
  def cadastro_usuario(self,login,senha,nome)
	  controlador = UserController()
	  user = controlador.get_user(login)
	  if (user is None):
		  usuario = controlador.criar_usuario(login,senha,nome)
      controlador.salvar_usuario(usuario)
