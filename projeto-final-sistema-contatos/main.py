import json
import os

ARQUIVO_DADOS = "contatos.json"


class Contato:
    """Representa um contato com nome, telefone e email."""

    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def para_dicionario(self):
        """Converte o contato num dicionário, pronto pra salvar em JSON."""
        return {"nome": self.nome, "telefone": self.telefone, "email": self.email}

    def __str__(self):
        return f"{self.nome} | Tel: {self.telefone} | Email: {self.email}"


class GerenciadorContatos:
    """Gerencia a lista de contatos: adicionar, buscar, editar, remover e salvar."""

    def __init__(self):
        self.contatos = []
        self.carregar()

    def adicionar(self, nome, telefone, email):
        contato = Contato(nome, telefone, email)
        self.contatos.append(contato)
        self.salvar()
        print(f"Contato '{nome}' adicionado com sucesso!")

    def listar(self):
        if not self.contatos:
            print("Nenhum contato cadastrado ainda.")
            return
        for indice, contato in enumerate(self.contatos, start=1):
            print(f"{indice}. {contato}")

    def buscar(self, nome_procurado):
        for contato in self.contatos:
            if contato.nome.lower() == nome_procurado.lower():
                return contato
        return None

    def editar(self, nome_procurado, novo_telefone, novo_email):
        contato = self.buscar(nome_procurado)
        if contato:
            contato.telefone = novo_telefone
            contato.email = novo_email
            self.salvar()
            print(f"Contato '{nome_procurado}' atualizado!")
        else:
            print("Contato não encontrado.")

    def remover(self, nome_procurado):
        contato = self.buscar(nome_procurado)
        if contato:
            self.contatos.remove(contato)
            self.salvar()
            print(f"Contato '{nome_procurado}' removido!")
        else:
            print("Contato não encontrado.")

    def salvar(self):
        with open(ARQUIVO_DADOS, "w") as arquivo:
            dados = [contato.para_dicionario() for contato in self.contatos]
            json.dump(dados, arquivo)

    def carregar(self):
        if os.path.exists(ARQUIVO_DADOS):
            with open(ARQUIVO_DADOS, "r") as arquivo:
                dados = json.load(arquivo)
                self.contatos = [Contato(d["nome"], d["telefone"], d["email"]) for d in dados]


def pedir_texto_nao_vazio(mensagem):
    """Pergunta algo e repete até a pessoa digitar um texto de verdade."""
    while True:
        texto = input(mensagem)
        if texto.strip() != "":
            return texto
        print("Isso não pode ficar em branco, tenta de novo.")


def exibir_menu():
    print("\n===== SISTEMA DE CONTATOS =====")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contato")
    print("4 - Editar contato")
    print("5 - Remover contato")
    print("6 - Sair")


def main():
    gerenciador = GerenciadorContatos()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                nome = pedir_texto_nao_vazio("Nome: ")
                telefone = pedir_texto_nao_vazio("Telefone: ")
                email = pedir_texto_nao_vazio("Email: ")
                gerenciador.adicionar(nome, telefone, email)

            elif opcao == "2":
                gerenciador.listar()

            elif opcao == "3":
                nome = input("Nome a buscar: ")
                encontrado = gerenciador.buscar(nome)
                print(encontrado if encontrado else "Contato não encontrado.")

            elif opcao == "4":
                nome = input("Nome do contato a editar: ")
                novo_telefone = pedir_texto_nao_vazio("Novo telefone: ")
                novo_email = pedir_texto_nao_vazio("Novo email: ")
                gerenciador.editar(nome, novo_telefone, novo_email)

            elif opcao == "5":
                nome = input("Nome do contato a remover: ")
                gerenciador.remover(nome)

            elif opcao == "6":
                print("Encerrando o sistema. Até mais!")
                break

            else:
                print("Opção inválida, tenta de novo.")

        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")


if __name__ == "__main__":
    main()
