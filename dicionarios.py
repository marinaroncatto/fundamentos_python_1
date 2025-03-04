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
