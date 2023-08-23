import math

'''Cosseno: math.cos(x)
   Seno: math.sin(x)
   Tangente: math.tan(x)'''

while True:
	teste = input("Deseja testar o programa ou calcular? [T/C] ")

	print(" ")

	while True:

		if teste.lower() == "t":
			a, b, f = [2, 3, "math.sin(x) - x**2 + 4"]
			break
		elif teste.lower() == "c":
			a = float(input("Escreva o valor de 'a'       : "))
			b = float(input("Escreva o valor de 'b'       : "))
			f = input("Escreva a função             : ")
			print(" ")
			break
		else:
			print("Letra inválida! Use apenas 'T' ou 'C'.")
			print(" ")
			teste = input("Deseja testar o programa ou calcular? [T/C] ")
			print(" ")

	f1 = ""

	for j in range(len(f)):
		if f[j] == "x":
			f1 += str(a)
		else:
			f1 += f[j]

	ff1 = eval(str(f1))

	f2 = ""

	for j in range(len(f)):
		if f[j] == "x":
			f2 += str(b)
		else:
			f2 += f[j]

	ff2 = eval(str(f2))

	if ff1 * ff2 < 0:
		print("Existe raiz real no intervalo [%.2f,%.2f]." % (a,b))
	else:
		print("Não existe raiz real no intervalo [%.2f,%.2f]." % (a, b))

	print(" ")
	conn = input("Deseja continuar? [S/N] ")

	if conn.lower() == "n":
		break
	else:
		print(" ")
