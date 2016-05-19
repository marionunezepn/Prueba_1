def lista1():
	x=[0,0,0]
	for i in range (len(x)):
		x[i]=int(input('ingrese numero vector 1: '))
	return x;
def lista2():
	y=[0,0,0]
	for i in range (len(x)):
		y[i]=int(input('ingrese numero vector2: '))
	return y;
def suma(x,y):
	r=[0,0,0]
	for i in range(len(r)):
		r[i]=x[i]+y[i]
	return r

def ingresar():
	continuar = 1
	contador = 0
	suma = 0
	while (continuar==1):
		x=int(input('ingrese un numero: '))
		suma=suma+x
		if(x==0):
			continuar=0
		contador=contador+1
	promedio=suma/(contador-1)
	return promedio
print('------menu-----')
print('1.-Suma de vectores')
print('2.-Promedio de numeros')
print('3.-Dividir un archivo')
print('4.-Salir')
print('________________')	
opcion = int(input('ingrese una opcion: '))
if(opcion==1):
	x=lista1()
	y=lista2()
	print(x)
	print(y)
	print(suma(x,y))
if(opcion==2):
	valor=ingresar()
	print (valor)
