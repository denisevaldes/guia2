#Extienda el programa anterior para logre encontrar palabras dentro de un texto, sin importar si están
#escritas en diferente combinación de mayúsculas/minúsculas.

frase = input("ingrese una frase: ")
palabra = input("ingrese una palabra a buscar dentro de la frase:")

busqueda = frase.find(palabra)

if busqueda == -1:
    print("la palabra no se encuentra en la frase")
else: 
    print("la palabra si se encuentra en la frase")    