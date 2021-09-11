#Cree un programa que permita concatenar los datos o palabras ingresadas por un usuario. El ingreso
#de palabras debe estar controlado por un ciclo y cuando se escriba la palabra fin termine la ejecución
#y se muestren todos los datos ingresados de forma concatenada.

palabra = None
juntar = ""

while palabra != "fin":
    palabra = input("ingrese una palabra para concatenar: ")
    juntar = juntar + " " + palabra 
    print("la frase formada es:", juntar) 