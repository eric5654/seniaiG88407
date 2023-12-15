from ast import Break


Conta = {
         '500,00': '3456',
         '360,00':'4657',
         '900,00':  '5676'
}
conta = []

saldo = input("Informe seu Saldo: ")
senha = input("Unforme a sua Senha: ")


if saldo in     Conta and Conta[saldo] == senha:
   print("Senha armazenada! ")
else:
      print("Senha incorreta!" )

while True != 4:
          print("[1] Verificar_saldo\n[2] depositar_valor\n[3] retirar_valor\n[4]Sair :")
def Verificar_saldo ():
              print("Saldo: ")
              for saldo in Conta:
                  print(saldo)
def depositar_valor ():
        saldo = input("Informe a quantia : ")
        if conta in saldo:
         conta.append(saldo)
         print(f"Saldo '{saldo}' dinheiro depositado.")
        else:
                        print("Deposito não é possivel de efetuar.")

def retirar_valor ():
    saldo = input("Retire o valor: ")
    if saldo in conta:
        conta.remove(saldo)
        print(f"Saldo '{saldo}' valor a ser retirado.")
    else:
        print("Valor insuficiente")
def sair():
    
 opcao = str(input("Informe a opção desejada: "))
 if opcao == 1:
      Verificar_saldo()
 elif opcao == 2:
            depositar_valor  ()
 elif opcao == 3:
                retirar_valor()
 elif opcao == 4:
        sair()
print("ENCERRADO")
break
    else:
    print("Sair." )