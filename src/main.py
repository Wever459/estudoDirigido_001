# main.py

from funcoes import exibir_menu, cadastrar, listar

def main():
    itens=[]
    print("===App de itens(BFD2.0)===")

    while True:
        exibir_menu()
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            cadastrar(itens)

        elif opcao == "2":
            listar(itens)

        elif opcao == "0":

            print("Até mais!")

            break

        else:

            print("Opção inválida.")

if __name__=="__main__":

    main()