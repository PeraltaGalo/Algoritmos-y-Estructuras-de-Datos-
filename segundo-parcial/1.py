
# 1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
# de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
# tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
# a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
# b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
# último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
# mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
# caracteres–;
# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
# además un listado por nivel por nombre;
# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
# f) Determina cuantos Pokémons hay de tipo eléctrico y acero. 2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar

# main.py

from pokemon import AdministradorPokemon
pokemons = [
    {
        "nombre": "Pikachu",
        "nivel": 35,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Pikachu",
        "nivel": 20,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Charizard",
        "nivel": 40,
        "tipo": "Fuego",
        "subtipo": "Volador"
    },
    {
        "nombre": "Bulbasaur",
        "nivel": 30,
        "tipo": "Planta",
        "subtipo": "Veneno"
    },
    {
        "nombre": "Starmie",
        "nivel": 30,
        "tipo": "Agua",
        "subtipo": "Psíquico"
    },
    {
        "nombre": "Psyduck",
        "nivel": 25,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Gyarados",
        "nivel": 35,
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "nombre": "Onix",
        "nivel": 38,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Geodude",
        "nivel": 28,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Vulpix",
        "nivel": 20,
        "tipo": "Fuego",
        "subtipo": None
    },
    {
        "nombre": "Blastoise",
        "nivel": 50,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Umbreon",
        "nivel": 45,
        "tipo": "Siniestro",
        "subtipo": None
    },
    {
        "nombre": "Nidoking",
        "nivel": 40,
        "tipo": "Veneno",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Dragonite",
        "nivel": 55,
        "tipo": "Dragón",
        "subtipo": "Volador"
    },
    {
        "nombre": "Aerodactyl",
        "nivel": 52,
        "tipo": "Roca",
        "subtipo": "Volador"
    }
]

# Crear el administrador de Pokémon
administrador = AdministradorPokemon(pokemons)

# a) Búsqueda por proximidad
print("Búsqueda por proximidad de 'bul':", administrador.buscar_por_nombre("bul"))

# b) Listar Pokémon de tipo agua
print("Pokémon de tipo Agua:", administrador.listar_por_tipo("agua"))

# c) Listar todos los Pokémon en orden ascendente por nivel y nombre
print("Listado de todos los Pokémon en orden:", administrador.listar_todos())

# d) Mostrar datos de Pokémon específicos
print("Datos de Pokémon específicos:", administrador.pokemons_especificos(["Jolteon", "Lycanroc", "Tyrantrum"]))

# e) Contar Pokémon de tipo eléctrico y acero
print("Cantidad de Pokémon Eléctricos:", administrador.contar_por_tipo("Eléctrico"))
print("Cantidad de Pokémon Acero:", administrador.contar_por_tipo("Acero"))  # Esto debería ser 0 según los datos.
