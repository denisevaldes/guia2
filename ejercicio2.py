# El siguiente String está encriptado 
# de mala manera a pesar que de todos modos sigue siendo un mensaje
# incomprensible. Idea un método para extraer el 
# mensaje y guárdalo en una variable llamada mensaje
# y mostrar el valor de la variable en pantalla.
# string = ¡XeXgXaXsXsXeXmX XtXeXrXcXeXsX XaX XsXiX XsXiXhXt”

string = "¡XeXgXaXsXsXeXmX XtXeXrXcXeXsX XaX XsXiX XsXiXhXt"
mensaje = string.replace("X","")
#hola = "".join(reversed(mensaje))
print(mensaje[::-1])
#[inicio:fin:salto] por lo que no dije donde era el inicio
#solo indique donde queria terminar 
#print(mensaje[-1::])


#"""
#	Invertir lista o arreglo en Python, pero asignar
#	el resultado a otra lista
#	@author parzibyte
#"""
#lenguajes = ["Go", "Rust", "C", "JavaScript", "PHP"]
##print("La lista es: ", lenguajes)
#lenguajes_invertidos = lenguajes[::-1]
#print("Lenguajes invertidos son:", lenguajes_invertidos)
