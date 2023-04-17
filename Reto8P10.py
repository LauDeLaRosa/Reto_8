import math # Importamos la libreria math
def arctan(x): # Hacemos una función con el arcotangente
    return math.atan(x) 
def seriemc(x,n): # Se hace con la serie Maclaurin la aproximación
    m=0
    for i in range(n+1):
        m += ((-1)**i)*(x**((2*i)+1))/((2*i)+1)
    return m
x=float(input("ingresar x entre -1 y 1: ")) # Se pide el valor de x entre -1 y 1
n=int(input("ingresar cantidad de las serie de Maclaurin : ")) #Se pide la cantidad de la serie
print(arctan(x)) # Se imprime el valor "real"
print(seriemc(x,n))  # Se imprime la aproximación