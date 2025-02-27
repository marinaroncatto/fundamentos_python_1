### listas ###

#Vamos criar uma variável chamada numbers; ela é atribuída com não apenas um número, mas é preenchida com uma lista composta por cinco valores (nota: a lista começa com um colchete aberto e termina com um colchete fechado; o espaço entre os colchetes é preenchido com cinco números separados por vírgulas).

#Os elementos em uma lista podem ter tipos diferentes. Alguns deles podem ser números inteiros, outros carros alegóricos e outros ainda podem ser listas.

#Python adotou uma convenção afirmando que os elementos em uma lista são sempre numerados começando do zero. Isso significa que o item armazenado no início da lista terá o número zero.

#Antes de prosseguirmos na discussão, precisamos declarar o seguinte: nossa lista é uma coleção de elementos, mas cada elemento é um escalar.

## indexando listas##

numbers = [10, 5, 7, 2, 1]
print("Conteúdos originais da lista:", numbers)  # Imprimindo o conteúdo original da lista.
 
numbers[0] = 111
print("Novo conteúdo da lista: ", numbers)  # Conteúdo atual da lista.
 
#E agora queremos que o valor do quinto elemento seja copiado para o segundo elemento - você consegue adivinhar como fazer isso?

numbers = [10, 5, 7, 2, 1]
print("Conteúdos originais da lista:", numbers)  # Imprimindo o conteúdo original da lista.
 
numbers[0] = 111
print("\nConteúdo da lista anterior:", numbers)  # Imprimindo conteúdos de listas anteriores.
 
numbers[1] = numbers[4]  # Copiando o valor do quinto elemento para o segundo.
print("Novo conteúdo da lista:", numbers)  # Printing Conteúdo atual da lista.
 
### acesso ao conteúdo da lista ###

numbers = [10, 5, 7, 2, 1]
print("Conteúdo da lista original:", numbers) # Imprimindo o conteúdo da lista original.


numbers[0] = 111

print ("\nConteúdo da lista anterior:", numbers) # Imprimindo conteúdo da lista anterior.


numbers[1] = numbers [4] # Copiando o valor do quinto elemento para o segundo.
print("Conteúdo da lista anterior:", numbers) # Imprimir o conteúdo da lista anterior.


print ("\n List length:", len (numbers)) # Imprimindo o comprimento da lista.

# Se quiser verificar o comprimento atual da lista, você pode usar uma função chamada len() (o nome vem do comprimento).

#A função usa o nome da lista como argumento e retorna o número de elementos armazenados atualmente na lista (em outras palavras, o comprimento da lista).

## remover elementos de uma lista ##

#Qualquer um dos elementos da lista pode ser removido a qualquer momento - isso é feito com uma instrução chamada del (delete). Nota: é uma instrução, não uma função.

numbers = [10, 5, 7, 2, 1]
print("Conteúdo da lista original:", numbers) # Imprimindo conteúdo da lista de originais.

numbers[0] = 111
print("\nConteúdo da lista anterior:", numbers) # Imprimindo conteúdo da lista anterior.

numbers[1] = numbers[4] # Copiando o valor do quinto elemento para o segundo.
print("Conteúdo da lista anterior:", numbers) # Imprimindo conteúdo da lista anterior.

print ("\nComprimento da lista:", len (numbers)) # Imprimindo comprimento de lista anterior.

###

del numbers[1] # Removendo o segundo elemento da lista.
print ("Comprimento da nova lista:", len (numbers)) # Imprimindo novo comprimento da lista.
print ("\nNova lista de conteúdo:", numbers) # Imprimindo conteúdo da lista atual.

### 


#### indices negativos###

#Pode parecer estranho, mas os índices negativos são legais e podem ser muito úteis.

#Um elemento com um índice igual a -1 é o último na lista.
#serve para acessar a lista de trás pra frente

numbers = [111, 7, 2, 1]
print(numbers[-1]) #imprie o último

numbers = [111, 7, 2, 1]
print(numbers[-2]) #imprime o penúltimo


#LAB LISTAS

hat_list = [1, 2, 3, 4, 5] # Esta é uma lista atual de números ocultos no hat.

 # Etapa 1: escreva uma linha de código que solicita ao usuário
# que substitua o número do meio por um número inteiro inserido pelo usuário. 

hat_list[2] = int(input("Digite um número inteiro "))

# Etapa 2: escreva uma linha de código que remova o último elemento da lista.
del hat_list[4]
 # Etapa 3: escreva uma linha de código que imprima o comprimento da lista atual
