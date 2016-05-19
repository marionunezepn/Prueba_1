def ingresar():
	continuar = 1
	contador = 0
	while (continuar==1):
		x=int(input('ingrese un numero: '))
		if(x==0):
			continuar=0
		contador=contador+1
ingresar()