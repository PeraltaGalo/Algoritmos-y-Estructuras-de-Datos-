from grafo import Grafo

# Crear el grafo no dirigido
g = Grafo(False)

# Cargar personajes 
personajes = ['luke skywalker', 'darth vader', 'yoda', 'boba fett', 'c 3po', 'leia', 'rey', 'kylo ren', 'chewbacca', 'han solo', 'r2 d2', 'obi wan kenobi', 'bb 8']
for personaje in personajes:
    g.insertar_vertice(personaje)

# Cargar las relaciones entre personajes
relaciones = [
    ('luke skywalker', 'darth vader', 3),
    ('luke skywalker', 'boba fett', 5),
    ('luke skywalker', 'c 3po', 13),
    ('rey', 'luke skywalker', 12),
    ('chewbacca', 'han solo', 7),
    ('han solo', 'r2 d2', 4),
    ('obi wan kenobi', 'kylo ren', 5),
    ('obi wan kenobi', 'r2 d2', 8),
    ('obi wan kenobi', 'bb 8', 7),
    ('bb 8', 'luke skywalker', 1),
    ('bb 8', 'leia', 2),
    ('kylo ren', 'yoda', 3),
    ('rey', 'chewbacca', 4),
    ('chewbacca', 'leia', 5),
    ('chewbacca', 'bb 8', 2),
    ('darth vader', 'chewbacca', 11),
    ('darth vader', 'r2 d2', 1),
    ('darth vader', 'han solo', 10),
    ('han solo', 'rey', 5),
    ('han solo', 'c 3po', 1),
]

for origen, destino, peso in relaciones:
    g.insertar_arista(origen, destino, peso)

# B))Árbol de expansión mínima desde C-3PO, Yoda y Leia
arbol_min = g.kruskal()
print("Árbol de expansión mínima que incluye a C-3PO, Yoda, y Leia:")
for origen, destino, peso in arbol_min:
    print(f"{origen} // {destino} con peso {peso}")

print()

# C)) Personajes que comparten 2 o más episodios
g.personajes_comparten_episodios()
print()

# E) Personaje que más conexiones tiene
g.personaje_mas_conectado()
print()
