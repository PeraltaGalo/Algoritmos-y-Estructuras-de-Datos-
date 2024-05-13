# 22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# ayuda de la fuerza” realizar las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila;

# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
# car para encontrarlo;

# c. Utilizar un vector para representar la mochila.

def usarLaFuerza(i=0):
    mochila=["","","","","","","","",""]
    mochila[i] = input("elemento a sacar?= ")
    if i>=len(mochila):
        print("no hay mas objetos en la mochila")
        return len(mochila),-1
    elif mochila[i]== "sable de luz" :
        print("se encontro el sable azul")
        return i+1,i
    else:
        sacado,indice = usarLaFuerza( i+1)
        if indice != -1:
            return sacado,indice
        return sacado,-1
c,i=usarLaFuerza()
print(f"la cant de elementos sacados fueron {c} el indice donde se encontro es el {i} ")