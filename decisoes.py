### operadores ###

# igualdade

var = 0 # Atribuindo 0 a var
print(var == 0)

var = 1 # Atribuindo 1 a var
print(var == 0)

#desigualdade

var = 0  # Atribuindo 0 a var
print(var != 0)
 
var = 1  # Atribuindo 1 a var
print(var != 0)


# maior que

black_sheep = 1

white_sheep = 2

black_sheep > white_sheep  # Maior que
 
# maior igual

centigrade_outside = 10.

centigrade_outside >= 0.0  # Maior ou igual a
 
#LAB
#Usando um dos operadores de comparação em Python, escreva um programa simples de duas linhas que aceita o parâmetro n como entrada, que é um inteiro, e imprime False se n for menor 100, e True se n for maior ou igual a 100.

n = 55
print(n>=100)
n = 100
print(n>=100)
n = 123
print(n>=100)

### condicionais ###

#if

#if sheep_counter >= 120:
#    make_a_bed()
#    take_a_shower()
#    sleep_and_dream()
#feed_the_sheepdogs()

#if-else

#if true_or_false_condition:
#    perform_if_condition_true
#else:
#    perform_if_condition_false

#if-else aninhados

#if the_weather_is_good:
#   if nice_restaurant_is_found:
#        have_lunch()
#    else:
#        eat_a_sandwich()
#else:
#    if tickets_are_available:
#        go_to_the_theater()
#    else:
#        go_shopping()

#elif (similar ao else if)

#if the_weather_is_good:
#    go_for_a_walk()
#elif tickets_are_available:
#    go_to_the_theater()
#elif table_is_available:
#    go_for_lunch()
#else:
#    play_chess_at_home()
 
#########################
#você não deve usar else sem preceder if;
#else é sempre o último ramo da cascata, independentemente de você ter usado elif ou não;
#else é uma parte opcional da cascata e pode ser omitida;
#se houver uma else na cascata, apenas uma de todas as ramificações será executada;
#se não houver a ramificação else, é possível que nenhuma das outras ramificações sejam executadas;

#############################


#ex:

#Ler dois números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
 
# Escolha o número maior
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
 
# Imprimir o resultado
print("O maior número é:", larger_number)
 

#ex 2

#Ler dois números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
 
# Escolha o número maior
if number1 > number2: larger_number = number1
else: larger_number = number2
 
# Imprimir o resultado
print("O maior número é:", larger_number)
 
#ex3

number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))

largest_number = number1

if number2 > largest_number:
    largest_number = number2
if number3 > largest_number:
    largest_number = number3
print("O maior número é: ",largest_number)
 

# funçao max()

# Leia três números.
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))
 
# Verifique qual dos números é o maior
# e passe-o para a variável de número_maior.
 
largest_number = max(number1, number2, number3)
 
# Imprimir o resultado.
print("O maior número é:", largest_number)

#Da mesma forma, você pode usar a função min() para retornar o número mais baixo.

#lab2
plant = input("Qual a melhor planta? ")

if plant == 'Spathiphyllum':
    print("Sim - Spathiphyllum é a melhor planta de todos os tempos!")
elif plant == 'spathiphyllum':
    print("Não, eu quero um grande Spathiphyllum!")
else:
    print('Spathiphyllum! não',plant+'!')



#lab3

#Era uma vez uma terra - uma terra de leite e mel, habitada por pessoas felizes e prósperas. As pessoas pagavam impostos, é claro - a felicidade tinha limites. O imposto mais importante, chamado de imposto de renda pessoal (PIT) tinha que ser pago uma vez por ano e foi avaliado usando a seguinte regra:

#se a renda do cidadão não era superior a 85.528 talões, o imposto era igual a 18% da renda, menos 556 taller e 2 centavos (isso era o que eles chamavam de isenção de imposto)
#se a receita fosse superior a esse valor, o imposto seria igual a 14.839 talões e 2 centavos, mais 32% do excedente em mais de 85.528 taller.

#Nota: esse país feliz nunca devolveu dinheiro para seus cidadãos. Se o imposto calculado for menor que zero, isso significaria apenas nenhum imposto (o imposto foi igual a zero). Leve isso em consideração durante os cálculos.    

income = float(input("Entre com os rendimentos anuais "))

if income < 85528:
 tax = income * 0.18 - 556.02
# Escreve o resto do código aqui.
else:
    tax = (income - 85528) * 0.32 + 14839.02  

if tax < 0.0:
    tax = 0.0
    
tax = round(tax, 0)
print("A taxa é:", tax, "thalers")

#lab3
#faça um sistema que calcule se o ano é bissexto

#Desde a introdução do calendário gregoriano (em 1582), a regra a seguir é usada para determinar o tipo de ano:

#se o número do ano não é divisível por quatro, é um ano comum;
#caso contrário, se o número do ano não for divisível por 100, será um ano bissexto;
#caso contrário, se o número do ano não for divisível por 400, é um ano comum ;
#caso contrário, é um ano bissexto .


year = int(input("Digite um ano: "))

if year < 1582:
  print("Não dentro do período do calendário gregoriano")
else:
  if year % 4 != 0:
      print("ano comum")
  elif year % 100 != 0:
      print("ano bissexto")
  elif year % 400 !=0:
      print("ano comum")
  else: 
      print("ano bissexto")
