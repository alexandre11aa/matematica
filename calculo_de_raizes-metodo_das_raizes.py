import math

'''Cosseno: math.cos(x)
   Seno: math.sin(x)
   Tangente: math.tan(x)'''

def sinal(nmr):
	if nmr >= 0:
		nmr = "+%.5f" % nmr
	else:
		nmr = "%.5f" % nmr

	return nmr

while True:
	teste = input("Deseja testar o programa ou calcular? [T/C] ")

	print(" ")

	while True:

		if teste.lower() == "t":
			a, b, e, f = [0.5,1,0.01,"x ** 3 - 9 * x + 5"]
			break
		elif teste.lower() == "c":
			a = float(input("Escreva o valor de 'a'     : "))
			b = float(input("Escreva o valor de 'b'     : "))
			e = float(input("Escreva o valor da precisão: "))
			f = input("Escreva a função           : ")
			print(" ")
			break
		else:
			print("Letra inválida! Use apenas 'T' ou 'C'.")
			print(" ")
			teste = input("Deseja testar o programa ou calcular? [T/C] ")
			print(" ")

	print(" | k | x        | f(x)     | ")

	f1 = ""
	f2 = ""
	for j in range(len(f)):
		if f[j] == "x":
			f1 += str(a)
			f2 += str(b)
		else:
			f1 += f[j]
			f2 += f[j]

	ff1 = eval(str(f1))
	ff2 = eval(str(f2))

	print(" | " + "0" + " | " + sinal(a) + " | " + sinal(ff1) + " | ")
	print(" | " + "1" + " | " + sinal(b) + " | " + sinal(ff2) + " | ")

	con = 2
	while True:
		f3 = ""
		c = b - ((ff2 * (b - a)) / (ff2 - ff1))

		for j in range(len(f)):
			if f[j] == "x":
				f3 += str(c)
			else:
				f3 += f[j]

		ff3 = eval(str(f3))

		print(" | " + str(con) + " | " + sinal(c) + " | " + sinal(ff3) + " | ")

		a = b
		ff1 = ff2

		b = c
		ff2 = ff3

		if (ff3 < 0):
			if (ff3 * -1 < e):
				break
		elif (ff3 > 0):
			if (ff3 < e):
				break

		con += 1

	print(" ")
	conn = input("Deseja continuar? [S/N] ")

	if conn.lower() == "n":
		break
	else:
		print(" ")
