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
