# Lista de dinosaurios
dinosaurios = [
    {
        "nombre": "Tyrannosaurus Rex",
        "especie": "Theropoda",
        "peso": "7000 kg",
        "descubridor": "Barnum Brown",
        "ano_descubrimiento": 1902
    },
    {
        "nombre": "Triceratops",
        "especie": "Ceratopsidae",
        "peso": "6000 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1889
    },
    {
        "nombre": "Velociraptor",
        "especie": "Dromaeosauridae",
        "peso": "15 kg",
        "descubridor": "Henry Fairfield Osborn",
        "ano_descubrimiento": 1924
    },
    {
        "nombre": "Brachiosaurus",
        "especie": "Sauropoda",
        "peso": "56000 kg",
        "descubridor": "Elmer S. Riggs",
        "ano_descubrimiento": 1903
    },
    {
        "nombre": "Stegosaurus",
        "especie": "Stegosauridae",
        "peso": "5000 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1877
    },
    {
        "nombre": "Spinosaurus",
        "especie": "Spinosauridae",
        "peso": "10000 kg",
        "descubridor": "Ernst Stromer",
        "ano_descubrimiento": 1912
    },
    {
        "nombre": "Allosaurus",
        "especie": "Theropoda",
        "peso": "2000 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1877
    },
    {
        "nombre": "Apatosaurus",
        "especie": "Sauropoda",
        "peso": "23000 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1877
    },
    {
        "nombre": "Diplodocus",
        "especie": "Sauropoda",
        "peso": "15000 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1878
    },
    {
        "nombre": "Ankylosaurus",
        "especie": "Ankylosauridae",
        "peso": "6000 kg",
        "descubridor": "Barnum Brown",
        "ano_descubrimiento": 1908
    },
    {
        "nombre": "Parasaurolophus",
        "especie": "Hadrosauridae",
        "peso": "2500 kg",
        "descubridor": "William Parks",
        "ano_descubrimiento": 1922
    },
    {
        "nombre": "Carnotaurus",
        "especie": "Theropoda",
        "peso": "1500 kg",
        "descubridor": "José Bonaparte",
        "ano_descubrimiento": 1985
    },
    {
        "nombre": "Styracosaurus",
        "especie": "Ceratopsidae",
        "peso": "2700 kg",
        "descubridor": "Lawrence Lambe",
        "ano_descubrimiento": 1913
    },
    {
        "nombre": "Therizinosaurus",
        "especie": "Therizinosauridae",
        "peso": "5000 kg",
        "descubridor": "Evgeny Maleev",
        "ano_descubrimiento": 1954
    },
    {
        "nombre": "Pteranodon",
        "especie": "Pterosauria",
        "peso": "25 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1876
    },
    {
        "nombre": "Quetzalcoatlus",
        "especie": "Pterosauria",
        "peso": "200 kg",
        "descubridor": "Douglas A. Lawson",
        "ano_descubrimiento": 1971
    },
    {
        "nombre": "Plesiosaurus",
        "especie": "Plesiosauria",
        "peso": "450 kg",
        "descubridor": "Mary Anning",
        "ano_descubrimiento": 1824
    },
    {
        "nombre": "Mosasaurus",
        "especie": "Mosasauridae",
        "peso": "15000 kg",
        "descubridor": "William Conybeare",
        "ano_descubrimiento": 1829
    },
]


def contador_especie(dinosaurio):
    cont = set(dino['especie'] for dino in dinosaurio)
    return len(cont) 
contador = contador_especie(dinosaurios)
print("\nCantidad de especies:", contador)


def contar_descubridores(dinosaurio):
    des = set(dino["descubridor"] for dino in dinosaurio)
    return len(des)
descubridores = contar_descubridores(dinosaurios)
print("\nCantidad de descubridores:", descubridores)


def dinosaurioscont(dinosaurios):
    return [dino for dino in dinosaurios if dino["nombre"].startswith("T")]
cont = dinosaurioscont(dinosaurios)
print("\nDinosaurios que empiezan con 'T':", cont)


def cambio_integer(dinosaurio):
    for dino in dinosaurio:
        dino['peso'] = int(dino['peso'].replace(" kg", ""))
cambio_integer(dinosaurios)


def menos_275kg(dinosaurio):
    return [dino for dino in dinosaurio if dino["peso"] < 275]
print("\nDinosaurios con peso menor a 275 kg:", menos_275kg(dinosaurios))


def pila_a_q_s(dinosaurio):
    return [dino for dino in dinosaurio if dino["nombre"][0] in ["A", "Q", "S"]]
print("\nDinosaurios que empiezan con 'A', 'Q' o 'S':", pila_a_q_s(dinosaurios))
