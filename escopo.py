### Funções e escopos: a palavra-chave global ####

#Há um método Python especial que pode estender o escopo de uma variável de uma forma que inclua o corpo da função (mesmo se você quiser não apenas ler os valores, mas também modificá-los).

#Tal efeito é causado por uma palavra-chave chamada global:


#global name
#global name1, name2, ...
 
#Usar essa palavra-chave dentro de uma função com o nome (ou nomes separados por vírgulas) de uma variável (ou variáveis), força o Python a não criar uma nova variável dentro da função - a que pode ser acessada de fora será usada.

#Em outras palavras, esse nome se torna global (tem escopo global e não importa se é o assunto de leitura ou atribuição).

#ex

def my_function():
 global var
 var = 2
 print("Eu conheço aquela variável?", var)


var = 1
my_function()
print(var)

#saída: Eu conheço aquela variável? 2
#2


#### Como a função interage com seus argumentos ####

#alterar o valor do parâmetro não se propaga fora da função (em qualquer caso, não quando a variável é escalar, como no exemplo).

#Isso também significa que uma função recebe o valor do argumento, não o próprio argumento. Isso se aplica a escalares.

def my_function(n):
 print("Eu obtive", n)
 n += 1
 print("Eu tenho", n)


var = 1
my_function(var)
print(var)

#saída
#Eu obtive 1
#Eu tenho 2
#1

#Vale a pena verificar como ele funciona com listas (você se lembra das particularidades de atribuir fatias de lista versus atribuir listas como um todo?).

#O exemplo a seguir esclarecerá a questão:


def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)
 
 
my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)
 
#A saída do código é:

#Print #1: [2, 3]
#Print #2: [2, 3]
#Print #3: [0, 1]
#Print #4: [2, 3]
#Print #5: [2, 3]

#Parece que a regra anterior ainda funciona.

#Por fim, você pode ver a diferença no exemplo abaixo:


def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0] # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)
 
 
my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)
 
#Não alteramos o valor do parâmetro my_list_1 (já sabemos que ele não afetará o argumento), mas sim modificar a lista identificada por ele.

#A saída pode ser surpreendente. Execute o código e verifique:

#Print #1: [2, 3]
#Print #2: [2, 3]
#Print #3: [3]
#Print #4: [3]
#Print #5: [3]

#se o argumento for uma lista, a alteração do valor do parâmetro correspondente não afeta a lista (lembre-se: as variáveis que contêm listas são armazenadas de forma diferente de escalares)
#mas se você alterar uma lista identificada pelo parâmetro (Nota: a lista, não o parâmetro!), a lista refletirá a alteração.


#### 4.4.4 RESUMO DA SEÇÃO ####

#1. Uma variável que existe fora de uma função tem escopo dentro do corpo da função (exemplo 1), a menos que a função defina uma variável com o mesmo nome (exemplo 2 e exemplo 3), por exemplo:

#Exemplo 1:


var = 2
 
 
def mult_by_var(x):
    return x * var
 
 
print(mult_by_var(7)) # saídas: 14
 
#Exemplo 2:


def mult(x):
    var = 5
    return x * var
 
 
print(mult(7)) # saídas: 35
 
#Exemplo 3:


def mult(x):
    var = 7
    return x * var
 
 
var = 3
print(mult(7)) # saídas: 49
 
#2. Uma variável que existe dentro de uma função tem escopo dentro do corpo da função (exemplo 4), por exemplo:

#Exemplo 4:


def adding(x):
    var = 7
    return x + var
 
 
print(adding(4)) # saídas: 11
print(var) # NameError
 
#3. Você pode usar a palavra-chave global seguida por um nome de variável para tornar o escopo da variável global, por exemplo:


var = 2
print(var) # saídas: 2
 
 
def return_var():
    global var
    var = 5
    return var
 
 
print(return_var()) # saídas: 5
print(var) # saídas: 5
