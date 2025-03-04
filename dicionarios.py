#O dicionário é outra estrutura de dados Python. Não é um tipo de sequência (mas pode ser facilmente adaptado ao processamento de sequência) e é mutável.

#Para explicar o que é o dicionário Python, é importante entender que ele é literalmente um dicionário.

### Como fazer um dicionário ###

#Se você deseja atribuir alguns pares iniciais a um dicionário, use a seguinte sintaxe:


dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
phone_numbers = {'chefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
 
print(dictionary)
print(phone_numbers)
print(empty_dictionary)

#No primeiro exemplo, o dicionário usa chaves e valores, que são as duas strings. No segundo, as chaves são cadeias de caracteres, mas os valores são números inteiros. O layout reverso (teclas → números, valores → cadeias) também é possível, bem como combinações número-número.

#A lista de pares é cercada por chaves, enquanto os pares são separados por vírgulas, e as chaves e os valores por dois pontos.

#O primeiro de nossos dicionários é um dicionário inglês-francês muito simples. O segundo - uma lista telefônica muito pequena.

#O dicionário vazio é construído por um par vazio de chaves - nada de incomum.

#O dicionário Python funciona da mesma forma que um dicionário bilíngue. Por exemplo, você tem uma palavra em inglês (por exemplo, gato) e precisa do equivalente em francês. Você navega no dicionário para encontrar a palavra (você pode usar técnicas diferentes para fazer isso - não importa) e, eventualmente, obtê-la. Em seguida, verifique a contraparte em francês e é (provavelmente) a palavra "chat".

#No mundo do Python, a palavra que você procura é chamada de key. A palavra que você recebe do dicionário é chamada de value.

#Isso significa que um dicionário é um conjunto de pares de key-value. Nota:

#cada chave deve ser única - não é possível ter mais de uma chave com o mesmo valor;
#uma chave pode ser qualquer tipo imutável de objeto: pode ser um número (inteiro ou flutuante), ou até mesmo uma string, mas não uma lista;
#um dicionário não é uma lista - uma lista contém um conjunto de valores numerados, enquanto um dicionário contém pares de valores;
#a função len() também funciona para dicionários - ela retorna o número de elementos de valor-chave no dicionário;
#um dicionário é uma ferramenta de mão única. Se você tiver um dicionário inglês-francês, poderá procurar equivalentes em francês dos termos em inglês, mas não vice-versa.

#Primeiro de tudo, é uma confirmação de que os dicionários não são listas - eles não preservam a ordem dos dados, pois a ordem é completamente sem sentido (ao contrário dos dicionários de papel reais). A ordem em que um dicionário armazena seus dados está completamente fora de seu controle e de suas expectativas. Isso é normal. (*)

#  Nota  
#(*) No Python, os dicionários 3.6x tornaram-se coleções ordenadas por padrão. Seus resultados podem variar dependendo da versão do Python que você está usando.

#Se quiser obter qualquer um dos valores, é necessário fornecer um valor-chave válido:


print(dictionary['gato'])
print(phone_numbers['Suzy'])

#Obter o valor de um dicionário se assemelha à indexação, especialmente graças aos colchetes em torno do valor da chave.

#Nota:

#se a chave for uma string, você precisará especificá-la como uma string;
#chaves fazem distinção entre maiúsculas e minúsculas: "Suzy" é algo diferente de "suzy".

#E agora a notícia mais importante: você não deve usar uma chave inexistente.

#Felizmente, há uma maneira simples de evitar essa situação. O operador in, junto com seu acompanhante, not in, pode salvar essa situação.

#O código a seguir pesquisa com segurança algumas palavras em francês:


dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
words = ['gato', 'lion', 'cavalo']
 
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "não está no dicionário")

#Nota  
#Quando você escreve uma expressão grande ou longa, pode ser uma boa ideia mantê-la alinhada verticalmente. É assim que você pode tornar seu código mais legível e mais fácil para programadores, por exemplo:


# Exemplo 1:
dictionary = {
              "gato": "chat",
              "cachorro": "chien",
              "cavalo": "cheval"
}
# Exemplo 2:
phone_numbers = {'chefe': 5551234567,
              'Suzy': 22657854310
}
 
#Esse tipo de formatação é chamado de recuo suspenso.

## 4.6.4 Métodos e funções de dicionário ##

#O método keys()

#O método retorna um objeto iterável que consiste em todas as chaves reunidas no dicionário. Ter um grupo de chaves permite acessar todo o dicionário de forma fácil e prática.

dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
for key in dictionary.keys():
    print(key, "->", dictionary[key])


## items()

#Vamos agora dar uma olhada em um método de dicionário chamado items(). O método retorna tuplas (este é o primeiro exemplo em que as tuplas são algo mais do que apenas um exemplo delas) em que cada tupla é um par de valores-chave.

dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
for portuguese, french in dictionary.items():
    print(portuguese, "->", french)

#Modificação e adição de valores#

#Vamos substituir o valor "chat" por "minou", que não é muito preciso, mas funcionará bem com o nosso exemplo.

dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
dictionary['gato'] = 'minou'
print(dictionary)

## A função sorted() ##

#Deseja que ele seja ordenado? Basta enriquecer o loop for para obter o seguinte formulário:


for key in sorted(dictionary.keys()):

#Há também um método chamado values(), que funciona de forma semelhante a keys(), mas retorna valores.

#Aqui está um exemplo simples:


dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
for french in dictionary.values():
    print(french)
 
