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
			x, e, f, fl = [0.75, 0.01, "x ** 3 - 9 * x + 5", "(x ** 3 + 5)/9"]
			break
		elif teste.lower() == "c":
			x = float(input("Escreva o valor de 'x'       : "))
			e = float(input("Escreva o valor da precisão  : "))
			f = input("Escreva a função             : ")
			fl = input("Escreva a função de interação: ")
			print(" ")
			break
		else:
			print("Letra inválida! Use apenas 'T' ou 'C'.")
			print(" ")
			teste = input("Deseja testar o programa ou calcular? [T/C] ")
			print(" ")

	print(" | k | x        | f(x)     | ")

	f1 = ""

	for j in range(len(f)):
		if f[j] == "x":
			f1 += str(x)
		else:
			f1 += f[j]

	ff1 = eval(str(f1))

	print(" | " + str(0) + " | " + sinal(x) + " | " + sinal(ff1) + " | ")

	con = 1

	while True:
		f1 = ""

		for j in range(len(fl)):
			if fl[j] == "x":
				f1 += str(x)
			else:
				f1 += fl[j]

		x = eval(str(f1))

		f2 = ""

		for j in range(len(f)):
			if f[j] == "x":
				f2 += str(x)
			else:
				f2 += f[j]

		ff2 = eval(str(f2))

		print(" | " + str(con) + " | " + sinal(x) + " | " + sinal(ff2) + " | ")

		if (ff2 < 0):
			if (ff2 * -1 < e):
				break
		elif (ff2 > 0):
			if (ff2 < e):
				break

		con += 1

	print(" ")
	conn = input("Deseja continuar? [S/N] ")

	if conn.lower() == "n":
		break
	else:
		print(" ")
