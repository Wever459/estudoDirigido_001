def cadastrar(lista, item):
    """
    Cadastra um item na lista, verificando se ele já existe.
    """
    if item in lista:
        print("❌ Item já cadastrado!")
    else:
        lista.append(item)
        print("✔ Item cadastrado!")

def listar(lista):
    """
    Exibe os itens da lista com numeração.
    """
    if not lista:
        print("Lista vazia.")
    else:
        print("\n--- Lista de Itens ---")
        for i, item in enumerate(lista, 1):
            print(f"{i}. {item}")
        print("---------------------")

def remover(lista, numero_item):
    """
    Remove um item da lista usando o número exibido na listagem.
    O número do item é 1-based (começa em 1).
    """
    try:
        # Converte para índice 0-based
        indice = int(numero_item) - 1
        
        # Verifica se o índice é válido
        if 0 <= indice < len(lista):
            item_removido = lista.pop(indice)
            print(f"🗑 Item '{item_removido}' removido!")
        else:
            print("❌ Número de item inválido.")
    except ValueError:
        print("❌ Entrada inválida. Digite um número.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")