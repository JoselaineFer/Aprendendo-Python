import json
import os
import re
from datetime import datetime

ARQUIVO_DADOS = "adega.json"


class Vinho:
    """Classe base para qualquer vinho da adega."""

    def __init__(self, nome, safra, prateleira):
        self.nome = nome
        self.safra = safra
        self.prateleira = prateleira
        self.aberta = False

    def descricao(self):
        """Sobrescrita pelas classes filhas — cada tipo descreve do seu jeito."""
        return f"{self.nome} ({self.safra})"

    def harmonizacao(self):
        """Sobrescrita pelas classes filhas com sugestão de acompanhamento."""
        return "Harmonização não definida"

    def para_dicionario(self):
        return {
            "tipo": self.__class__.__name__,
            "nome": self.nome,
            "safra": self.safra,
            "prateleira": self.prateleira,
            "aberta": self.aberta,
        }


class VinhoTinto(Vinho):
    def __init__(self, nome, safra, prateleira, teor_alcoolico):
        super().__init__(nome, safra, prateleira)
        self.teor_alcoolico = teor_alcoolico

    def descricao(self):
        return f"[Tinto] {self.nome} ({self.safra}) - {self.teor_alcoolico}%"

    def harmonizacao(self):
        return "Combina com carnes vermelhas e queijos maduros"

    def para_dicionario(self):
        dados = super().para_dicionario()
        dados["teor_alcoolico"] = self.teor_alcoolico
        return dados


class VinhoBranco(Vinho):
    def __init__(self, nome, safra, prateleira, temperatura_ideal):
        super().__init__(nome, safra, prateleira)
        self.temperatura_ideal = temperatura_ideal

    def descricao(self):
        return f"[Branco] {self.nome} ({self.safra}) - servir a {self.temperatura_ideal}°C"

    def harmonizacao(self):
        return "Combina com peixes e frutos do mar"

    def para_dicionario(self):
        dados = super().para_dicionario()
        dados["temperatura_ideal"] = self.temperatura_ideal
        return dados


class Espumante(Vinho):
    def __init__(self, nome, safra, prateleira, metodo):
        super().__init__(nome, safra, prateleira)
        self.metodo = metodo

    def descricao(self):
        return f"[Espumante] {self.nome} ({self.safra}) - método {self.metodo}"

    def harmonizacao(self):
        return "Combina com aperitivos e sobremesas leves"

    def para_dicionario(self):
        dados = super().para_dicionario()
        dados["metodo"] = self.metodo
        return dados


def registrar_log(funcao):
    """Decorador que registra quando uma ação importante acontece na adega."""
    def embrulho(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
        agora = datetime.now().strftime("%d/%m/%Y %H:%M")
        print(f"[LOG {agora}] Ação '{funcao.__name__}' executada.")
        return resultado
    return embrulho


class Adega:
    def __init__(self):
        self.vinhos = []
        self.carregar()

    @registrar_log
    def adicionar_vinho(self, vinho):
        self.vinhos.append(vinho)
        self.salvar()
        print(f"Vinho adicionado: {vinho.descricao()}")

    def listar_vinhos(self):
        if not self.vinhos:
            print("Nenhum vinho cadastrado na adega.")
            return
        for indice, vinho in enumerate(self.vinhos, start=1):
            status = "aberta" if vinho.aberta else "fechada"
            print(f"{indice}. {vinho.descricao()} - garrafa {status}")

    def buscar_por_nome(self, nome_procurado):
        for vinho in self.vinhos:
            if vinho.nome.lower() == nome_procurado.lower():
                return vinho
        return None

    @registrar_log
    def abrir_garrafa(self, nome):
        vinho = self.buscar_por_nome(nome)
        if vinho is None:
            print("Vinho não encontrado.")
        elif vinho.aberta:
            print("Essa garrafa já está aberta.")
        else:
            vinho.aberta = True
            self.salvar()
            print(f"Garrafa de '{nome}' aberta! {vinho.harmonizacao()}.")

    def vinhos_disponiveis(self):
        """Generator: entrega um vinho fechado (disponível) de cada vez."""
        for vinho in self.vinhos:
            if not vinho.aberta:
                yield vinho

    def salvar(self):
        with open(ARQUIVO_DADOS, "w") as arquivo:
            dados = [vinho.para_dicionario() for vinho in self.vinhos]
            json.dump(dados, arquivo)

    def carregar(self):
        if os.path.exists(ARQUIVO_DADOS):
            with open(ARQUIVO_DADOS, "r") as arquivo:
                dados = json.load(arquivo)
                for item in dados:
                    if item["tipo"] == "VinhoTinto":
                        vinho = VinhoTinto(item["nome"], item["safra"], item["prateleira"], item["teor_alcoolico"])
                    elif item["tipo"] == "VinhoBranco":
                        vinho = VinhoBranco(item["nome"], item["safra"], item["prateleira"], item["temperatura_ideal"])
                    else:
                        vinho = Espumante(item["nome"], item["safra"], item["prateleira"], item["metodo"])
                    vinho.aberta = item["aberta"]
                    self.vinhos.append(vinho)


def validar_safra(safra):
    """Usa regex pra garantir que a safra é um ano de 4 dígitos, tipo 2019."""
    return bool(re.match(r"^\d{4}$", safra))


def exibir_menu():
    print("\n===== SISTEMA DE ADEGA =====")
    print("1 - Adicionar vinho tinto")
    print("2 - Adicionar vinho branco")
    print("3 - Adicionar espumante")
    print("4 - Listar todos os vinhos")
    print("5 - Listar vinhos disponíveis (fechados)")
    print("6 - Abrir uma garrafa")
    print("7 - Sair")


def main():
    adega = Adega()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                nome = input("Nome do vinho: ")
                safra = input("Safra (ano, ex: 2019): ")
                if not validar_safra(safra):
                    print("Safra inválida, use um ano com 4 dígitos.")
                    continue
                prateleira = input("Prateleira: ")
                teor = float(input("Teor alcoólico (%): "))
                adega.adicionar_vinho(VinhoTinto(nome, safra, prateleira, teor))

            elif opcao == "2":
                nome = input("Nome do vinho: ")
                safra = input("Safra (ano, ex: 2021): ")
                if not validar_safra(safra):
                    print("Safra inválida, use um ano com 4 dígitos.")
                    continue
                prateleira = input("Prateleira: ")
                temperatura = float(input("Temperatura ideal (°C): "))
                adega.adicionar_vinho(VinhoBranco(nome, safra, prateleira, temperatura))

            elif opcao == "3":
                nome = input("Nome do espumante: ")
                safra = input("Safra (ano, ex: 2020): ")
                if not validar_safra(safra):
                    print("Safra inválida, use um ano com 4 dígitos.")
                    continue
                prateleira = input("Prateleira: ")
                metodo = input("Método (ex: Champenoise, Charmat): ")
                adega.adicionar_vinho(Espumante(nome, safra, prateleira, metodo))

            elif opcao == "4":
                adega.listar_vinhos()

            elif opcao == "5":
                for vinho in adega.vinhos_disponiveis():
                    print(vinho.descricao())

            elif opcao == "6":
                nome = input("Nome do vinho a abrir: ")
                adega.abrir_garrafa(nome)

            elif opcao == "7":
                print("Fechando a adega. Até mais! 🍷")
                break

            else:
                print("Opção inválida, tenta de novo.")

        except ValueError:
            print("Valor inválido digitado, tenta de novo.")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")


if __name__ == "__main__":
    main()
