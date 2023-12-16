Conta = {
    '500,00': '3456',
    '360,00': '4657',
    '900,00': '5676'
}
conta = []

saldo = input("Informe seu Saldo: ")
senha = input("Informe a sua Senha: ")

if saldo in Conta and Conta[saldo] == senha:
    print("Senha armazenada!")
else:
    print("Senha incorreta!")

while True:
    print("[1] Verificar_saldo\n[2] depositar_valor\n[3] retirar_valor\n[4] Sair:")

    opcao = input("Informe a opção desejada: ")

    def Verificar_saldo():
        print("Saldo:")
        for saldo in Conta:
            print(saldo)

    def depositar_valor():
        saldo_deposito = input("Informe a quantia: ")
        print(f"Saldo '{saldo_deposito}' dinheiro depositado.")
        

    def retirar_valor():
        saldo_retirada = input("Retire o valor: ")
        if saldo_retirada in conta:
            conta.remove(saldo_retirada)
            print(f"Saldo '{saldo_retirada}' valor retirado.")
        else:
            print("Valor insuficiente.")

    def sair():
        print("ENCERRADO")
        exit()

    if opcao == '1':
        Verificar_saldo()
    elif opcao == '2':
        depositar_valor()
    elif opcao == '3':
        retirar_valor()
    elif opcao == '4':
        sair()
    else:
        print("Opção inválida. Tente novamente.")