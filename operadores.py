# Operadores

print(2+2)

# Exponenciação
print()
print("Exponenciação")
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

#quando os dois ** argumentos são inteiros, o resultado também é um número inteiro;
#Quando pelo menos um argumento ** é um float, o resultado também é um float.

# Multiplicação

print()
print("Multiplicação")
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

#Divisão

print()
print("Divisão")
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

#O resultado produzido pelo operador de divisão é sempre um float

# Divisão de número inteiro (divisão arredondada)
print()
print("Divisão de número inteiro (divisão arredondada)")
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
print()
print(6 / 4)
print(6 // 4)
print(6. // 4)

#O resultado da divisão do número inteiro é sempre arredondado para
#o valor inteiro mais próximo que é menor que o resultado real (não arredondado).

print("o arredondamento sempre vai para o número inteiro menor.")
print(-6 // 4)
print(6. // -4)
# o resultado seria -1.5,mas -2 é o inteiro arredondado menor

# Restante (módulo / mod)

print()
print("Mod")
print("O resultado do operador é o restante após a divisão do número inteiro.")
print(14 % 4) #resto 2

#Como você provavelmente sabe, a divisão por zero não funciona.

# Adição

print()
print("adição")
print(-4 + 4)
print(-4. + 8)

# O operador de subtração, os operadores unários e binários

print()
print("- = Subtração ou números negativos")
print(-4 - 4)
print(4. - 8)
print(-1.1)

# Operadores e suas ligações

print()
print("O Python respeita a hierarquia das operações e executa os calculos da esquerda para direita")
print(9 % 6 % 2)
print("os calculos exponenciais são uma excessão e começam pela direita")
print(2 ** 2 ** 3)

print(2 ** 3 ** 2)
