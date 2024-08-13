#Gerenciamento de Estoque

import os

produtos = []

def limpar_tela():
    os.system('cls')


def pausa():
    print("\n\n")
    os.system('pause')

    
def mostrar_menu():
    limpar_tela
    print("\n\n\t-- Gerenciamento de Estoque --\n")
    print("Menu de Opções:\n")
    print("1- Cadastrar Produto")
    print("2- Atualizar Quantidade de Produto")
    print("3- Exibir Estoque")
    print("4- Calculo do Valor de Estoque")
    print("5- Sair do Programa")

    
def cadastrar_produto(produtos):
    print("\n\n\t-- Cadastrar Produto --\n")
    nome_produto = input("Digite o nome do produto: ")
    qtd_produto = int(input("Digite a quantidade do produto: "))
    valor_produto = float(input("Digite o valor do produto: "))
    produtos.append({"nome": nome_produto, "quantidade": qtd_produto, "valor": valor_produto})
    print("Produto cadastrado com sucesso!")
    pausa()
    
        
def atualizar_produto(produtos):
    print("\n\n\t-- Atualizar Produtos --\n")
    nome_produto = input("Digite o nome do produto que deseja atualizar: ")
    for produto in produtos:
        if produto["nome"] == nome_produto:
            nova_qtd = int(input(f"Digite a nova quantidade para {nome_produto}: "))
            produto["quantidade"] = nova_qtd
            print("Quantidade atualizada com sucesso!")
            pausa()
            return
    print("Produto não encontrado.")
    pausa()
    

def exibir_estoque(produtos):            
    print("\n\n\t-- Estoque Atual --\n")
    for produto in produtos:
        print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Valor: {produto['valor']}")
    pausa()
        
        
def calcular_total(produtos):
    print("\n\n\t-- Valor Total de Estoque --\n")
    total = 0
    for produto in produtos:
        total += produto['quantidade'] * produto['valor']
        print(f"O valor total do estoque é: {total:.2F}")
    pausa()
        
while True:
        mostrar_menu()
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            cadastrar_produto(produtos)
        elif opcao == 2:
            atualizar_produto(produtos)
        elif opcao == 3:
            exibir_estoque(produtos)
        elif opcao == 4:
            calcular_total(produtos)
        elif opcao == 5:
            print("Saindo do programa...")
            limpar_tela()
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")    
    
            
    
       
    



