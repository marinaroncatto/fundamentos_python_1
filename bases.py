# 1 seção - Print() e suas manipulações

print("Aspas duplas")
print('Aspas simples')
print()
#sep e end

print("Programação","Essenciais","em", sep="***", end="...")
print("Python")

print("teste com end e", end=".\n")
print("quebra de linha")
print()
#duplicando

print("pi " *3)
print()
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
print()
# número octal deve ser precedido de 0o(zero-o)

print(0o123)#o print traduzira para o número decimal correspondente

# número hexadecimal 0x (zero-x)

print(0x123) #imprimirá em decimal
print()
# floats (ponto flutuante) só aceita com ponto

print("Todos são floats")
print(0.4)
print(.4)
print(4.)
print(4.0)
print()
print("Notação científica")
print(300000000)
# notaçao científica de 3 x 10°8
print(3e8)
print(4.2e5)
# 6,62607 x 10-34
print(6.62607e-34) #Python exibe a forma mais econômica 
print(0.0000000000000000000001)
print()
#Strings

print("Strings com aspas no texto")
print("Eu gosto \"Monty Python\"")
print('Eu gosto "Monty Python"')
print('I\'m Monty Python.')
print("I'm Monty Python.")

#Boleanos True(1) e False(0)
print()
print("Booleans")
print(True > False)
print(True < False)



