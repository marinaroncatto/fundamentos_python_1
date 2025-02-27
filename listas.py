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


