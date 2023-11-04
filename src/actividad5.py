'''Ejercicio 3.1.5: Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.'''
# como deberia ser mi version
# como es el programa
def crear_listainversa(lista):
    numero= len(lista)
    listainversa=lista
    for i in range (numero-1):
        for j in range(numero-1-i):
            if lista[j] < lista[j+1] :
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return listainversa

if __name__=="__main__":
    lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    listainversa=crear_listainversa(lista)
    print(listainversa)