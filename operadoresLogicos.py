###### and #########

#Um operador de conjunção lógica em Python é a palavra and. É um operador binário com uma prioridade menor do que a expressa pelos operadores de comparação. Ela nos permite codificar condições complexas sem o uso de parênteses como este:


#counter > 0 and value == 100

### or #####

#Um operador de disjunção é a palavra or. É um operador binário com uma prioridade menor do que and (assim como + em comparação com *).

### not ####

#Além disso, há outro operador que pode ser aplicado à construção de condições. É um operador unário que executa uma negação lógica. Sua operação é simples: transforma verdade em falsidade e falsidade em verdade.

#Esse operador é escrito como a palavra not, e sua prioridade é muito alta: o mesmo que os + e - unários. Sua tabela de verdade é simples:

## expressões lógicas ##

#Vamos criar uma variável chamada var e atribuir 1 a ela. As condições a seguir são equivalentes aos pares:

# Exemplo 1:
#print(var > 0)
#print(not (var <= 0))
 
 
# Exemplo 2:
#print(var != 0)
#print(not (var == 0))
 
### operadores bit a bit #####

#No entanto, existem quatro operadores que permitem manipular bits únicos de dados. Eles são chamados de operadores bit a bit.

#Eles abrangem todas as operações que mencionamos anteriormente no contexto lógico e um operador adicional. Este é o operador xor (as em exclusivo ou) e é indicado como ^ (circunflexo).

#Aqui estão todos eles:

#& (e comercial) - conjunção bit a bit;
#| (barra) - disjunção bit a bit;
#~ (til) - negação bit a bit;
#^ (circunflexo) ‒ bit a bit exclusivo ou (xor).

#Vamos facilitar:

#& requer exatamente dois 1 s para fornecer 1 como resultado;
#| requer pelo menos um 1 para fornecer 1 como resultado;
#^ requer exatamente um 1 para fornecer 1 como resultado.
#Vamos acrescentar uma observação importante: os argumentos desses operadores devem ser números inteiros; não devemos usar carros alegóricos aqui.

#Cada um desses operadores de dois argumentos pode ser usado de forma abreviada. Estes são os exemplos de notações equivalentes:

#x = x & y == x &= y
#x = x | y == x |= y
#x = x ^ y == x ^= y

### deslocamento binário esquerda e direita

# Os operadores de deslocamento em Python são um par de dígrafos: << e >>, sugerindo claramente em qual direção o deslocamento vai agir.

# ex

#valor << bits
#valor >> bits


var = 17
var_right = var >> 1
var_left = var << 2
print (var, var_left, var_right)

#17 >> 1 → 17 // 2 (17 piso dividido por 2 à potência de 1) → 8 (deslocar para a direita por um bit é igual a divisão inteira por dois)
#17 << 2 → 17 * 4 (17 multiplicado por 2 à potência de 2) → 68 (deslocar para a esquerda por dois bits é igual a multiplicação do número inteiro por quatro 


