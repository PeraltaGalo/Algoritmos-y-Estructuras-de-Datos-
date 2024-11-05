class NodoArbol:
    def __init__(self, clave, pokemon):
        self.clave = clave
        self.pokemon = pokemon
        self.izquierdo = None
        self.derecho = None


class ArbolBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, pokemon):
        if self.raiz is None:
            self.raiz = NodoArbol(clave, pokemon)
        else:
            self._insertar_recursivo(self.raiz, clave, pokemon)

    def _insertar_recursivo(self, nodo, clave, pokemon):
        if clave < nodo.clave:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(clave, pokemon)
            else:
                self._insertar_recursivo(nodo.izquierdo, clave, pokemon)
        else:
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(clave, pokemon)
            else:
                self._insertar_recursivo(nodo.derecho, clave, pokemon)

    def buscar_por_proximidad(self, clave):
        return self._buscar_por_proximidad_recursivo(self.raiz, clave)

    def _buscar_por_proximidad_recursivo(self, nodo, clave):
        if nodo is None:
            return []
        resultados = []
        if clave.lower() in nodo.pokemon['nombre'].lower():
            resultados.append(nodo.pokemon)
        resultados += self._buscar_por_proximidad_recursivo(nodo.izquierdo, clave)
        resultados += self._buscar_por_proximidad_recursivo(nodo.derecho, clave)
        return resultados

    def listar_en_orden(self):
        return self._listar_en_orden_recursivo(self.raiz)

    def _listar_en_orden_recursivo(self, nodo):
        if nodo is None:
            return []
        return (
            self._listar_en_orden_recursivo(nodo.izquierdo) +
            [nodo.pokemon] +
            self._listar_en_orden_recursivo(nodo.derecho)
        )


class AdministradorPokemon:
    def __init__(self, pokemons):
        self.pokemons = pokemons
        self.arbol_nombre = ArbolBusqueda()
        self.arbol_nivel = ArbolBusqueda()
        self.arbol_tipo = ArbolBusqueda()
        self._cargar_arboles()

    def _cargar_arboles(self):
        for pokemon in self.pokemons:
            self.arbol_nombre.insertar(pokemon["nombre"].lower(), pokemon)
            self.arbol_nivel.insertar(pokemon["nivel"], pokemon)
            self.arbol_tipo.insertar(pokemon["tipo"].lower(), pokemon)

    def buscar_por_nombre(self, nombre):
        return self.arbol_nombre.buscar_por_proximidad(nombre.lower())

    def listar_por_tipo(self, tipo):
        return [pokemon for pokemon in self.pokemons if pokemon["tipo"].lower() == tipo.lower()]

    def listar_todos(self):
        return self.arbol_nivel.listar_en_orden()

    def pokemons_especificos(self, nombres):
        return [pokemon for pokemon in self.pokemons if pokemon["nombre"] in nombres]

    def contar_por_tipo(self, tipo):
        return sum(1 for pokemon in self.pokemons if pokemon["tipo"].lower() == tipo.lower())
