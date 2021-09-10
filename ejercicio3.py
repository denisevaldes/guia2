# Denise Valdés
# Ejercicio 3
# Escriba un programa que indique si una palabra existe dentro de un texto. La palabra como la oración
#serán ingresadas por el usuario.

frase = input("ingrese una frase: ")
palabra = input("ingrese una palabra a buscar dentro de la frase:")
#se utiliza find para saber si la palabra ingresada se encuentra en la frase
busqueda = frase.find(palabra)
# si el resultado de find es -1, la palabra no se encuentra en la frase
# otro resultado significaria que la palabra si se encuentra 
if busqueda == -1:
    print("la palabra no se encuentra en la frase")
else: 
    print("la palabra si se encuentra en la frase")    