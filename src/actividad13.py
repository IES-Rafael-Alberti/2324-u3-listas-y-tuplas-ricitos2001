'''Ejercicio 3.1.13: Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.'''
# definicion de la funcion
def crear_sumatorio(numeros):
    suma=sum(numeros)
    return suma

def crear_contador(numeros):
    contador=len(numeros)
    return contador

def crear_media(suma,contador):
    media=suma/contador
    return media

def crear_desviacion(numeros,media):
    variacion = sum((x - media) ** 2 for x in numeros)
    desviaciontipica=(variacion/len(numeros))**0.5
    return desviaciontipica

if __name__=="__main__":
    # entrada
    introducirnumero=input("introduce una serie de numeros separados por comas: ")
    numeros = []
    for numero in introducirnumero.split(','):
        numeros.append(int(numero))
    # procesamiento
    suma=crear_sumatorio(numeros)
    contador=crear_contador(numeros)
    media=crear_media(suma,contador)
    desviaciontipica=crear_desviacion(numeros,media)
        # salida
    print (suma)
    print(contador)
    print (media)
    print (desviaciontipica)
# desviacion tipica √(((n1-m)2+(n2-m)2)/m)