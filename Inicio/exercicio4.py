# 4. Receba nome, peso e altura. Calcule IMC.

# Entrada

nome = (input("Digite seu nome: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura:"))


# Processamento
imc = peso / (altura * altura)


# Saída
print()
print(f"Seu IMC é: {imc:.2f}")