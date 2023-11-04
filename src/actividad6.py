'''Ejercicio 3.1.6: Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.'''
# definicion de la funcion
def crear_recuperaciones(asignaturas):
    mensaje="asignaturas que recuperar: "+str(asignaturas)
    return mensaje

if __name__ == '__main__':
    asignaturas = ["matematicas","fisica","quimica","historia","lengua"]
    notas = []
    for asignatura in asignaturas:
        nota=float(input("introduce tu nota de "+str(asignatura)+": "))
        if nota >= 5:
            notas.append(asignatura)
    for i in notas:
        asignaturas.remove(i)
    mensaje=crear_recuperaciones(asignaturas)
    print(mensaje)
