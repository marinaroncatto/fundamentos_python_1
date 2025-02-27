#Imagine uma lista - não muito longa, não muito complicada, apenas uma lista simples que contém alguns números inteiros. Alguns desses números podem ser repetidos, e essa é a pista. Não queremos repetições. Queremos que eles sejam removidos.

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#m
# Escreva seu código aqui.
#
u_list = []

for num in my_list:
    if num not in u_list:
        u_list.append(num)
        
print(u_list)
print(my_list)
