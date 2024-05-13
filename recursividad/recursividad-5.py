# 5. Desarrollar una función que permita convertir un número romano en un número decimal.
def recursiva(numero):
    romano = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    if len(numero) == 0:
        return 0
    
    if len(numero) == 1:
        return romano[numero[0]]
    
    if romano[numero[0]] < romano[numero[1]]:
        return romano[numero[1]] - romano[numero[0]] + recursiva(numero[2:])
    else:
        return romano[numero[0]] + recursiva(numero[1:])#el : permite saltar a la otra secuencia (+1)
print(recursiva("XXI"))