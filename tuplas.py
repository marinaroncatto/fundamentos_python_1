#### Tipos de sequência e mutabilidade ####

#Um tipo de sequência é um tipo de dados em Python que é capaz de armazenar mais de um valor (ou menos de um, pois uma sequência pode estar vazia), e esses valores podem ser sequencialmente (por isso o nome) navegados, elemento a elemento.

#Como o loop for é uma ferramenta especialmente projetada para iterar através de sequências, podemos expressar a definição como: uma sequência são dados que podem ser verificados pelo for loop.

#listas são um tipo de sequencia


#A segunda noção - mutabilidade - é uma propriedade de qualquer dado Python que descreva sua disponibilidade para ser livremente alterado durante a execução do programa. Existem dois tipos de dados Python: mutáveis e imutáveis.

#Os dados mutáveis podem ser atualizados livremente a qualquer momento - chamamos isso de operação in situ.

#In situ é uma frase em latim que se traduz literalmente em posição. Por exemplo, a instrução a seguir modifica os dados in situ:


#list.append(1)
 
#Os dados imutáveis não podem ser modificados dessa maneira.

#Imagine que uma lista só possa ser atribuída e reler. Você não pode acrescentar um elemento a ele nem remover nenhum elemento dele. Isso significa que acrescentar um elemento ao final da lista exigiria a recriação da lista do zero.

#Você precisaria criar uma lista completamente nova, consistindo em todos os elementos da lista já existente, além do novo elemento.

#O tipo de dados que queremos falar agora é uma tupla. Uma tupla é um tipo de sequência imutável. Pode se comportar como uma lista, mas não pode ser modificado in situ.

#### tuplas ####

#A primeira e a mais clara distinção entre listas e tuplas é a sintaxe usada para criá-las - as tuplas preferem usar parênteses, enquanto as listas gostam de ver colchetes, embora também seja possível criar uma tupla apenas de um conjunto de valores separados por vírgulas.

#ex

tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)

#Nota: cada elemento de tupla pode ser de um tipo diferente (ponto flutuante, inteiro ou qualquer outro tipo de dados ainda não introduzidos).

#Se você deseja criar uma tupla de um elemento, precisa levar em consideração o fato de que, devido a razões de sintaxe (uma tupla precisa ser distinguida de um valor único comum), você deve terminar o valor com uma vírgula:

one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,

print(one_element_tuple_1)
print(one_element_tuple_2)
 
#Remover as vírgulas não estragará o programa em nenhum sentido sintático, mas você obterá duas variáveis únicas, não as tuplas.

#Como usar uma tupla

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
 print(elem)

#As semelhanças podem ser enganosas - não tente modificar o conteúdo de uma tupla! Não é uma lista!

 #O que mais as tuplas podem fazer por você?

#a função len() aceita tuplas e retorna o número de elementos contidos nela;
#o operador + pode unir as tuplas (já mostramos isso)
#o operador * pode multiplicar tuplas, assim como listas;
#os operadores in e not in funcionam da mesma forma que nas listas.

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

#Uma das propriedades da tupla mais úteis é a capacidade de aparecer no lado esquerdo do operador de atribuição. Vocês viram esse fenômeno há algum tempo, quando era necessário encontrar uma ferramenta elegante para trocar os valores de duas variáveis.

var = 123
 
t1 = (1, )
t2 = (2, )
t3 = (3, var)
 
t1, t2, t3 = t2, t3, t1
 
print(t1, t2, t3)

#Ele mostra três tuplas interagindo - com efeito, os valores armazenados nelas "circulam" - t1 se torna t2, t2 se torna t3 e t3 se torna t1.

#Nota: o exemplo apresenta mais um fato importante: os elementos de uma tupla podem ser variáveis, não apenas literais. Além disso, podem ser expressões se estiverem no lado direito do operador de atribuição.
 
