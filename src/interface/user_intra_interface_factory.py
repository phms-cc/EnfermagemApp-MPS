from user_intra_interface import UserIntraInterface
from user_intra_interface_abstractfactory import UserIntraInterface_AbstractFactory


class UserIntraInterface_Factory(UserIntraInterface_AbstractFactory):
	def __init__ (self):
		pass

	def getUserIntraInter(self):
		user_intra_interface = UserIntraInterface()
		return user_intra_interface

	def cadastrar_usuario(self,usuario):
		produto = self.getUserIntraInter()
		produto.cadastrar_usuario(usuario)
