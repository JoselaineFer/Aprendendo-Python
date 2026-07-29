contatos = []

def adicionar_contato(nome, telefone):
    contatos.append({"nome": nome, "telefone": telefone})
    print(f"Contato {nome} adicionado!")

def listar_contatos():
    if not contatos:
        print("Nenhum contato cadastrado.")
    for contato in contatos:
        print(f"{contato['nome']}: {contato['telefone']}")

while True:
    print("\n1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        adicionar_contato(nome, telefone)
    elif opcao == "2":
        listar_contatos()
    elif opcao == "3":
        print("Saindo... até mais!")
        break
    else:
        print("Opção inválida, tenta de novo.")
