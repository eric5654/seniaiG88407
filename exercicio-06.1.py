Menu = {'Big Mac': 20.00,
        'Cheese Burger': 40.00,
        'Milk Shake': 30.00
        }

pedido = []


def exibir_menu():
    print("Cardápio:")
    for item, preco in Menu.items():
        print(f"{item}: R${preco:.2f}")


def informe_item():
    item = input("Informe o item do cardápio: ")
    if item in Menu:
        pedido.append(item)
        print(f"Item '{item}' adicionado ao pedido.")
    else:
        print("Item não está no cardápio.")


def remover_item():
    item = input("Informe o item a ser removido do pedido: ")
    if item in pedido:
        pedido.remove(item)
        print(f"Item '{item}' removido do pedido.")
    else:
        print("Item não está no pedido.")


def exibir_pedido():
    print("Itens no pedido:")
    for item in pedido:
        print(item)


def calcular_pedido():
    total = sum(Menu[item] for item in pedido)
    print(f"Total do pedido: R${total:.2f}")

def salvar_pedido():
        with open('pedido.txt', 'w') as arquivo:
            arquivo.write("Itens no pedido:\n")
            for item in pedido:
                arquivo.write(f"{item}\n")
                total = sum(Menu[item] for item in pedido)
                arquivo.write(f"\nTotal do pedido: R${total:.2f}")

while True:
    print("[1] Exibir menu\n[2] Informar item\n[3] Remover item\n[4] Exibir pedido\n[5] Calcular pedido\n[6] Encerrar pedido")
    opcao = int(input("Informe a opção desejada: "))

    if opcao == 1:
        exibir_menu()
    elif opcao == 2:
        informe_item()
    elif opcao == 3:
        remover_item()
    elif opcao == 4:
        exibir_pedido()
    elif opcao == 5:
        calcular_pedido()
        
    elif opcao == 6:
        print("Encerrando o pedido.")
        salvar_pedido()
        break
    else:
        print("Opção inválida. Tente novamente.")


#while True:
#    elif opcao == 6:
#    salvar_pedido()
#    print("Pedido salvo no arquivo 'pedido.txt'.")
#    break