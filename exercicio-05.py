Usuarios = {
         'Icaro': '3456',
         'Isabela': '4657',
         'Jonatas':  '5676'
}

usuario = input("Informe seu Usuario: ")
senha = input("Unforme a sua Senha")

if usuario in Usuarios and Usuarios[usuario] == senha:
   print("Login bem sucedido! ")
else:
      print("Usuario não existe!")