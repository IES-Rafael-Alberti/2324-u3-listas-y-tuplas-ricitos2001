'''Ejercicio 3.1.4: Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.'''
# definicion de la funcion
def crear_listaloteria(lista):
    numero= len(lista)
    listafinal=lista
    for i in range (numero-1):
        for j in range(numero-1-i):
            if lista[j] > lista[j+1] :
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return listafinal
if __name__=="__main__":
    # entrada
    lista=[]
    while len(lista)<8:
        numeros = int(input("introduce un numero: "))
        lista.append(numeros)
        # procesamiento
    listafinal=crear_listaloteria(lista)
    #salida
    print(listafinal)
        