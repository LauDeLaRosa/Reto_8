n=int(input("Ingresa un numero natural mayor o igual a 2:")) #Se define la variable
if n%2==0:#Si el residuo de la variable es igual a cero
    n=n #La variable va a quedar igual
else: #si no pasa lo anterior
 n=n-1 #se le resta 1 a la variable

for i in range(n,1,-2): #Se determina el rango donde va a ser de la variable hasta 2, restando 2
   print(i) #Se imprime el listado

