
import math # Importamos la libreria math
def expo(x): # Hacemos una función con el exponencial
    return  math.exp(x) 
def factorial(n : int ): # Usamos el factorial 
    p = 1
    for i in range(1,n+1):
        p *= i
    return p
def seriemc(x,n): # Se hace con la serie Maclaurin la aproximación
    m=0
    for i in range(n+1):
        m += (x**i)/factorial(i)
    return m

x=float(input("ingresar x: ")) # Se pide el valor de x
n=int(input("ingresar cantidad de las serie de Maclaurin : ")) #Se pide la cantidad de la serie
print(expo(x)) # Se imprime el valor "real"
print(seriemc(x,n)) # Se imprime la aproximación