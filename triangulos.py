### sistema que verifica se os dados podem constituir um triangulo e faz seus calculos ##

def is_a_triangle(a, b, c): #verifica se os valores podem ser de um triangulo
    return a + b > c and b + c > a and c + a > b
 #a soma de dois lados arbitrários precisa ser maior que o terceiro lado.
 
def heron(a, b, c): #A fórmula da Heron para calcular area
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
 
 
def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)
 
 
print(area_of_triangle(1., 1., 2. ** .5))
 
def is_a_right_triangle(a, b, c): # teorema de pitagoras:
    if not is_a_triangle(a, b, c):
        return False
    elif c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    elif a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    elif b > a and b > c:
        return b ** 2 == a ** 2 + c ** 2
    else:
        return false    
    
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))
 
