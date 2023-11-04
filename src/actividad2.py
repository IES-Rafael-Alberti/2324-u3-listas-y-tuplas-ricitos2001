'''Ejercicio 3.1.2: Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista.'''
# definicion de la funcion
def crear_lista(asignatura):
    mensaje="yo estudio "+str(asignatura)
    return (mensaje)

if __name__=="__main__":
    # entrada
    asignaturas=["matematicas","fisica","quimica","historia","lengua"]
    # procesamiento
    for asignatura in asignaturas:
        mensaje=crear_lista(asignatura)
        # salida
        print(mensaje)
