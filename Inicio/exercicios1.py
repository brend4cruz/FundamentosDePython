# . Receba a idade em anos e imprima em meses, dias, horas e minutos.



# Entrada
idade = int(input("Digite a idade:"))

# Processamento

idadeEmMeses = idade * 12
idadeEmDias = idade * 365
idadeEmHoras = idadeEmDias * 24
idadeEmMinutos = idadeEmHoras * 60

# Saída
print()
print(f"sua idade em meses é: {idadeEmMeses} meses")
print()
print(f"Sua idade em dias é: {idadeEmDias} dias")
print()
print(f"Sua idade em horas é: {idadeEmHoras} horas")
print()
print(f"Sua idade em minutos é: {idadeEmMinutos} minutos")