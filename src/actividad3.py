'''Ejercicio 3.1.3: Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.'''#funcion de la definicion
# definicion de la funcion

def crear_resultado(asignatura,nota):
    notas=[]
    for nota in notas:
        if nota<11 and nota >=0:
            notas.append(nota)
        return notas
    mensaje="tu nota en "+str(asignatura)+" es un "+str(nota)
    return mensaje

if __name__=="__main__":
    # entrada
    asignaturas=["matematicas","fisica","quimica","historia","lengua"]
    # procesamiento
    for asignatura in asignaturas:
        nota=int(input("introduce tu nota de "+str(asignatura)+": "))
    for asignatura in asignaturas:
        mensaje=crear_resultado(asignatura,nota)
        # salida
        print(mensaje)
