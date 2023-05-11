import re

class User: 
    def __init__(self,login,password):
        self.login = login
        self.password= password
        #por mais atributos:nome, email, telefone
        self.email = None
        self.telefone = None
        self.nome = None
        self.idosos = []
    
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
        
    def add_idosos(self,idoso):
        self.idosos.append(idoso)

        
class UserForm:
    def validate_login(self, login):
        if not login:
            return False
        if len(login) > 12:
            return False
        if any(char.isdigit() for char in login):
            return False
        return True
    
    def validate_password(self, password):
        if not password:
            return False
        if len(password) < 8 or len(password) > 20:
            return False
        if not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
            return False
        if len(re.findall('\d', password)) < 2:
            return False
        return True
    
    def validate_user(self, login,password):
        return self.validate_login(login) and self.validate_password(password)

class UserControl:
    def __init__(self):
        self.users = []
    def add_user(self,login,password):
        form = UserForm()
        if form.validate_user(login,password):
            new_user = User(login,password)
            self.users.append(new_user)
    
    def list_user(self,user_searched):
        for user in self.users:
            if(user_searched == user.get_login()):
                print("User:" + user.get_login() + " Password: "+ user.get_password() )
    def list_all_users(self):
        if(self.users):
            for user in self.users:
                print("User: " + user.get_login())
    def delete_user_bylogin(self, del_user):
        for user in self.users:
            if (del_user == user.get_login()):
                self.users.remove(user)
                break
    
    def change_user_password(self,user_name,new_password):
        for user in self.users:
            if(user_name == user.get_login()):
                user.set_password(new_password)
                
    def get_user_login(self,login):
        for user in self.users:
            if(login == user.get_login()):
                return user

    def user_get_password(self,login):
        user = self.get_user_login(login)
        return user.get_password()

    def user_compare_password(self,user, password):
        return ((self.user_get_password())== (password))

    def user_get_email(self,login):
        user = self.get_user_login(login)
        return user.get_email()

    def user_set_email(self,login,email):
        user = self.get_user_login(login)
        user.set_email(email)

    def user_get_telefone(self,login):
        user = self.get_user_login(login)
        return user.get_telefone()

    def user_set_telefone(self,login,telefone):
        user = self.get_user_login(login)
        user.set_telefone(telefone)

    def user_get_nome(self,login):
        user = self.get_user_login(login)
        return user.get_nome()

    def user_set_nome(self,login,nome):
        user = self.get_user_login(login)
        user.set_nome(nome)

if __name__ == "__main__":
    manager = UserControl()
    manager.add_user("joaosilva", "senha1234")
    manager.add_user("mariasilva", "senha01234")
    manager.add_user("pedroalmeida", "senha5678")
    manager.list_all_users()
    manager.delete_user_bylogin("joaosilva")
    print("joao silva deletado, nova lista:")
    manager.list_all_users()
    print("listando maria silva")
    manager.list_user("mariasilva")
    manager.change_user_password("mariasilva","123456789")
    manager.list_user("mariasilva")
