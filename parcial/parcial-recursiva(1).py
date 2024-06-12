def listar_inverso(lista): #funcion del inverso 
    if len(lista) == 0:
        return []
    else:
        return [lista[-1]] + listar_inverso(lista[:-1])
vector=[] #vector sin cargar 
print(listar_inverso(vector))