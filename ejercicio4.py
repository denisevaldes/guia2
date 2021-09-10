#Extienda el programa anterior para logre encontrar palabras dentro de un texto, sin importar si están
#escritas en diferente combinación de mayúsculas/minúsculas.

frase = input("ingrese una frase: ")
frase_lower = frase.lower()
palabra = input("ingrese una palabra a buscar dentro de la frase:")
palabra_lower = palabra.lower()
busqueda = frase_lower.find(palabra_lower)

if busqueda == -1:
    print("la palabra no se encuentra en la frase")
else: 
    print("la palabra si se encuentra en la frase")    