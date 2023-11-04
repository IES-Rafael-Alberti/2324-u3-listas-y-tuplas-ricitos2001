'''Ejercicio 3.1.1: Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.'''
#funcion de la definicion
def crear_lista(asignaturas):
    mensaje=asignaturas
    return mensaje

if __name__=="__main__":
    #entrada
    asignaturas=["matematicas","fisica","quimica","historia","lengua"]
    #procesamiento
    mensaje=crear_lista(asignaturas)
    #salida
    print(mensaje)
