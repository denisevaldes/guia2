#Escriba un programa que pida al usuario dos palabras, y se indique cuál de ellas es la más larga y por
#cuántas letras lo es.

primera_palabra = input("ingrese una palabra: ")
segunda_palabra = input("ingrese una segunda palabra: ")

largo_1 = len(primera_palabra)
largo_2 = len(segunda_palabra)

if largo_1 > largo_2:
    print("la primera palabra es mayor")
    resta = largo_1 - largo_2 
    print("la diferencia es de: ", resta)
elif largo_2 > largo_1:
    print("la segunda palabra es mayor")
    resta = largo_2 - largo_1
    print("la diferencia es de: ", resta)
#cuando la palabra 1 es mayor, se imprime el else tambien   
else: 
    print("las palabras tienen el mismo largo")        