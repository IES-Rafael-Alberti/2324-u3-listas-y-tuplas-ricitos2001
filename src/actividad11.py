'''Ejercicio 3.1.11: Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.'''
# como deberia ser mi version
# como es el programa
def escalar_producto(vector1,vector2):
    producto = 0
    for i in range(len(vector1)):
        producto+= vector1[i]*vector2[i]
        mensaje="El producto final de "+str(vector1)+" y "+str(vector2)+" es "+str(producto)
    return mensaje

if __name__ == '__main__':
    vector1 = (1,2,3)
    vector2 = (-1,0,2)
    mensaje=escalar_producto(vector1, vector2)
    print(mensaje)