print("Comprimento da lista: ",len (hat_list) )
print (hat_list) 


## funções x métodos

#Um método pertence aos dados para os quais trabalha, enquanto uma função pertence ao código inteiro.

#Em geral, uma chamada de função típica pode ser assim:

#result = function(arg)

#A função usa um argumento, faz alguma coisa e retorna um resultado.

#Uma invocação típica de método geralmente se parece com isso:

#result = data.method(arg)

#Nota: o nome do método é precedido pelo nome dos dados proprietários do método. Em seguida, adicione um ponto, seguido pelo nome do método, e um par de parênteses que encerra os argumentos.

#O método se comportará como uma função, mas pode fazer algo mais - ele pode alterar o estado interno dos dados dos quais foram chamados.

#### Adicionando elementos a uma lista: append() e insert() ###

#Um novo elemento pode ser colado ao final da lista atual:

#list.append(value)
 
#Essa operação é realizada por um método chamado append(). Ele pega o valor do argumento e o coloca no final da lista que possui o método.

#O comprimento da lista aumenta em um.

#O método insert() é um pouco mais inteligente - ele pode adicionar um novo elemento em qualquer lugar na lista, não apenas no final.

#list.insert(location, value)
 
#São necessários dois argumentos:

#o primeiro mostra a localização necessária do elemento a ser inserido; Nota: todos os elementos existentes que ocupam locais à direita do novo elemento (inclusive o na posição indicada) são deslocados para a direita, a fim de liberar espaço para o novo elemento;
#o segundo é o elemento a ser inserido.


#ex

numbers = [111, 7, 2, 1]

print(len(numbers))

print(numbers)


 ###


numbers.append (4)


print(len(numbers))

print(numbers)

###

numbers.insert (0, 222)

print(len (numbers))
print(numbers)


 #
#Você pode começar a vida de uma lista deixando-a vazia (isso é feito com um par de colchetes vazios) e, em seguida, adicionando novos elementos, conforme necessário.
#ex1:
my_list = [] # Criando uma lista vazia.

for i in range(5):
   my_list.append (i + 1)

print (my_list)


#ex2

my_list = []  # Criando uma lista vazia.
 
for i in range(5):
    my_list.insert(0, i + 1)
 
print(my_list)

#Você deve obter a mesma sequência, mas em ordem inversa (este é o mérito de usar o método insert()).

## Utilização de listas ##

#O loop for tem uma variante especial que pode processar listas de forma muito eficaz - vamos dar uma olhada nisso.

my_list = [10, 1, 8, 3, 5]

total = 0

for i in range(len(my_list)):

  total += my_list[i]

print(total)


#Mas o loop for pode fazer muito mais. Ele pode ocultar todas as ações conectadas à indexação da lista e disponibilizar todos os elementos da lista de maneira prática.

my_list = [10, 1, 8, 3, 5]
total = 0
 
for i in my_list:
    total += i
 
print(total)


# Pergunta: como você pode trocar os valores de duas variáveis?

#É assim que você pode fazer:


variable_1 = 1
variable_2 = 2
 
auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary

#O Python oferece uma maneira mais conveniente de fazer a troca - dê uma olhada:

variable_1 = 1
variable_2 = 2
 
variable_1, variable_2 = variable_2, variable_1

#Agora você pode facilmente trocar os elementos da lista para reverter a ordem:


my_list = [10, 1, 8, 3, 5]
 
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
 
print(my_list)

#Você pode usar o loop for para fazer a mesma coisa automaticamente, independentemente do comprimento da lista? Sim, você pode.

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
print(my_list)

#atribuímos a variável length com o comprimento da lista atual (isso torna nosso código um pouco mais claro e mais curto)
#lançamos o loop for para percorrer length//2 vezes (isso funciona bem para listas com comprimentos pares e ímpares, porque quando a lista contém um número ímpar de elementos, o meio permanece intocado)
#trocamos o i-ésimo elemento (do início da lista) pelo elemento com um índice igual a (length - i - 1) (do fim da lista); no nosso exemplo, para i igual a 0 o (length - i - 1) dá 4; para i igual a 1, dá 3 - isso é exatamente o que precisávamos.

#### Ordenando uma lista #########

#Resolvemos esse problema da seguinte maneira: introduzimos outra variável ; sua tarefa é observar se alguma troca foi feita durante a passagem ou não; se não houver troca, a lista já está classificada e nada mais precisa ser feito. Criamos uma variável chamada swapped e atribuímos um valor de False a ela para indicar que não há swaps. Caso contrário, ele será atribuído como True.

