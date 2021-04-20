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
			a, b, e, f = [1,2,0.001,"x ** 2 - 3"]
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

	er = 0
	k = (math.log(b-a) - math.log(e)) / math.log(2)
	print(" |   k | a        | b        | x0       | f(a)     | f(x0)    | sinal  | E(b-a)   | ")

	for i in range(round(k) + 1):
		f1 = ""
		f2 = ""

		for j in range(len(f)):
			if f[j] == "x":
				f1 += str(a)
				f2 += str((a+b)/2)
			else:
				f1 += f[j]
				f2 += f[j]

		ff1 = eval(str(f1))
		ff2 = eval(str(f2))

		if ff1 * ff2 >= 0:
			si = "+"
		else:
			si = "-"

		if i != 0:
			er = b - a

		print(" | " + "%3i" % i + " | " + sinal(a) + " | " + sinal(b) + " | " + sinal((a+b)/2) +
			  " | " + sinal(ff1) + " | " + sinal(ff2) + " | " + si + "      | " + sinal(er) + " | ")

		if ff1 * ff2 >= 0:
			a = (a+b)/2
		else:
			b = (a+b)/2

	print(" ")
	con = input("Deseja continuar? [S/N] ")

	if con.lower() == "n":
		break
	else:
		print(" ")
