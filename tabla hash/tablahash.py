# Escribir un algoritmo que permita utilizar tres tablas hash para guardar los datos de Pokémons,
# que contemple las siguientes actividades: 
# a. en la primera tabla hash la función hash debe ser sobre el tipo de Pokémon, en la segunda
# tabla la función hash deberá utilizar el ultimo dígito del número del Pokémon como clave y la tercera sera en base  a su nivel repartiéndolos en 10 posiciones dentro de la tabla; 
# b. debe utilizar tablas hash abiertas con listas como estructura secundaria;
# c. si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que indiquen estos tipos;
# d. deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre, tipo/s, nivel.
# e. mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9;
# f. mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10;
# g. mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo

class Pokemon:
    def __init__(self, number, name, types, level):
        self.number = number
        self.name = name
        self.types = types
        self.level = level

    def __repr__(self):
        return f"Pokemon({self.number}, {self.name}, {self.types}, {self.level})"

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key, pokemon):
        index = self.hash_function(key)
        self.table[index].append(pokemon)

    def hash_function(self, key):
        raise NotImplementedError("Please implement this method in the subclass")

    def search(self, condition):
        result = []
        for bucket in self.table:
            for pokemon in bucket:
                if condition(pokemon):
                    result.append(pokemon)
        return result

class TypeHashTable(HashTable):
    def hash_function(self, key):
        return hash(key) % self.size

class LastDigitHashTable(HashTable):
    def hash_function(self, key):
        return key % 10

class LevelHashTable(HashTable):
    def hash_function(self, key):
        return key // 10 % self.size

class PokemonDatabase:
    def __init__(self):
        self.type_table = TypeHashTable(10)
        self.last_digit_table = LastDigitHashTable(10)
        self.level_table = LevelHashTable(10)

    def add_pokemon(self, number, name, types, level):
        pokemon = Pokemon(number, name, types, level)
        for type_ in types:
            self.type_table.insert(type_, pokemon)
        self.last_digit_table.insert(number, pokemon)
        self.level_table.insert(level, pokemon)

    def pokemons_by_last_digits(self, digits):
        return self.last_digit_table.search(lambda p: p.number % 10 in digits)

    def pokemons_by_level_multiples(self, multiples):
        return self.level_table.search(lambda p: any(p.level % m == 0 for m in multiples))

    def pokemons_by_types(self, types):
        result = []
        for type_ in types:
            result.extend(self.type_table.search(lambda p: type_ in p.types))
        return result

db = PokemonDatabase()

db.add_pokemon(3, "Venusaur", ["Planta", "Veneno"], 32)
db.add_pokemon(7, "Squirtle", ["Agua"], 15)
db.add_pokemon(9, "Blastoise", ["Agua"], 36)
db.add_pokemon(12, "Butterfree", ["Bicho", "Volador"], 10)
db.add_pokemon(25, "Pikachu", ["Eléctrico"], 22)
db.add_pokemon(55, "Golduck", ["Agua"], 25)
db.add_pokemon(87, "Dewgong", ["Agua", "Hielo"], 34)
db.add_pokemon(100, "Voltorb", ["Eléctrico"], 20)
db.add_pokemon(115, "Kangaskhan", ["Normal"], 35)
db.add_pokemon(136, "Flareon", ["Fuego"], 40)

print("Pokémons cuyos números terminan en 3, 7 y 9:")
print(db.pokemons_by_last_digits([3, 7, 9]))

print("\nPokémons cuyos niveles son múltiplos de 2, 5 y 10:")
print(db.pokemons_by_level_multiples([2, 5, 10]))

print("\nPokémons de los tipos Acero, Fuego, Eléctrico, Hielo:")
print(db.pokemons_by_types(["Acero", "Fuego", "Eléctrico", "Hielo"]))
