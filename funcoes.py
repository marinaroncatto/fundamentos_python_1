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
 
 
