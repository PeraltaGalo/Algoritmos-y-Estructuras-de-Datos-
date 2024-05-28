class Character:
    def __init__(self, name, movies):
        self.name = name
        self.movies = movies

class Stack:# clase de pila 
    
    def __init__(self):
        self.items = [] #inicializando pila 

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

# Crear la pila y añadir personajes
mcu_stack = Stack()

characters = [
    Character("Iron Man", 10),
    Character("Captain America", 11),
    Character("Thor", 9),
    Character("Hulk", 7),
    Character("Black Widow", 8),
    Character("Hawkeye", 6),
    Character("Rocket Raccoon", 4),
    Character("Groot", 4),
    Character("Doctor Strange", 5),
    Character("Black Panther", 4)
]

for character in characters:
    mcu_stack.push(character)

# a. Determinar la posición de Rocket Raccoon y Groot
def find_position(stack, name):
    position = 1
    for character in stack:
        if character.name == name:
            return position
        position += 1
    return -1  # Si el personaje no se encuentra

position_rocket = find_position(mcu_stack, "Rocket Raccoon")
position_groot = find_position(mcu_stack, "Groot")

print(f"Rocket Raccoon está en la posición: {position_rocket}")
print(f"Groot está en la posición: {position_groot}")

# b. Determinar los personajes que participaron en más de 5 películas
def characters_more_than_n_movies(stack, n):
    result = []
    for character in stack:
        if character.movies > n:
            result.append((character.name, character.movies))
    return result

characters_5_plus = characters_more_than_n_movies(mcu_stack, 5)

print("Personajes que participaron en más de 5 películas:")
for name, movies in characters_5_plus:
    print(f"{name} - {movies} películas")

# c. Determinar en cuántas películas participó Black Widow
def movies_by_character(stack, name):
    for character in stack:
        if character.name == name:
            return character.movies
    return 0

black_widow_movies = movies_by_character(mcu_stack, "Black Widow")

print(f"Viuda Negra participó en {black_widow_movies} películas")

# d. Mostrar todos los personajes cuyos nombres empiezan con C, D y G
def characters_starting_with(stack, letters):
    result = []
    for character in stack:
        if character.name[0] in letters:
            result.append(character.name)
    return result

characters_cdg = characters_starting_with(mcu_stack, {'C', 'D', 'G'})

print("Personajes cuyos nombres empiezan con C, D y G:")
for name in characters_cdg:
    print(name)
