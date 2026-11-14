# operadores lógicos
# and - ambas as expressões devem retornar verdadeiras
# or - basta apenas uma das expressões retornar verdadeira
# not - inverte o resultado da expressão lógica





idade = int(input("Qual é sua idade: "))
ingresso = input("Você tem ingresso? s/n ")




# conjugar com operador and

if idade >= 18 and ingresso == "s":
    print("Seja bem vindo a festa  😎")
else : 
    print("Você não pode entrar na festa 😥")
    
    