
#sistema que calcula IMC


def ft_and_inch_to_m(ft, inch = 0.0): # converte de pés para metros
    return ft * 0.3048 + inch * 0.0254
 
 
def lb_to_kg(lb): # converte de libra para kg
    return lb * 0.4535923
 
 
def bmi(weight, height): #calcula o imc
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
 
    return weight / height ** 2
 
 
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))

#o símbolo de barra invertida (\) é usado. Se você usá-lo no código Python e terminar uma linha com ele, ele informará o Python para continuar a linha de código na próxima linha de código.
