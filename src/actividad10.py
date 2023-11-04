'''Ejercicio 3.1.10: Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios.'''
# definicion de la funcion
def crear_listaprecio(precios):
    numero=len(precios)
    lista=precios
    for i in range (numero-1):
        for j in range(numero-1-i):
            if precios[j] > precios[j+1] :
                precios[j], precios[j+1] = precios[j+1], precios[j]
    return lista


if __name__=="__main__":
    precios = [50, 75, 46, 22, 80, 65, 8]
    lista=crear_listaprecio(precios)
    print(lista)
