# matrizes #

#As listas podem consistir em escalares (ou seja, números) e elementos de uma estrutura muito mais complexa (você já viu exemplos como strings, booleanos ou até mesmo outras listas nas lições anteriores do Resumo da seção). Vamos dar uma olhada no caso em que os elementos de uma lista são apenas listas.

#ex 1 xadrez


row = []
 
for i in range(8):
    row.append(WHITE_PAWN)

#O mesmo efeito pode ser alcançado por meio de uma compreensão de lista, a sintaxe especial usada pelo Python para preencher listas enormes.


#Confira o trecho:


row = [WHITE_PAWN for i in range(8)]

#os dados a serem usados para preencher a lista (WHITE_PAWN)
#a cláusula que especifica quantas vezes os dados ocorrem dentro da lista (for i in range(8))

#Exemplo #1:


squares = [x ** 2 for x in range(10)]

#O snippet produz uma lista de dez elementos preenchida com quadrados de dez números inteiros começando em zero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

#Exemplo #2:


twos = [2 ** i for i in range(8)]
 
#O fragmento cria uma matriz de oito elementos que contém as oito primeiras potências de dois (1, 2, 4, 8, 16, 32, 64, 128)

#Exemplo #3:


odds = [x for x in squares if x % 2 != 0 ]

#O fragmento faz uma lista com apenas os elementos ímpares da lista de squares.

## matrizes bidimensionais ##

board = []
 
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
 
#Nota:

#a parte interna do loop cria uma linha que consiste em oito elementos (cada um deles igual a EMPTY) e a anexa à lista ao board;
#a parte externa a repete oito vezes;
#no total, a lista board compõe-se de 64 elementos (todos iguais a EMPTY)

#A variável board é agora uma matriz bidimensional. É também chamada, por analogia aos termos algébricos, de matriz.

#Como as compreensões da lista podem ser aninhadas, podemos reduzir a criação da placa da seguinte maneira:


board = [[EMPTY for i in range(8)] for j in range(8)]
 
#A parte interna cria uma linha e a parte externa cria uma lista de linhas.

#O acesso ao campo selecionado do quadro requer dois índices: o primeiro seleciona a linha; o segundo - o número do campo dentro da linha, que é de fato um número de coluna.

### Natureza multidimensional das listas: aplicações avançadas ###


#Vamos aprofundar a natureza multidimensional das listas. Para encontrar qualquer elemento de uma lista bidimensional, você precisa usar duas coordenadas:

#a vertical (número da linha)
#e horizontal (número da coluna).

#Imagine que você está desenvolvendo um software para uma estação meteorológica automática. O dispositivo registra a temperatura do ar a cada hora e faz isso durante todo o mês. Isso gera um total de 24 × 31 = 744 valores. Vamos tentar criar uma lista capaz de armazenar todos esses resultados.

#Primeiro, você precisa decidir que tipo de dados seria adequado para essa aplicação. Nesse caso, um float seria o melhor, já que este termômetro é capaz de medir a temperatura com uma precisão de 0,1 ° C.

#Em seguida, você toma uma decisão arbitrária de que as linhas gravarão as leituras de hora em hora (para que a linha tenha 24 elementos) e cada uma das linhas será atribuída a um dia do mês (vamos supor que cada mês tenha 31 dias, então você precisa de 31 linhas). Aqui está o par apropriado de compreensões (h é para hora, d para dia):


temps = [[0.0 for h in range(24)] for d in range(31)]


#Toda a matriz está preenchida com zeros agora. Você pode supor que ela é atualizada automaticamente usando agentes de hardware especiais. O que você precisa fazer é esperar que a matriz seja preenchida com medidas.

#Agora é hora de determinar a temperatura média mensal ao meio-dia. Adicione todas as 31 leituras gravadas ao meio-dia e divida a soma por 31. Você pode supor que a temperatura da meia-noite é armazenada primeiro. Aqui está o código relevante:

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# A matriz é magicamente atualizada aqui.
#
 
total = 0.0
 
for day in temps:
    total += day[11]
 
average = total / 31
 
print("Temperatura média ao meio-dia:", average)
 
#Observação: a variável day usada pelo loop for não é escalar; cada passagem pela matriz day itera por todas as linhas na temps a atribui às linhas subsequentes da matriz; portanto, é uma lista. Ele precisa ser indexado com 11 para acessar o valor de temperatura medido ao meio-dia.

#Agora, encontre a temperatura mais alta durante todo o mês - veja o código:


temps = [[0.0 for h in range(24)] for d in range(31)]
#
# A matriz é magicamente atualizada aqui.
#
 
highest = -100.0
 
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
 
print("A maior temperatura foi:", highest)
 
#Nota:

#a variável day itera por todas as linhas na matriz temps;
#a variável temp itera todas as medidas feitas em um dia.

#Agora conte os dias em que a temperatura ao meio-dia era de pelo menos 20 ℃:


temps = [[0.0 for h in range(24)] for d in range(31)]
#
# A matriz é magicamente atualizada aqui.
#
 
hot_days = 0
 
for day in temps:
    if day[11] > 20.0:
        hot_days += 1
 
print(hot_days, "dias estavam quentes.")
 

## matriz tridimensional ##

#O Python não limita a profundidade da inclusão na lista. Aqui você pode ver um exemplo de uma matriz tridimensional:


rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
 
#Imagine um hotel. É um grande hotel composto de três edifícios, de 15 andares cada. Há 20 salas em cada andar. Para isso, você precisa de uma matriz que possa coletar e processar informações sobre as salas ocupadas/livres.

#Primeira etapa - o tipo dos elementos da matriz. Nesse caso, um valor booleano (True/False) seria adequado.

#Etapa dois - Análise calma da situação. Resuma as informações disponíveis: três edifícios, 15 andares, 20 salas.

#Agora você pode criar a matriz:


rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
 
#O primeiro índice (0 a 2) seleciona um dos edifícios; o segundo (0 a 14) seleciona o piso, o terceiro (0 a 19) seleciona o número do quarto. Todas as salas são gratuitas.

#Agora você pode reservar um quarto para dois noivos: no segundo edifício, no décimo andar, quarto 14:


rooms[1][9][13] = True
 
#e liberar a segunda sala no quinto andar, localizada no primeiro edifício:


rooms[0][4][1] = False
 
#Verifique se há vagas no 15º andar do terceiro edifício:


vacancy = 0
 
for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
 
#A variável vacancy contém 0 se todas as salas estiverem ocupadas ou o número de salas disponíveis em contrário.
