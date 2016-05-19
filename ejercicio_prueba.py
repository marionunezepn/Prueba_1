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
print('1')
print('2.-promedio de numeros')	
opcion = int(input('ingrese una opcion: '))
if(opcion==2):
	valor=ingresar()
	print (valor)