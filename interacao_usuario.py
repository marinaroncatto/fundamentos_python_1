# input() -> entrada de dados

print("Função input()")
print("Conta-me qualquer coisa...")
#anything = input()
#print("Hum...", anything, "... Realmente?")

# input() com agumento (semelhante a um placeholder)
print()
#anything = input("Conta-me qualquer coisa...")
#print("Hum...", anything, "...Realmente?")
 
# tudo vira String com o input()

#anything = input("Digite um número: ")
#something = anything ** 2.0
#print(anything, "elevado a 2 é", something)
 
# a operação resulta em erro 
 
# CONVERSÃO DE TIPO
# função int() e float() converte a entrada str em seus tipos

anything = float(input("Digite um número: "))
something = anything ** 2.0
print(anything, "elevado a 2 é", something)

print()

anything = int(input("Digite um número: "))
something = anything ** 2.0
print(anything, "elevado a 2 é", something)

print()

# pitagoras

leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("O comprimento da hipotenusa é", round(hypo, 2))

print()

leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
print("O comprimento da hipotenusa é", (leg_a**2 + leg_b**2) ** .5)
#calculando direto com o print()

# + concatenador de Strings (só funciona quando todos forem stri

fnam = input("Posso ter seu primeiro nome, por favor? ")
lnam = input("Posso ter seu sobrenome, por favor? ")
print("Obrigado!.")
print("\nSeu nome é " + fnam + " " + lnam + ".")

# operador * com strings serve para replicar

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

# conversão em String str()
#converte números em strings

leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
print("O comprimento da hipotenusa é " + str((leg_a**2 + leg_b**2) ** .5))

# lab 1

print()

a = float(input("Digite um número a: "))
b = float(input("Digite um número b:"))

print("Adição = "+ str(a + b))
print("Subtração = "+ str(a - b))
print("Multiplicação = "+ str(a * b))
print("Divisão = "+ str(a / b))

print("\nIsso é tudo, pessoal!")

#versão 2

print()
a = float(input("Entre com o primeiro valor: "))
b = float(input("Entre com o segundo valor: "))
print("Adição:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)
print("Divisão:", a / b)
print("\nIsso é tudo, pessoal!")

# lab 2

x = float(input("Digite o valor para x: "))

y = 1 /( x + 1/(x + 1/(x +1 / x)))

print("y =", y)







