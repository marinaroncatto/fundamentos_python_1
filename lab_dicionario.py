#escreva um programa que junte os dois dicionários (d1 e d2) e crie um novo (d3).

d1 = {'Adão Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)
