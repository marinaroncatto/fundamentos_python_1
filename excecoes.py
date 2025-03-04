## validando um tipo de dado  ##

#Você já deve ser capaz de implementar essa verificação e escrever por conta própria, não deveria? Também é possível verificar se o tipo da variável value é um int (Python tem um meio especial para esses tipos de verificações - é um operador chamado is. A verificação em si pode ficar assim:


#type(value) is int
 
#e avalia como true se o tipo da variável de valor atual é int.

##O ramo de tentativa exceto##

#try:
 # Esse é um lugar
 # que você pode fazer algo
 # sem pedir permissão.
#except:
 # Esse lugar é dedicado
 # apenas para implorar por persão.

 
#Você pode ver dois ramos aqui:

#primeiro, começando com a palavra-chave try - este é o lugar onde você coloca o código que você suspeita ser arriscado e pode ser encerrado em caso de erro; Nota: esse tipo de erro é chamado de exceção, enquanto a ocorrência da exceção é lançada- podemos dizer que uma exceção é (ou foi) gerada;
#segundo, a parte do código que começa com a palavra-chave except é projetada para lidar com a exceção; depende de você o que você quer fazer aqui: você pode limpar a bagunça ou apenas varrer o problema para baixo do tapete (embora prefiramos a primeira solução).
#Então, poderíamos dizer que esses dois blocos funcionam assim:

#a palavra-chave try marca o local onde você tenta fazer algo sem permissão;
#a palavra-chave except inicia um local onde é possível exibir talentos de desculpas.
#Como você pode ver, essa abordagem aceita erros (os trata como uma parte normal da vida útil do programa) em vez de intensificar os esforços para evitar erros.

try:
     value= int (input('Insira um número natural:')) 
     print('O recíproco de', valor, 'é', 1 / value) 
except: 
     print('Não sei o que fazer.')

#Vamos resumir sobre o que falamos:

#qualquer parte do código colocada entre try e except é executada de uma maneira muito especial - qualquer erro que ocorre aqui não terminará a execução do programa. Em vez disso, o controle saltará imediatamente para a primeira linha situada após a palavra-chave except, e nenhuma outra parte do ramo try é executada;
#o código no ramo except é ativado somente quando uma exceção é encontrada dentro do bloco try. Não há como chegar lá por qualquer outro meio;
#quando o bloco de try ou o bloco except é executado com sucesso, o controle retorna para o caminho normal de execução, e qualquer código localizado além no arquivo de origem é executado como se nada tivesse acontecido.


## Duas exceções após um try     ###

#Olhe para o código no editor. Como você pode ver, acabamos de apresentar o segundo ramo except. Essa não é a única diferença - observe que ambos os ramos têm nomes de exceção especificados. Nessa variante, cada uma das exceções esperadas tem sua própria maneira de lidar com o erro, mas deve ser enfatizado que apenas uma de todas exceções pode interceptar o controle - se um dos ramos for executado, todos os outros permanecerão inativas.

try:
 value = int(input('Digite um número natural: '))
 print('O recíproco de', value, 'é', 1/value) 
except ValueError:
 print('Eu não sei o que fazer.') 
except ZeroDivisionError:
 print('A divisão por zero não é permitida em nosso Universo.')

#Além disso, o número de ramos except não é limitado. Você pode especificar quantos deles precisar, mas não esqueça que nenhuma das exceções pode ser especificada mais de uma vez.

##A exceção padrão e como usá-la##

try:
    value = int (input('Insira um número natural:')) 
    print('O recíproco de', value, 'é', 1 / value) 
except ValueError:
     print('Não sei o que fazer.' ) 
except ZeroDivisionError:
     print('Divisão por zero não é permitida em nosso universo.') 
except: 
    print('algo de estranho aconteceu aqui ... Desculpe! ')

#Adicionamos um terceiro, ramo except, mas desta vez não tem nenhum nome de exceção especificado - podemos dizer que é anônimo ou (o que está mais próximo da sua função real) é o padrão. Você pode esperar que, quando uma exceção for gerada e não houver nenhum ramo except dedicada, ela seja tratada ramo padrão.

#  Nota  
#O except padrão deve ser o último except. Sempre!


###### 4.7.7 Algumas exceções úteis #############

#Vamos discutir com mais detalhes algumas exceções úteis (ou melhor, as mais comuns) que você pode enfrentar.

#ZeroDivisionError
#Isso aparece quando você tenta forçar o Python a executar qualquer operação que provoque uma divisão na qual o divisor é zero ou é indistinguível de zero. Observe que há mais de um operador Python que pode causar essa exceção. Você consegue adivinhar todos eles?

#Sim, eles são: /, // e %.

#ValueError
#Espere essa exceção ao lidar com valores que podem ser usados de forma inadequada em algum contexto. Em geral, essa exceção é gerada quando uma função (como int() ou float()) recebe um argumento de um tipo adequado, mas seu valor é inaceitável.

#TypeError
#Essa exceção aparece quando você tenta aplicar dados cujo tipo não pode ser aceito no contexto atual. Veja o exemplo:


#short_list = [1]
#one_value = short_list[0.5]
 
#Você não pode usar um valor flutuante como um índice de lista (a mesma regra também se aplica às tuplas). TypeError é um nome adequado para descrever o problema e uma exceção adequada para gerar.

#AttributeError
#Essa exceção chega, entre outras ocasiões, quando você tenta ativar um método que não existe em um item com o qual está lidando. Por exemplo:


#short_list = [1]
#short_list.append(2)
#short_list.depend(3)
 
#A terceira linha do nosso exemplo tenta usar um método que não está contido nas listas. Este é o local onde o AttributeError é gerado.

#SyntaxError
#Essa exceção é gerada quando o controle atinge uma linha de código que viola a gramática do Python. Pode parecer estranho, mas alguns erros desse tipo não podem ser identificados sem antes executar o código. Esse tipo de comportamento é típico das linguagens interpretadas - o intérprete sempre trabalha com pressa e não tem tempo para verificar todo o código-fonte. Ele se contenta em verificar o código que está sendo executado no momento. Um exemplo dessa categoria de problemas será apresentado em breve.

#É uma má ideia lidar com essa exceção nos programas. Você deve produzir um código livre de erros de sintaxe, em vez de mascarar as falhas que causou.

# Algumas das exceções internas mais úteis do Python são: ZeroDivisionError, ValueError, TypeError, AttributeError e SyntaxError. Mais uma exceção que, em nossa opinião, merece sua atenção é a exceção KeyboardInterrupt, que é acionada quando o usuário pressiona a tecla de interrupção (CTRL-C ou Excluir). Execute o código acima e pressione a combinação de teclas para ver o que acontece.
