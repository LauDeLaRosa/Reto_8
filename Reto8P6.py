def potencia(n,b): # Definimos la función
    p = 1 # Definimos una variable
    for i in range(1,n+1): # Hacer el rango hasta n
        p *= b 
    return p
b = float(input("base: ")) # Pedir la base
n=int(input("ingresar n: ")) # Pedir la n a la que se eleva la base
print(potencia(n,b)) # Se imprime el resultado