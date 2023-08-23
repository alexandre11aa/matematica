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

	con = 0
	print(" | k | a        | f(a)     | b        | f(b)     | x        | f(x)     | ")

	while True:
		f1 = ""
		f2 = ""
		f3 = ""

		for j in range(len(f)):
			if f[j] == "x":
				f1 += str(a)
				f2 += str(b)
			else:
				f1 += f[j]
				f2 += f[j]

		ff1 = eval(str(f1))
		ff2 = eval(str(f2))

		for j in range(len(f)):
			if f[j] == "x":
				f3 += str((a * ff2 - b * ff1)/(ff2 - ff1))
			else:
				f3 += f[j]

		ff3 = eval(str(f3))

		if ff1 * ff2 >= 0:
			si = "+"
		else:
			si = "-"

		print(" | " + str(con) + " | " + sinal(a) + " | " + sinal(ff1) + " | " + sinal(b) + " | " + sinal(ff2) + " | "
			  + sinal((a * ff2 - b * ff1)/(ff2 - ff1)) + " | " + sinal(ff3) + " | ")

		if ff1 * ff2 >= 0:
			a = (a * ff2 - b * ff1)/(ff2 - ff1)
		else:
			b = (a * ff2 - b * ff1)/(ff2 - ff1)

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
