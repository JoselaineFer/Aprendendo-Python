contatos = [
    {"nome": "Josi", "telefone": "53984427414"},
    {"nome": "Alex", "telefone": "51988887777"}
]

def buscar_contato(nome_procurado):
    for contato in contatos:
        if contato["nome"].lower() == nome_procurado.lower():
            return contato
    return None

resultado = buscar_contato("josi")

if resultado:
    print(f"Encontrado: {resultado['nome']} - {resultado['telefone']}")
else:
    print("Contato não encontrado.")
