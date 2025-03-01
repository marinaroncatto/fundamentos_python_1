
#Sua tarefa é escrever uma função verificando se um número é primo ou não.

#é chamado is_prime;
#requer um argumento (o valor a ser verificado)
#retorna True se o argumento for um número primo e False caso contrário.
#Dica: tente dividir o argumento por todos os valores subsequentes (começando em 2) e verifique o restante - se for zero, seu número não pode ser um primo; pense bem quando deve interromper o processo.

#Se você precisar conhecer a raiz quadrada de qualquer valor, poderá utilizar o operador **. Lembre-se: a raiz quadrada de x é o mesmo que x0.5

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Testando a função para imprimir os primeiros números primos
primes = []
for i in range(2, 20):  # Verificar números até 20
    if is_prime(i):
        primes.append(i)

print(*primes)  # A saída será os números primos até 19
