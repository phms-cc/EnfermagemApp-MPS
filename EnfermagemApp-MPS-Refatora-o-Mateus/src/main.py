from form.userForm import UserForm
from interface.userFacade import UserFacade

def exibir_menu():
    print("Menu:")
    print("1 - Cadastrar Usuário")
    print("2 - Gerenciar Usuário")
    print("0 - Sair")


def cadastrar_usuario():
    formulário_usuário = UserForm()
    formulário_usuário.preencher_formulario()


def gerenciar_usuarios():
    persistência = UserFacade()
    usuários = persistência.obter_usuarios()

    print("Usuários Cadastrados:")
    for usuário in usuários:
        print("Login:", usuário.login)
        print("Senha:", usuário.senha)
        print("Pacientes:", len(usuário.pacientes))
        print("-" * 20)


# Exemplo de uso:
while True:
    exibir_menu()
    opção = input("Digite a opção desejada: ")

    if opção == "1":
        cadastrar_usuario()
    elif opção == "2":
        gerenciar_usuarios()
    elif opção == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
