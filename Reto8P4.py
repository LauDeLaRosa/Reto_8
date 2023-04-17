from math import factorial #Se importa la funcion de factorial
n=int(input("Ingrese un numero natural:")) #Se define la variable
for i in range(1,n+1): #Se determina el rango
    print(i,factorial(i), sep=":") #Se imprime el listado de numeros junto con su factorial