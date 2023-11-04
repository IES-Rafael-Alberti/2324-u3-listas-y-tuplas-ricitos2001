'''Ejercicio 3.1.7: Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.'''
# definicion de la funcion
def crear_alfabeto(abecedario):
    for i in range(len(abecedario)-1,-1,-1):
        if i %3==0:
            abecedario.pop(i)
    return abecedario

if __name__ == '__main__':
    # entrada
    abecedario= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    #  procesamiento
    alfabeto=crear_alfabeto(abecedario)
    # salida
    print(alfabeto)

