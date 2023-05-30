class User:
    def __init__(self, login, senha, nome):
        self.login = login
        self.senha = senha
        self.nome = nome
        self.email = None
        self.telefone = None

    def __del__(self):
        pass
        
    def get_password(self):
        return self.password
    
    def get_login(self):
        return self.login
   
    def set_login(self,new_login):
        self.login = new_login
    
    def set_password(self,new_password):
        self.password = new_password
    
    def get_email(self):
        return self.email
    
    def set_email(self,email):
        self.email = email
    
    def get_telefone(self):
        return self.telefone
    
    def set_telefone(self,telefone):
        self.telefone = telefone
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self,nome):
        self.nome = nome
