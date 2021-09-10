# Denise valdes
# ejercicio 2
# El siguiente String está encriptado 
# de mala manera a pesar que de todos modos sigue siendo un mensaje
# incomprensible. Idea un método para extraer el 
# mensaje y guárdalo en una variable llamada mensaje
# y mostrar el valor de la variable en pantalla.
# string = ¡XeXgXaXsXsXeXmX XtXeXrXcXeXsX XaX XsXiX XsXiXhXt”


string = "¡XeXgXaXsXsXeXmX XtXeXrXcXeXsX XaX XsXiX XsXiXhXt"
#se usa replace para remplazar todas las X por espacios vacios
mensaje = string.replace("X","")
# se imprime el mensaje con [::-1], no se indica el comienzo ni el final 
# para que tome todo el str y se agrega un -1 al final para que se imprima
# de atrás hacia adelante
print(mensaje[::-1])



