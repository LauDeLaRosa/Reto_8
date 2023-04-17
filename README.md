# ¿Cuándo se va a acabar el semestre? (Reto 8)
## Ejercicio
### Qué se genera con range(-2)?
Conjunto vacio.
## Problema #1
Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
```python
range(1, 101) #Establezco el rango
for i in range (1, 101): #Se establece que la variable estará en este rango
    print (i,i**2, sep=":") #Se arrojará el listado de los números y su cuadrado
```
## Problema #2
Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
```python
range (1,1000,2) #Se establece el rango para que vaya de 2 en 2 desde 1 hasta 999
for i in range(1,1000,2): #Se establece que la variable irá en ese rango
    print (i) #Se imprime el listado de números

range (2,1001,2)#Se establece el rango para que vaya de 2 en 2 de 2 hasta 1000
for i in range (2,1001,2):#Se establece que la variable está en este rango
    print(i)#Se imprime el listado de números
```

## Problema #3
Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
```python
n=int(input("Ingresa un numero natural mayor o igual a 2:")) #Se define la variable
if n%2==0:#Si el residuo de la variable es igual a cero
    n=n #La variable va a quedar igual
else: #si no pasa lo anterior
 n=n-1 #se le resta 1 a la variable

for i in range(n,1,-2): #Se determina el rango donde va a ser de la variable hasta 2, restando 2
   print(i) #Se imprime el listado
```   
   
## Problema #4
Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
```python
from math import factorial #Se importa la funcion de factorial
n=int(input("Ingrese un numero natural:")) #Se define la variable
for i in range(1,n+1): #Se determina el rango
    print(i,factorial(i), sep=":") #Se imprime el listado de numeros junto con su factorial
```

## Problema #5
Calcular el valor de 2 elevado a la potencia n usando ciclos for.
```python
n=int(input("Ingrese un numero entero:")) #Se define la variable
for i in range(0,n+1): #Se define el rango
    print(2**i) #Se imprime el listado de 2 elevado desde cero hasta n
```

## Problema #6
Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for.
```python
def potencia(n,b): # Definimos la función
    p = 1 # Definimos una variable
    for i in range(1,n+1): # Hacer el rango hasta n
        p *= b 
    return p
b = float(input("base: ")) # Pedir la base
n=int(input("ingresar n: ")) # Pedir la n a la que se eleva la base
print(potencia(n,b)) # Se imprime el resultado
```

## Problema #7
Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
```python
for i in range(1,10):#Se define el rango del 1 al 9
    for n in range(0,11):#Se define el rango del 1 al 10
        print(i,"*",n,"=", i*n)#Se imprimen las tablas del 1 al 9 
```

## Problema #8
Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
```python

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
```

## Problema #9
Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
```python
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
```

## Problema #10
Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
```python
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
```

