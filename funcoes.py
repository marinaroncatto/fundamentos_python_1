## FUNÇÕES ##

#Podemos agora definir a primeira condição que pode ajudá-lo a decidir quando começar a escrever suas próprias funções: se um fragmento específico do código começar a aparecer em mais de um lugar, considere a possibilidade de isolá-lo na forma de uma função chamada de os pontos onde o código original foi colocado antes.

#Podemos agora declarar a segunda condição: se um código se tornar tão grande que a leitura e o subestimação podem causar um problema, divida-o em problemas menores e separados e implemente cada um deles na forma de uma função separada.

#Essa decomposição continua até que você obtenha um conjunto de funções curtas, fáceis de entender e testar.

#Isso nos leva diretamente à terceira condição: se você vai dividir o trabalho entre vários programadores, decomponha o problema para permitir que o produto seja implementado como um conjunto de funções escritas separadamente, reunidas em módulos diferentes.

#Você precisa defini-lo. A palavra define é significativa aqui.

#É assim que a definição mais simples de função se parece:

def function_name():
    function_body

#Começa sempre com a palavra-chave def (de define)
#Depois de def passa o nome da função (as regras para nomear funções são exatamente as mesmas que para nomear variáveis)
#depois do nome da função, há um lugar para um par de parênteses (eles não contêm nada aqui, mas isso vai mudar em breve)
#a linha deve ser terminada com dois pontos;
#a linha logo após def inicia o corpo da função - um par (pelo menos um) de instruções necessariamente aninhadas, que serão executadas sempre que a função for chamada; nota: a função termina onde o aninhamento termina, então você precisa ter cuidado.

#EX - sem função

print("Entre um valor: ")
a = int(input())

print("Entre um valor: ")
b = int(input())

print("Entre um valor: ")
c = int(input())

#ex - com função

def message():
    print("Entre um valor: ")
 
print("Começamos aqui.")
message()
print("terminamos aqui.")

#ex 3

def message():
    print("Entre um valor: ")
 
message()
a = int(input())
message()
b = int(input())
message()
c = int(input())
 
#Você pode definir uma função que não aceita argumentos, por exemplo:


def message(): # definindo uma função
    print("Olá") # o corpo da função
 
message() # chamando a função
 
#Você pode definir uma função que aceita argumentos, assim como a função de um parâmetro abaixo:


def hello(name): # definindo uma função
    print("Olá,", name) # o corpo da função
 
 
name = input("Entre um valor: ")
 
hello(name) # chamando a função
 
#Não se esqueça:

#parâmetros vivem em funções internas (este é o ambiente natural)
#argumentos existem fora das funções e são portadores de valores passados para os parâmetros correspondentes.

def message(number):
    print("Digite um número:", number)
 
message(1)
 
#dois parametros

def message(what, number):
    print("Entrar", what, "número", number)
 
message("telefone", 11)
message("preço", 5)
message("número", "número")
 
## parametros posicionais ##

def my_function(a, b, c):
    print(a, b, c)
 
my_function(1, 2, 3)
 
#ex

def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)
 
introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")
 
##  Passagem de parametro por palavra-chave ##

def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)
 
introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")
 
#Você pode combinar os dois estilos, se quiser - há apenas uma regra inquebrável: você precisa colocar argumentos posicionais antes dos argumentos das palavras-chave.

adding(3, c = 1, b = 2)
 
## funções parametrizadas ##

#Às vezes, os valores de um determinado parâmetro são usados com mais frequência do que outros. Esses argumentos podem ter seus valores padrão (predefinidos) levados em consideração quando seus argumentos correspondentes foram omitidos.


#Eles dizem que o sobrenome mais popular em inglês é Smith. Vamos tentar levar isso em conta.
#ex

def introduction(first_name, last_name="Smith"):
     print("Olá meu nome é", first_name, last_name)
 
introduction("James", "Doe")
 
introduction("Henry")
 
#não haverá erro, e as duas chamadas serão bem-sucedidas, enquanto o console mostrará a seguinte saída:

#Olá meu nome é Henry Smith
#Olá meu nome é William Smith

#Você pode ir além se for útil. Ambos os parâmetros têm seus valores padrão agora, veja o código abaixo:


def introduction(first_name="John", last_name="Smith"):
    print("Olá meu nome é", first_name, last_name)

#Isso torna a seguinte chamada absolutamente válida:


introduction()

#E essa é a saída esperada:

#Olá meu nome é John Smith


#Se você usar um argumento de palavra-chave, o restante terá o valor padrão:


introduction(last_name="Hopkins")
 
#A saída é:

#Olá meu nome é John Hopkins

#Um exemplo de função de três parâmetros:


def address(street, city, postal_code):
    print("Seu endereço é:", street, "St.,", city, postal_code)
 
s = input("Street: ")
p_c = input("Código postal: ")
c = input("Cidade: ")
address(s, c, p_c)

#Pergunta 4: Qual é a saída do trecho de código?


#def add_numbers(a, b=2, c):
   # print(a + b + c)
 
#add_numbers(a=1, c=3)
 
#SyntaxError - um argumento não padrão (c) Segue um argumento default (b=2).

### return ###

#Para que as funções retornem um valor (mas não apenas para essa finalidade), use a instrução return.

#Essa palavra oferece uma visão completa de seus recursos. Nota: é uma palavra-chave Python.

