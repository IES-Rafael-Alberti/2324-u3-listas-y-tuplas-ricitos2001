'''Ejercicio 3.1.9: Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.'''
# como deberia ser mi version
def crear_lista(palabra,letra):
    contador = 0
    for i in palabra:
        if i == letra:
            contador+=1
    mensaje="la vocal "+str(letra)+" se encuentra "+str(contador)+" veces"
    return mensaje

if __name__=="__main__":
    # entrada
    palabra=input("introduce una palabra: ")
    letras=["a","e","i","o","u"]
    # procesamiento
    for letra in letras:
        mensaje=crear_lista(palabra,letra)
    # salida
        print(mensaje)
