compras = []
while True:

    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    produto = input("Digite o nome do produto comprado: ")
    
   
    compras.append({"Nome": nome, "CPF": cpf, "Produto": produto})
    
 
    continuar = input("Deseja adicionar outra compra? (s/n) ")
    
   
    if continuar.lower() == "n":
        break


print("\nLista de compras registradas:")
for compra in compras:
    print("Nome: " + compra["Nome"] + " | CPF: " + compra["CPF"] + " | Produto: " + compra["Produto"])
