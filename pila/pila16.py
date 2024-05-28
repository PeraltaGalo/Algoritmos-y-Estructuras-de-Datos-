# 16. Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
# strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que

# permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en am-
# bos episodios.
class Stack:# clase de pila 

    def __init__(self):
        self.items = []#inicializacion de pila

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

# Crear pilas con personajes de cada episodio
episode_v_stack = Stack()
episode_vii_stack = Stack()

# Agregar personajes del episodio V "The Empire Strikes Back"
episode_v_characters = ["Luke Skywalker", "Darth Vader", "Han Solo", "Leia Organa", "Yoda"]
for character in episode_v_characters:
    episode_v_stack.push(character)

# Agregar personajes del episodio VII "The Force Awakens"
episode_vii_characters = ["Han Solo", "Leia Organa", "Luke Skywalker", "Kylo Ren", "Rey"]
for character in episode_vii_characters:
    episode_vii_stack.push(character)

# Encontrar la intersección de ambas pilas
intersection = []

# Usar conjuntos para encontrar la intersección
episode_v_set = set(episode_v_stack)
episode_vii_set = set(episode_vii_stack)

intersection = list(episode_v_set.intersection(episode_vii_set))

# Mostrar los personajes que aparecen en ambos episodios
print("Personajes en ambos episodios (V y VII):")
for character in intersection:
    print(character)
