def saudacao(nome):
    return f"Olá, {nome}!"

usuario = input("Digite seu nome: ")

print(saudacao(usuario))

idade=int(input("Digite sua idade: "))

sobra=(100-idade)

print(f"Faltam {sobra} anos para chegar aos 100")