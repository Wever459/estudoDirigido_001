idade=int(input("Qual a sua idade?: "))

if idade>=60:
    print("Você é idoso.")

elif idade>=18:
    print("Você é adulto.")

else :

    print("Você é menor de idade.")

cidade=(input("De qual cidade você é?: "))
print(f"Você tem {idade} anos e veio de {cidade}.")