# A instrução return tem duas variantes diferentes - vamos considerá-las separadamente.

### return sem uma expressão#### 

def happy_new_year(wishes = True):
    print("Três...")
    print("Duas...")
    print("Uma...")
    if not wishes:
        return
 
    print("Feliz Ano Novo!")
 
#Quando invocado sem nenhum argumento:


happy_new_year()
 
#a função causa um pouco de ruído - a saída será semelhante a:

#Três...
#Duas...
#Uma...
#Feliz Ano Novo!

#Fornecendo False como um argumento:

happy_new_year(False)
 
#vai modificar o comportamento da função - a instrução return e fará com que seja encerrado logo antes dos desejos - esta é a saída atualizada:

#Três...
#Duas...
#Uma...

### return com uma expressão ###

#A segunda variante de return é estendida com uma expressão:


def function():
    return expression
 
#Há duas consequências de usá-lo:

#causa o término imediato da execução da função (nada de novo se comparado à primeira variante)
#além disso, a função avaliará o valor da expressão e o retornará (daí o nome mais uma vez) como o resultado da função.
#Sim, já sabemos - este exemplo não é muito sofisticado:


def boring_function():
    return 123
 
x = boring_function()
 
print("A aborrecimento_função retornou seu resultado. Isso é:", x)
 
#O fragmento escreve o seguinte texto no console:

#O retorno da função boring_function é 123

#O resultado pode ser usado livremente aqui, por exemplo, para ser atribuído a uma variável.

#Também pode ser completamente ignorado e perdido sem deixar vestígios.

#Observe que não estamos sendo muito educados aqui - a função retorna um valor e nós o ignoramos (não o usamos de forma alguma):


def boring_function():
    print("'Modo de tédio' ON.")
    return 123
 
print("Esta lição é interessante!")
boring_function()
print("Essa aula é chata...")

#O programa produz a seguinte saída:

#Esta lição é interessante!
#'Modo Tédio' ON.
#Essa aula é chata...
 
#Não se esqueça:

#você sempre pode ignorar o resultado da função e ficar satisfeito com o efeito da função (se a função tiver algum)
#se uma função se destina a retornar um resultado útil, ela deve conter a segunda variante da instrução de return.

### VALOR NONE ###

#Seus dados não representam nenhum valor razoável - na verdade, não é um valor; portanto, não deve participar de nenhuma expressão.

#Existem apenas dois tipos de circunstâncias em que None pode ser usada com segurança:

#quando você a atribui a uma variável (ou a retorna como resultado de uma função)
#quando você a compara com uma variável para diagnosticar seu estado interno.

#Exatamente como aqui:


value = None
if value is None:
    print("Desculpe, você não carrega nenhum valor")

#Não se esqueça disso: se uma função não retorna um determinado valor usando a cláusula return, pressupõe-se que ele retorne implicitamente None.

def strange_function(n):
 if(n % 2 == 0):
 return True


#É óbvio que a função strange_function retorna True quando seu argumento é par.

#O que ele retorna no outro caso?

#Podemos verificar o código a seguir:


print(strange_function(2))
print(strange_function(1))
 
#Isso é o que vemos no console:

#True
#None

#Não fique surpreso na próxima vez que não vir o None como resultado de uma função - pode ser o sintoma de um erro sutil dentro da função.

### Listas e Funções ###

#Listas podem ser enviadas como argumentos para funções, assim como serem geradas
#por elas.

#Então, se você passar uma lista para uma função, a função tem que lidar com isso como uma lista.

#ex de lista como argumento

def list_sum(lst):
    s = 0
 
    for elem in lst:
        s += elem
 
    return s
 
#e invocados da seguinte forma:


print(list_sum([5, 4, 3]))
 
#retornará 12 como resultado

#ex de lista como resultado da função

def strange_list_fun(n):
 strange_list = []
 
 for i in range(0, n):
 strange_list.insert(0, i)
 
 return strange_list

#A saída do programa será assim:

[#4, 3, 2, 1, 0]
print(strange_list_fun(5))

#### 4.3.9 RESUMO DA SEÇÃO ########

#1. Você pode usar a palavra-chave return para informar uma função para retornar algum valor. A declaração de return sai da função, por exemplo:


def multiply(a, b):
    return a * b
 
print(multiply(3, 4)) # saídas: 12
 
 
def multiply(a, b):
    return
 
print(multiply(3, 4)) # saídas: None
 
#2. O resultado de uma função pode ser facilmente atribuído a uma variável, por exemplo:


def wishes():
    return "Feliz aniversário!"
 
w = wishes()
 
print(w) # saídas: Feliz aniversário!
 
#Veja a diferença de saída nos dois exemplos a seguir:


# Exemplo 1
def wishes():
    print("Meus desejos")
    return "Feliz aniversário!"
 
wishes() # saídas: Meus desejos
 
 
# Exemplo 2
def wishes():
    print("Meus desejos")
    return "Feliz aniversário!"
 
print(wishes())
 
# saídas: Meus desejos
# Feliz aniversário!
 
#3. Você pode usar uma lista como argumento de função, por exemplo:


def hi_everybody(my_list):
    for name in my_list:
   "woda": "água",
        print("Oi,", name)
 
hi_everybody(["Adão", "John", "Lucy"])
 
#4. Uma lista também pode ser um resultado de função, por exemplo:


def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list
 
print(create_list(5))
 
