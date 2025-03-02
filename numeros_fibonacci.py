## sistema que calcula números de fibonacci  ##

#Eles são uma sequência de números inteiros criados usando uma regra muito simples:

#o primeiro elemento da sequência é igual a um (Fib1 = 1)
#o segundo também é igual a um (Fib 2 = 1)
#cada número subsequente é a the_sum dos dois números anteriores:( Fib i = Fib i-1 + Fib i-2)
#Aqui estão alguns dos primeiros números de Fibonacci:

#fib_1 = 1 fib_2 = 1 fib_3 = 1 + 1 = 2 fib_4 = 1 + 2 = 3 fib_5 = 2 + 3 = 5 fib_6 = 3 + 5 = 8 fib_7 = 5 + 8 = 13

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
 
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
 
 
for n in range(1, 10):  # testando
    print(n, "->", fib(n))
 
# saída esperada
#1 -> 1
#2 -> 1
#3 -> 2
#4 -> 3
#5 -> 5
#6 -> 8
#7 -> 13
#8 -> 21
#9 -> 34
