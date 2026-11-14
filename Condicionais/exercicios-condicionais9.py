# 9) Uma empresa decide dar aumento de 30% aos funcionários cujo salário é inferior a

# 500 reais. Escreva um programa que receba o salário de um funcionário e imprima o

# valor do salário reajustado ou uma mensagem caso o funcionário não tenha direito a aumento.



print()
print()
print("|*************************|")
print("|    Programa Reajuste    |")
print("|        Versão 2.0       |")
print("|*************************|")
print()
print()


# Entrada

salario = float(input("Digite o salário:  "))


#  Processamento

if salario < 500: 
    salario = salario + salario * 1.30  # 30% de aumento
    print(f"Seu  salário foi ajustado para R$:  {salario:.2f}")
    
else: # salário sem reajuste
    print("Salário sem direito a reajuste")