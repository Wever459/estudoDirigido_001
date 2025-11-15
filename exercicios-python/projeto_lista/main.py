from funcoes import cadastrar, listar, remover # Importamos 'remover'

itens = []

while True:
    print("\n--- Menu ---")
    print("[1] Cadastrar")
    print("[2] Listar")
    print("[3] Remover") # Nova opção
    print("[0] Sair")
    print("------------")
    
    op = input("Escolha: ").strip()

    if op == "1":
        nome = input("Item: ").strip()
        # Garante que o item não é uma string vazia antes de cadastrar
        if nome:
            cadastrar(itens, nome)
        else:
            print("O nome do item não pode ser vazio.")
            
    elif op == "2":
        listar(itens)
        
    elif op == "3": # Implementação da remoção
        if not itens:
            print("Lista vazia. Não há nada para remover.")
            continue
            
        listar(itens) # Exibe a lista para que o usuário saiba qual número remover
        num = input("Digite o número do item a remover: ").strip()
        remover(itens, num)
        
    elif op == "0":
        print("👋 Saindo do programa. Até mais!")
        break
        
    else:
        print("❌ Opção inválida. Escolha 1, 2, 3 ou 0.")