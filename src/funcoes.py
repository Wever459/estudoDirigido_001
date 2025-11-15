#funcoes.py

def exibir_menu():
    print("\n[1] Cadastrar item [2] Listar itens [0] Sair")


def cadastrar(itens):

    nome=input("Digite o nome do item: ").strip()

    if not nome:
        print("X Nome não pode ser vazio.")

        return
    
    if nome in itens:
        print("X Item já existe.")

        return
    itens.append(nome)
    print("Item cadastrado!")

def listar(itens):

    if not (itens):
        print("Nenhum item cadastrado.")

    else:

        for i, nome in enumerate(itens, start=1):
            print(f"{i}.{nome}")