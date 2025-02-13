# variáveis

print("Uma variável passa a existir como resultado da atribuição de um valor a ela. Ao contrário de outros idiomas, você não precisa declará-lo de nenhuma maneira especial.")
print("A criação (ou seja, sua sintaxe) é extremamente simples: basta usar o nome da variável desejada, depois o sinal de igual (=) e o valor que deseja colocar na variável.")
variavel = 1 #variável
print(variavel)

print()

var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)

# concatenação

print()
print("concatenação")

var = "3.8.5"
print("Versão Python: " + var)
 
print()
print("Teorema de pitagoras")

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

#exercício
print()
john = 3
mary = 5
adam = 6
print(john, mary, adam, sep=',')
total_apples = john + mary + adam
print("Número total de maças: ", end='')
print(total_apples)

peter = 12.5
suzy = 2
print(peter / suzy)
print("Número total de maçãs:", total_apples)


#Operadores atalhos
print()
print("Operadores atalhos")
#i = i + 2 * j
#i += 2 * j

#var = var / 2
#var /= 2

#rem = rem % 10
#rem %= 10

#j = j - (i + var + rem)
#j -= (i + var + rem)

#x = x ** 2
#x **= 2


#lab variáveis
print()
print("Lab variáveis")
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "milhas é", round(miles_to_kilometers, 2), "quilômetros")
print(kilometers, "quilômetros é", round(kilometers_to_miles, 2), "milhas")

#função round() serve para formatar o número de casas decimais do float

# lab operadores e expressões

# y = 3x3 - 2x2 + 3x - 1
print()
print("Lab operadores e expressões")
x = -1
x = float(x)
y = 3 * x **3 - 2 * x ** 2 + 3 * x - 1
print("y =", y)

print()
a = 6
b = 3
a /= 2 * b
print(a)
