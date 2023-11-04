'''Ejercicio 3.1.8: Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.'''
# como deberia ser mi version
# como es el programa
def verificar_palindromo(palabra):
    palabrainvertida = palabra
    palabra = list(palabra)
    palabrainvertida = list(palabrainvertida)
    palabrainvertida.reverse()
    if palabra==palabrainvertida:
        mensaje="es un palindromo"
        return mensaje
    else:
        mensaje="no es un palindromo"
        return mensaje

if __name__ == '__main__':
    palabra=input('introduce una palabra: ')
    mensaje=verificar_palindromo(palabra)
    print(mensaje)
