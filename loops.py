#### while #####

#while conditional_expression:
#    instruction_one
#    instruction_two
#    instruction_three
#    :
#    :
#    instruction_n

#ex

# Armazene o maior número atual aqui.
largest_number = -999999999
 
# Insira o primeiro valor.
number = int(input("Digite um número ou digite -1 para parar: "))
 
# Se o número não for igual a -1, continue.
while number != -1:
    # O número é maior que o maior_número?
    if number > largest_number:
        # Sim, atualize o maior_número.
        largest_number = number
    # Insira o próximo número.
    number = int(input("Digite um número ou digite -1 para parar: "))
 
# Imprima o maior número.
print("O maior número é:", largest_number)


#ex2

# Um programa que lê uma sequência de números
# e conta quantos números são pares e quantos são ímpares.
# O programa termina quando zero é digitado.
 
odd_numbers = 0
even_numbers = 0
 
# Leia o primeiro número.
number = int(input("Digite um número ou digite 0 para parar: "))
 
# 0 termina a execução.
while number != 0:
    # Verifique se o número é ímpar.
    if number % 2 == 1:
        # Aumente o contador odd_numbers.
        odd_numbers += 1
    else:
        # Aumente o contador even_numbers.
        even_numbers += 1
    # Leia o número seguinte.
    number = int(input("Digite um número ou digite 0 para parar: "))
 
# Imprimir resultados.
print("Números ímpares contam:", odd_numbers)
print("Números pares contam:", even_numbers)

#x3 Usando uma variável counter para sair do loop

counter = 5
while counter != 0:
    print("Dentro do laço.", counter)
    counter -= 1
print("Fora do circuito.", counter)

#LAB

#solicitará que o usuário insira um número inteiro;
#vai usar um while loop;
#verificará se o número inserido pelo usuário é igual ao número escolhido pelo mágico. Se o número escolhido pelo usuário for diferente do número secreto do mago, o usuário deverá ver a mensagem "Ha ha! Você está preso no meu loop!" E será solicitado a inserir um número novamente. Se o número inserido pelo usuário corresponder ao número escolhido pelo mago, ele deverá ser impresso na tela, e o mago deve dizer as seguintes palavras: "Muito bem, trouxa! Você está livre agora."

#########
#A propósito, observe a função print(). A maneira como usamos aqui é chamada de impressão de várias linhas. Você pode usar aspas triplas para imprimir sequências de caracteres em várias linhas para facilitar a leitura ou criar um design especial baseado em texto.
#########

secret_number = 777

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")

number = int(input("adivinhe o número secreto "))

while number != secret_number:
    print("Ha ha! Você está preso no meu loop!")    
    number = int(input("adivinhe o número secreto "))
print("Muito bem, trouxa! Você está livre agora.")

#### for ###

#for i in range(100):
#    # do_something()
#    pass

# observe a palavra-chave pass dentro do corpo do loop - ela não faz nada; é uma instrução vazia - nós a colocamos aqui porque a sintaxe do loop for exige pelo menos uma instrução dentro do corpo (a propósito - if, elif, else e while expressamos a mesma coisa)


#ex

for i in range(10):
   print("O valor de i é atualmente", i)



