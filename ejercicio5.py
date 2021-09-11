# Denise valdés
# Ejercicio 5
# Escriba un programa que pida al usuario dos palabras, y se indique cuál de ellas es la más larga y por
# cuántas letras lo es.

# se le pide al usuario ingresar dos palabras
primera_palabra = input("ingrese una palabra: ")
segunda_palabra = input("ingrese una segunda palabra: ")
#se ocupa len para saber el largo de las palabras
largo_1 = len(primera_palabra)
largo_2 = len(segunda_palabra)
# se compara largo_1 y largo_2 para ver cual es mayor
# luego se restan los largos de las palabras para saber
# por cuanto es la diferencia
if largo_1 > largo_2:
    print("la primera palabra es mayor")
    resta = largo_1 - largo_2 
    print("la diferencia es de: ", resta)
elif largo_2 > largo_1:
    print("la segunda palabra es mayor")
    resta = largo_2 - largo_1
    print("la diferencia es de: ", resta)  
else: 
    print("las palabras tienen el mismo largo")        