#Como o dicionário não consegue encontrar automaticamente uma chave para um determinado valor, a função desse método é bastante limitada.

## Adição de uma nova chave ##

#Adicionar um novo par de valores-chave a um dicionário é tão simples quanto alterar um valor - você só precisa atribuir um valor a uma nova chave anteriormente inexistente.

#Nota: esse é um comportamento muito diferente em comparação às listas, que não permitem atribuir valores a índices inexistentes.

#Vamos adicionar um novo par de palavras ao dicionário - um pouco estranho, mas ainda válido:


dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
dictionary['swan'] = 'cygne'
print(dictionary)
 

#  Nota  
#Você também pode inserir um item em um dicionário usando o método update(), por exemplo:


dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
dictionary.update({"pato": "canard"})
print(dictionary)

## Removendo uma chave ##


#Nota: a remoção de uma chave sempre causará a remoção do valor associado. Os valores não podem existir sem as chaves.

#Isso é feito com a instrução del.

3Aqui está o exemplo:


dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
del dictionary['cachorro']
print(dictionary)
 
#Nota: remover uma chave não existente causa um erro.

#O exemplo gera:

#{'gato': 'chat', 'cavalo': 'cheval'}

#Para remover o último item de um dicionário, você pode usar o método popitem():


dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
dictionary.popitem()
print(dictionary) # saídas: {'gato': 'chat', 'cachorro': 'chien'}
 
#Nas versões mais antigas do Python, ou seja, antes da versão 3.6.7, o método popitem() remove um item aleatório de um dicionário.

###Pontos chave: dicionários####
#1. Os dicionários são conjuntos de dados indexados *, mutáveis e indexados. (* Desdo Python 3.6x os dicionários passaram a ser ordenados por padrão.)

#Cada dicionário é um conjunto de pares chave: valor. Você pode criá-lo usando a seguinte sintaxe:


my_dictionary = {
    key1: value1,
    key2: value2,
    key3: value3,
}
 
#2. Se você quiser acessar um item de dicionário, faça isso fazendo uma referência à sua chave dentro de um par de colchetes (por exemplo, 1) ou usando o método get() (por exemplo, 2):


pol_eng_dictionary = {
    "kwiat": "flor",
    "woda": "água",
    "gleba": "solo"
    }
 
item_1 = pol_eng_dictionary["gleba"] # ex. 1
print(item_1) # saídas: solo
 
item_2 = pol_eng_dictionary.get("woda") # ex. 2
print(item_2) # saídas: água
 
#3. Se você quiser alterar o valor associado a uma chave específica, consulte o nome da chave do item da seguinte forma:


pol_eng_dictionary = {
    "zamek": "castelo",
    "woda": "água",
    "gleba": "solo"
    }
 
pol_eng_dictionary["zamek"] = "trancar"
item = pol_eng_dictionary["zamek"]
print(item) # saídas: trancar
 
#4. Para adicionar ou remover uma chave (e o valor associado), use a seguinte sintaxe:


phonebook = {} # um dicionário vazio
 
phonebook["Adão"] = 3456783958 # criar/adicionar um par chave-valor
print(phonebook) # saídas: {'Adão': 3456783958}
 
del phonebook["Adão"]
print(phonebook) # saídas: {}
 
#Você também pode inserir um item em um dicionário usando o método update() e remover o último elemento usando o método popitem(), por exemplo:


pol_eng_dictionary = {"kwiat": "flor"}
 
pol_eng_dictionary.update({"gleba": "solo"})
print(pol_eng_dictionary) # saídas: {'kwiat': 'flor', 'gleba': 'solo'}
 
pol_eng_dictionary.popitem()
print(pol_eng_dictionary) # saídas: {'kwiat': 'flor'}
 
#5. Você pode usar o loop for para percorrer um dicionário, por exemplo:


pol_eng_dictionary = {
    "zamek": "castelo",
    "woda": "água",
    "gleba": "solo"
    }
 
for item in pol_eng_dictionary:
    print(item)
 
#          woda
#          gleba
 
#6. Se você deseja percorrer as chaves e os valores de um dicionário, pode usar o método items(), por exemplo:


pol_eng_dictionary = {
    "zamek": "castelo",
    "woda": "água",
    "gleba": "solo"
    }
 
for key, value in pol_eng_dictionary.items():
    print("Pol/Eng ->", key, ":", value)
 
#7. Para verificar se uma determinada chave existe em um dicionário, você pode usar a palavra-chave in:


pol_eng_dictionary = {
    "zamek": "castelo",
    "woda": "água",
    "gleba": "solo"
    }
 
if "zamek" in pol_eng_dictionary:
   print("Sim")
else:
   print("Não")
 
#8. Você pode usar a palavra-chave del para remover um item específico ou excluir um dicionário. Para remover todos os itens do dicionário, você precisa usar o método clear():


pol_eng_dictionary = {
    "zamek": "castelo",
    "woda": "água",
    "gleba": "solo"
    }
 
print(len(pol_eng_dictionary)) # saídas: 3
del pol_eng_dictionary["zamek"] # remover um item
print(len(pol_eng_dictionary)) # saídas: 2
 
pol_eng_dictionary.clear() # remove todos os itens
print(len(pol_eng_dictionary)) # saídas: 0
 
del pol_eng_dictionary # remove o dicionário
 
#9. Para copiar um dicionário, use o método copy():


pol_eng_dictionary = {
    "zamek": "castelo",
    "woda": "água",
    "gleba": "solo"
    }
 
copy_dictionary = pol_eng_dictionary.copy()

