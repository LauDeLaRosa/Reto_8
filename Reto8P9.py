import math # Importamos la libreria math
def seno(x): # Hacemos una función con el seno
    return  math.sin(x) 
def factorial(n : int ): # Usamos el factorial 
    p = 1
    for i in range(1,n+1):
        p *= i
    return p
def seriemc(x,n): # Se hace con la serie Maclaurin la aproximación
    m=0
    for i in range(n+1):
        m += ((-1)**i)*(x**((2*i)+1))/(factorial((2*i)+1))
    return m

x=float(input("ingresar x: ")) # Se pide el valor de x
n=int(input("ingresar cantidad de las serie de Maclaurin : ")) #Se pide la cantidad de la serie
print(seno(x)) # Se imprime el valor "real"
print(seriemc(x,n)) # Se imprime la aproximación