# Receba ano de nascimento e ano atual. Calcule idade e semanas.


# Entrada
# Recebe o ano de nascimento
# Receba o ano atual


anoNascimento = int(input("Digite o ano de seu nascimento: "))
anoAtual = int(input("Digite o ano atual: "))



# Processamento
idade =  anoAtual - anoNascimento 
idadeSemanas = idade * 12 * 4


# Saída 

print()
print(f"Sua idade  é: {idade}")

print(f"Sua idade em semanas é: {idadeSemanas}")
print()
