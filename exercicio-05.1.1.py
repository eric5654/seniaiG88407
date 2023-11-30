Usuarios = {'Junior': '34546'}

def cadastro_de_usuario():
    print("Cadastre seu Usuario agora")
    Usuario = input("Digite o nome de usuario: ")
    if Usuario in Usuarios:
        print("Usuario já cadastrado!")
    else:
        print("Usuario Cadastrado!")
        Usuarios[Usuario] = input("Digite a senha: ")

def fazer_login():
    print("Iniciaremos o login neste momento!")
    Usuario = input("Digite seu Usuario: ")
    senha = input("Digite sua Senha: ")
    if Usuario in Usuarios and senha == Usuarios[Usuario]:
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos.")

Usuario = 0
while Usuario != 3:
    print("[1] Cadastrar usuário\n[2] Fazer login\n[3] Encerrar programa")
    opcao = int(input("Insira a opção desejada: "))

    if opcao == 1:
        cadastro_de_usuario()
    elif opcao == 2:
        fazer_login()
    elif opcao == 3:
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida!")