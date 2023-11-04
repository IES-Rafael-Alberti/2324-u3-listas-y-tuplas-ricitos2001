'''Ejercicio 3.1.12: Escribir un programa que almacene las matrices A=(123456) y B=(-100111) en una lista y muestre por pantalla su producto. Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.'''
# definicion de la funcion
def producto_vector(a,b,resultado):
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                resultado[i][j]+= a[i][k] * b[k][j]
    for i in range(len(resultado)):
        resultado[i] = tuple(resultado[i])
    resultadofinal= tuple(resultado)
    return resultadofinal

if __name__ == '__main__':
    # entrada
    a=((1,2,3),(4,5,6))
    b=((-1,0),(0,1),(1,1))
    resultado = [[0,0],[0,0]]
    # procesamiento
    resultadofinal=producto_vector(a,b,resultado)
    for resultadofinal in resultado:
        # salida
        print (resultadofinal)
