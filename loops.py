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

# range com 2 argumentos

#A invocação da função range() pode ser equipada com dois argumentos, não apenas um:


for i in range(2, 8):
    print("O valor de i é atualmente", i)

#Nesse caso, o primeiro argumento determina o (primeiro) valor inicial da variável de controle.


#O último argumento mostra o primeiro valor em que a variável de controle não será atribuída.

#Nota: a função range() aceita apenas números inteiros como argumentos e gera sequências de números inteiros.

#O primeiro valor mostrado é 2 (extraído do primeiro argumento do range().)

#O último é 7 (embora o segundo argumento do range() seja 8).

################
    
#A função range() também pode aceitar três argumentos - dê uma olhada no código no editor.

for i in range(2, 8, 3):
  print("O valor de i é atualmente", i)

#O terceiro argumento é um incremento - é um valor adicionado para controlar a variável a cada volta do loop (como você pode suspeitar, o valor padrão do incremento é 1).

#O primeiro argumento passado para a função range() nos diz qual é o número inicial da sequência (portanto, 2 na saída). O segundo argumento diz à função onde parar a sequência (a função gera números até o número indicado pelo segundo argumento, mas não o inclui). Por fim, o terceiro argumento indica a etapa, que realmente significa a diferença entre cada número na sequência de números gerada pela função.

#ex2

  power = 1
for expo in range(16):
  print("2 à potência de", expo, "é", power)
  power *= 2


#LAB contagem mississipi

  import time

# Escreva um loop for que conte até cinco
for i in range(1, 6):
   # Corpo do loop - exiba o número de iteração do loop e a palavra "Mississippi".
   print(i,"Mississippi")
   # Corpo do loop - use: time.sleep(1)
   time.sleep(1)
# Escreva uma função print com a mensagem final.
print("Pronto ou não, aqui vou eu!")

#break e continue

#break - sai do loop imediatamente e termina incondicionalmente a operação do loop; o programa começa a executar a instrução mais próxima após o corpo do loop;
#continue - se comporta como se o programa tivesse chegado ao fim do corpo; o próximo turno é iniciado e a expressão de condição é testada imediatamente.

# break - exemplo

print("The break instrução:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro do laço.", i)
print("Fora do loop.")


# continue - exemplo

print("The continue instrução:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro do laço.", i)
print("Fora do loop.")

#ex2 break:

maior_numero = -99999999
counter = 0

while True:
    number = int(input("Digite um número ou digite -1 para terminar o programa: "))
    if number == -1:
        break
    counter += 1
    if number > maior_numero:
        maior_numero = number

if counter != 0:
    print("TO maior número é", maior_numero)
else:
    print("Você não inseriu nenhum número.")    

#ex2 continue

largest_number = -99999999
counter = 0

number = int(input("Insira um número ou digite -1 para finalizar o programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Insira um número ou digite -1 para finalizar o programa: "))

if counter:
    print("O maior número é",  largest_number)
else:
    print("Você não tem inseriu qualquer número.")    

#LAB BREAK

#Projete um programa que use um loop while e solicite continuamente que o usuário insira uma palavra, a menos que o usuário insira "chupacabra" como a palavra de saída secreta, caso em que a mensagem "Você saiu do loop com sucesso". Deve ser impresso na tela, e o loop deve terminar.

secret_word = "chupacabra"

while True:
    word = input("Qual a palabra secreta? ")
    if word == secret_word:
        break
print("Você saiu do loop com sucesso")     


#LAB CONTINUE COMEDOR DE VOGAIS

# Solicita que o usuário insira uma palavra
# e atribua-a à variável user_word.
user_word = input("Digite uma palavra: ")
user_word = user_word.upper()

for letter in user_word:
    # Preenchao corpo do loop for.
    if letter == "A":
        continue
    elif letter == 'E':
        continue
    elif letter =="I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)
    
#versão2
word_without_vowels = ""

# Solicitar ao usuário que digite uma palavra
# e atribua-o à variável user_word.
user_word = input("Digite uma palavra: ")
user_word = user_word.upper()

for letter in user_word:
    # Completa o corpo do loop.
    if letter == "A":
        continue
    elif letter == 'E':
        continue
    elif letter =="I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter

# Imprima a palavra atribuída a word_without_vowels.
print(word_without_vowels)        

#loop while e o else

#O ramo else do loop sempre é executada uma vez, independentemente de o loop ter entrado em seu corpo ou não.
#ex

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

#ex2 else sempre executa

i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)


# for e o else

#nele o else sempre imprime a última volta
#ex

for i in range(5):
 print(i)
else:
 print("else:", i)

#ex2

i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)

