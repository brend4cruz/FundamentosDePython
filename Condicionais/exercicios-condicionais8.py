# 8) Faça um programa que receba o nome, cargo e salário de um funcionário. 
# Se o funcionário ganhar abaixo de 1000 reais, calcule o salário acrescido de 10%.
# Ao final exiba o nome, o cargo e o salário desse funcionário.


# Entrada

nome = input("Digite seu nome: ")
cargo = input("Digite seu cargo: ")
salario = float(input("Digite seu salário:  "))


# Processamento

if salario <= 1000 :
    salario = salario + salario * 1.10
    print(f"Nome: {nome}")
    print(f"Cargo: {cargo}")
    print(f"Novo Salário:{salario}")
    
    
    
    
else:
    print("Salário sem direito a reajuste")
    
    

 #Saída
    
    print(f"Nome: {nome}")
    print(f"Cargo: {cargo}")
    print(f"Novo Salário: R${salario:.2f}")
    

    
    
    
    
    
    # print(nome,cargo,salario)