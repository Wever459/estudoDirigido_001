senha_correta = "python123"
tentativa=""
tentativas_maximas=3
tentativas_realizadas=0

while tentativa != senha_correta and tentativas_realizadas<tentativas_maximas:
    tentativa = input("Digite a senha: ")
    tentativas_realizadas+=1

    if tentativa != senha_correta and tentativas_realizadas < tentativas_maximas:
        tentativas_restantes = tentativas_maximas - tentativas_realizadas
        print(f"Senha incorreta! Você tem {tentativas_restantes} tentativa(s) restante(s).")

if tentativa == senha_correta:
    print("Acesso liberado!")

else:
    print("Acesso bloqueado! Número máximo de tentativas excedido.")
    