def creartxt(numero,texto):
	if(numero==1):
		archi=open('archivo1.txt','a')
		archi.write(texto)
		archi.close() 
		invertir(1)
	if(numero==2):
		archi=open('archivo2.txt','a')
		archi.write(texto)
		archi.close()
		invertir(2)
	if(numero==3):
		archi=open('archivo3.txt','a')
		archi.write(texto)
		archi.close()	
		invertir(3)	
def invertir(numero):
	if(numero==1):
		archi=open('archivo1.txt','r')
		linea=archi.read(100)
		cadena = linea
		var = ''
		for h in cadena:
			var = h + var
		ar=open('archivoivertido1.txt','a')
		ar.write(var)
		ar.close()
		archi.close()
	if(numero==2):
		archi=open('archivo2.txt','r')
		linea=archi.read(100)
		cadena = linea
		var = ''
		for h in cadena:
			var = h + var
		ar=open('archivoivertido2.txt','a')
		ar.write(var)
		ar.close()
		archi.close()
	if(numero==3):
		archi=open('archivo3.txt','r')
		linea=archi.read(100)
		cadena = linea
		var = ''
		for h in cadena:
			var = h + var
		ar=open('archivoivertido3.txt','a')
		ar.write(var)
		ar.close()
		archi.close()
 
def leertxt():
	contador=1
	archi=open('archivooriginal.txt','r')
	linea=archi.read(100)
	creartxt(1,linea)
	linea2=archi.read(100)
	creartxt(2,linea)
	linea3=archi.read(100)
	creartxt(3,linea)
	archi.close()
 
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
continuar=1
while(continuar==1):
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
	if(opcion==3):
		leertxt()
		print('Revisar los archivos .txt creados')
	if (opcion==4):
		continuar=2
	else:
		print('opcion incorrecta')


