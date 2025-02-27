# etapa 1
beatles = []
print("Etapa 1:", beatles)


# etapa 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Etapa 2:", beatles)


# etapa 3

input("Adicione Stu Sutcliffe e Pete Best: ")

for i in range(2):
     name = input("Digite um nome: ")
     beatles.append(name)
print("Etapa 3:", beatles)


# etapa 4
del beatles[4]
del beatles[3]
print("Etapa 4:", beatles)

# passo 5
beatles.insert(0, "Ringo Starr")
print("Etapa 5:", beatles)



# testando o tamanho da lista

print("o fabuloso", len(beatles))
