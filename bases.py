# 1 seção - Print() e suas manipulações

print("Aspas duplas")
print('Aspas simples')

#sep e end

print("Programação","Essenciais","em", sep="***", end="...")
print("Python")

print("teste com end e", end=".\n")
print("quebra de linha")

#duplicando

print("pi " *3)

# 2 seção - Literais e tipos dedados

# int - inteiro

# A função print() os apresenta exatamente da mesma maneira ‒
# este exemplo é óbvio, pois sua representação legível por humanos também
# é a mesma. Internamente, na memória do computador, esses dois valores são
# armazenados de formas completamente diferentes ‒ a string existe apenas
# como uma string ‒ uma série de letras.

print("2")
print(2)

print(111111111)
print(11_111_1111) #sublinhados foram inseridos no Python 3

# número octal deve ser precedido de 0o(zero-o)

print(0o123)#o print traduzira para o número decimal correspondente

# número hexadecimal 0x (zero-x)

print(0x123) #imprimirá em decimal
