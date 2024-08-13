import os

# Função para limpar a tela de acordo com o sistema operacional
def limpar_tela():
    os.system('cls')

def pausa():
    print("\n\n")
    os.system('pause')

# Função para mostrar o menu de opções
def mostra_menu():
    limpar_tela()
    print("\n\n\tSistema Finanças\n")
    print("Menu de Opções:\n")
    print("1 - Cadastrar Receita")
    print("2 - Cadastrar Despesa")
    print("3 - Listar Saldo")
    print("4 - Listar Extrato")
    print("5 - Sair\n")

# Função para adicionar receita
def add_receita(receitas):
    descricao = input("Digite a descrição da receita: ")
    valor = float(input("Digite o valor da receita: "))
    receitas.append({"descricao": descricao, "valor": valor})
    print("Receita cadastrada com sucesso!")
    pausa()

# Função para adicionar despesa
def add_despesa(despesas):
    descricao = input("Digite a descrição da despesa: ")
    valor = float(input("Digite o valor da despesa: "))
    despesas.append({"descricao": descricao, "valor": valor})
    print("Despesa cadastrada com sucesso!")
    pausa()

# Função para listar o saldo
def listar_saldo(receitas, despesas):
    total_receitas = sum([receita["valor"] for receita in receitas])
    total_despesas = sum([despesa["valor"] for despesa in despesas])
    saldo = total_receitas - total_despesas
    print(f"O saldo atual é: {saldo:.2f}")
    pausa()

# Função para listar o extrato
def listar_extrato(receitas, despesas):
    print("Extrato:")
    print("Receitas:")
    for receita in receitas:
        print(f"- {receita['descricao']}: {receita['valor']:.2f}")
    
    print("Despesas:")
    for despesa in despesas:
        print(f"- {despesa['descricao']}: {despesa['valor']:.2f}")
    pausa()

# Função principal
def main():
    receitas = []
    despesas = []
    
    while True:
        mostra_menu()
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            add_receita(receitas)
        elif opcao == 2:
            add_despesa(despesas)
        elif opcao == 3:
            listar_saldo(receitas, despesas)
        elif opcao == 4:
            listar_extrato(receitas, despesas)
        elif opcao == 5:
            print("Saindo do programa...")
            limpar_tela()
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

# Executar o programa principal
if __name__ == "__main__":
    main()