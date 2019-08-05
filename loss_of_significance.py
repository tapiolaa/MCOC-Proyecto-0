from numpy import *
from matplotlib import pyplot as plt
import math

m = 999999999999

#Funcion comun para ver lo que ocurre con el limite. Al momento de usar un numero muy negativo
#del orden de 10*10^7 el limite se va a 0, mientras que durante todos los numeros menores a este
#el limite era -0.25. Esto ocurre ya que se pierde significancia dado que el computador maneja
#alrededor de 23 decimales solamente.
def f(x):
	li=[]
	for i in x:
		a = i*(sqrt(4*(i**2)+1)+2*i)
		li.append(a)
	return li

#Para solucionar este problema, se trabaja la funcion anterior de manera de volverla mas simple
#para el computador. Esto se logra factorizando la funcion, multiplicando arriba y abajo por 
#la expresion que esta dentro del primer parentesis, pero con el signo de 2*i cambiado, es decir,
#-2*i. La expresion final queda como se detalla a continuacion:

def g(x):
	li=[]
	for i in x:
		a = i/(sqrt(4*(i**2)+1)-2*i) # cabe mencionar que esta funcion es equivalente a la funcion
		#previamente definida tal como se puede apreciar en el primer grafico a plotear.
		li.append(a)
	return li

lis = []
i = -1000
while i < 0:
	lis.append(i)
	i+=1
l1 = [-1,-10,-100,-1000,-10000,-1000000,-10000000,-100000000,-1000000000]
#l2 = [0.1,0.01,0.001,0.0001,0.00001,0.000001,0.0000001,0.00000001,0.000000001]

plt.plot(f(lis), label='f(x)')
plt.plot(g(lis), label='g(x)') #f y g equivalentes
plt.legend(loc='upper left')
plt.show()
plt.plot(f(l1), label='tendiendo a -inf')
plt.plot(g(l1), label='tendiendo a -inf')
#plt.plot(f(l2), label='tendiendo a 0')
#plt.plot(g(l2), label='tendinedo a 0')
plt.xlabel('Potencias de 10')
plt.legend(loc='upper')
plt.show()