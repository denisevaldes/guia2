# Denise valdés
# Ejercicio 4
# Extienda el programa anterior para logre encontrar palabras dentro de un texto, sin importar si están
# escritas en diferente combinación de mayúsculas/minúsculas.

frase = input("ingrese una frase: ")
# se utiliza lower para que todas las letras se vuelvan minusculas 
frase_lower = frase.lower()
palabra = input("ingrese una palabra a buscar dentro de la frase:")
palabra_lower = palabra.lower()
# se realiza una busqueda utilizando find y las nuevas variables en donde
# todas las letras de los string son minusculas 
busqueda = frase_lower.find(palabra_lower)

if busqueda == -1:
    print("la palabra no se encuentra en la frase")
else: 
    print("la palabra si se encuentra en la frase")    