my_list = [8, 10, 6, 2, 4]  # Lista para ordenar
 
for i in range(len(my_list) - 1):  # precisamos de (5 - 1) comparações
    if my_list[i] > my_list[i + 1]:  # comparar elementos adjacentes
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Se acabarmos aqui, nós temos que trocar os elementos.


#ex


my_list = [8, 10, 6, 2, 4]  # Lista para ordenar
swapped = True  # É um pouco falso, precisamos dele para entrar no loop while.
 
while swapped:
    swapped = False  # nenhuma troca até agora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # uma troca ocorreu!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
print(my_list)


### A ordenação por bolhas - versão interativa###

my_list = []
swapped = True
num = int(input("Quantos elementos você deseja embaralhar? "))

for i in range(num):
 val = float(input("Entre com a lista de elementos:"))
 my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)


### método sort() ###

Como você pode ver, todas as listas têm um método chamado sort(), que as classifica o mais rápido possível.

my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

## método revers()

#Há também um método de lista chamado revers(), que você pode usar para reverter a lista, por exemplo:


lst = [5, 3, 1, 2, 4]
print(lst)
 
lst.reverse()
print(lst)  # outputs: [4, 2, 1, 3, 5]

##  A vida interior das listas ##

list_1 = [1]
list_2 = list_1
list_1 [0] = 2
print(list_2)


#A parte surpreendente é o fato de que o programa produzirá: [2], não [1], que parece ser a solução óbvia.

#As listas (e muitas outras entidades Python complexas) são armazenadas de maneiras diferentes das variáveis comuns (escalares).

#Você poderia dizer que:

#o nome de uma variável comum é o nome de seu conteúdo;
#o nome de uma lista é o nome de um local de memória onde a lista é armazenada.

## fatiamento ##

#Uma fatia é um elemento da sintaxe do Python que permite fazer uma cópia totalmente nova de uma lista ou de partes de uma lista.

#Na verdade, ele copia o conteúdo da lista, não o nome da lista.

list_1 = [1]
list_2 = list_1[:] #cria uma cópia
list_1[0] = 2
print(list_2)

#Uma das formas mais gerais da fatia é a seguinte:

#my_list[start:end] 

#ex

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list) # resultado [8, 6]

# Copiar a lista inteira.
list_1 = [1]
list_2 = list_1 [:]
list_1 [0] = 2
print (list_2)

# Copiando parte da lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list [1: 3]
print(new_list)

#  índices negativos #

#start é o índice do primeiro elemento incluído na fatia;
#end é o índice do primeiro elemento não incluído na fatia.

#É assim que os índices negativos trabalham com o particionamento:


my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list) # [8,6, 4]

#Se você omitir o start na fatia, presume-se que você deseja obter uma fatia começando no elemento com índice 0.

#my_list[:end] OU my_list[0:end]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list) #[10, 8, 6]

#Da mesma forma, se você omitir o end da fatia, pressupõe-se que você deseja que a fatia termine no elemento com o índice len(my_list).

#my_list[start:] OU my_list[start:len(my_list)]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list) #[4, 2]

## Mais sobre a instrução del##

#A instrução del descrita anteriormente é capaz de excluir mais do que apenas os elementos de uma lista de uma só vez - ela também pode excluir fatias:

my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list) #[10, 4, 2]

#Também é possível excluir todos os elementos de uma só vez:


my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list) # []

#A remoção da fatia do código muda bastante de significado.

#Dê uma olhada:


my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list) #erro
 
#A instrução del excluirá a lista em si, não seu conteúdo.


### operadores in e not in ###

#O Python oferece dois operadores muito eficientes, capazes de examinar a lista para verificar se um valor específico é armazenado ou não na lista.

#Esses operadores são:


#elem in my_list
#elem not in my_list

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)


## alguns usos ##

#O primeiro deles tenta encontrar o maior valor na lista.

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

#forma 2

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list:
    if i > largest:
        largest = i
 
print(largest)

#forma 3

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list[1:]:
    if i > largest:
        largest = i
 
print(largest)


 #Agora vamos encontrar a localização de um determinado elemento dentro de uma lista:

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False
 
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
 
if found:
    print("Elemento encontrado no índice", i)
else:
    print("ausente")

#Vamos supor que você tenha escolhido os seguintes números na loteria: 3, 7, 11, 42, 34, 49.

#Os números que foram desenhados são: 5, 11, 9, 42, 3, 49.

#A pergunta é: quantos números você acertou?

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
v
 
for number in bets:
    if number in drawn:
        hits += 1
 
print(hits)
 
    

