#Dada un String que se forman de manera aleatoria, devuelva una nueva lista cuyo contenido sea igual
#a la original pero de modo invertida.

texto = "estas como hola"
separar_texto = texto.split()

for i in range(len(separar_texto)-1,-1,-1):
    reversa = separar_texto[i]
    
