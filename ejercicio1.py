# Denise valdés
# Ejercicio 1
# Dada un String que se forman de manera aleatoria, devuelva una nueva lista cuyo contenido sea igual
# a la original pero de modo invertida.

texto = "estas como hola"
separar_texto = texto.split()
# se crea for y se agrega -1 para ir decreciendo 
for i in range(len(separar_texto)-1,-1,-1):
    # se imprime el texto en reversa y se añade un espacio
    # para que las palabras se escriban hacia el lado
    print(separar_texto[i], end = " ")
    
