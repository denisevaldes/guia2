# Denise Valdes
# Ejercicio 6
# Cree un programa que permita concatenar los datos o palabras ingresadas por un usuario. El ingreso
# de palabras debe estar controlado por un ciclo y cuando se escriba la palabra fin termine la ejecución
# y se muestren todos los datos ingresados de forma concatenada.

# se crean dos variables
palabra = None
juntar = ""

#mientras palabra sea diferente de fin, el ciclo se repetira
while palabra != "fin":
    # se le pide al usuario ingresar una palabra
    palabra = input("ingrese una palabra para concatenar: ")
    # en variable juntar se van concatenando las palabras con +
    juntar += " " + palabra 
    print("la frase formada es:", juntar) 