print("--- Sistema de Calculo para Folha de Pagamento ---\n")

valor_hora = float(input("\nDigite o valor da hora do funcionário:\n"))
qtd_horas = int(input("Digite a quantidade de horas trabalhadas no mês:\n"))
salario_bruto = valor_hora * qtd_horas

if salario_bruto <= 1903.98:
    ir = 0
    deducao = 0
elif salario_bruto <= 2826.65:
    ir = 0.075
    deducao = 142.80
elif salario_bruto <= 3751.05:
    ir = 0.15
    deducao = 354.80
elif salario_bruto <= 4664.68:
    ir = 0.225
    deducao = 636.13
else:
    ir = 0.275
    deducao = 869.36

desconto_ir = (salario_bruto * ir) - deducao

if desconto_ir < 0:
    desconto_ir = 0
    
desconto_ir = salario_bruto * ir
desconto_inss = salario_bruto * 0.1
valor_fgts = salario_bruto * 0.11
total_descontos = desconto_ir + desconto_inss
salario_liquido = salario_bruto - total_descontos


print("\n--- Resumo do Salário ---\n")
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto do IR: R$ {desconto_ir:.2f}")
print(f"Desconto do INSS: R$ {desconto_inss:.2f}")
print(f"Valor de depósito do FGTS: R$ {valor_fgts:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")

input("\nPressione Enter para sair...")