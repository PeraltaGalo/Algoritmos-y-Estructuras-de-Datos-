class Grafo:
    def __init__(self, es_dirigido=False):
        self.es_dirigido = es_dirigido
        self.vertices = {}

    def insertar_vertice(self, nombre):
        if nombre not in self.vertices:
            self.vertices[nombre] = {}

    def insertar_arista(self, origen, destino, peso):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen][destino] = peso
            if not self.es_dirigido:
                self.vertices[destino][origen] = peso

    def adyacentes(self, vertice):
        return self.vertices.get(vertice, {}).items()

    def kruskal(self):
        # Implementación de Kruskal para el árbol de expansión mínima
        aristas = []
        for origen in self.vertices:
            for destino, peso in self.vertices[origen].items():
                if (destino, origen, peso) not in aristas:  # Evitar duplicados
                    aristas.append((origen, destino, peso))
        
        aristas.sort(key=lambda arista: arista[2])  # Ordenar por peso
        padre = {v: v for v in self.vertices}  # Estructura para la unión y búsqueda

        def find(vertice):
            if padre[vertice] != vertice:
                padre[vertice] = find(padre[vertice])
            return padre[vertice]

        def union(v1, v2):
            raiz1 = find(v1)
            raiz2 = find(v2)
            padre[raiz1] = raiz2

        arbol_min = []
        for origen, destino, peso in aristas:
            if find(origen) != find(destino):
                union(origen, destino)
                arbol_min.append((origen, destino, peso))
                # Parar si contiene los nodos claves
                if {'c 3po', 'yoda', 'leia'}.issubset({origen, destino}):
                    break
        return arbol_min

    def personajes_comparten_episodios(self):
        print("Personajes que comparten 2 o más episodios:")
        for origen, adyacentes in self.vertices.items():
            for destino, peso in adyacentes.items():
                if peso >= 2:
                    print(f"{origen} - {destino}: {peso} episodios")

    def personaje_mas_conectado(self):
        max_personaje = None
        max_conexiones = 0
        for vertice, adyacentes in self.vertices.items():
            if len(adyacentes) > max_conexiones:
                max_conexiones = len(adyacentes)
                max_personaje = vertice
        print(f"El personaje con más conexiones es {max_personaje}, con {max_conexiones} conexiones.")
