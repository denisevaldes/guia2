#Escriba un programa que indique si una palabra existe dentro de un texto. La palabra como la oración
#serán ingresadas por el usuario.

frase = input("ingrese una frase: ")
palabra = input("ingrese una palabra a buscar dentro de la frase:")

busqueda = frase.find(palabra)

if busqueda == -1:
    print("la palabra no se encuentra en la frase")
else: 
    print("la palabra si se encuentra en la frase")    