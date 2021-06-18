import math
from math import e

inicio = input("Você irá Calcular ou Testar? [C/T] ")
print()

if inicio == "T":
	fc = "x * e**(2*x)"
	lf = "e**(2*x) * 2 * x - e**(2*x)"
	f2 = "32 * e**(2*x) + 16 * x * e**(2*x)"
	iv = [0, 0.4]
	eo = 0.001
	n = 2
else:
	fc = input("Informe a equação da função: ")
	print()
	lf = input("Informe a integral da função: ")
	print()
	f2 = input("Informe a segunda derivada da função: ")
	print()
	iv = list(map(float,input("Informe o intervalo: ").split()))
	print()
	eo = float(input("Informe o erro para descobrir as subdivisões: "))
	print()
	n = int(input("Informe o número de iterações: "))
	print()

# Quarta Derivada
mf20, mf21 = ["",""]
for w in range(len(f2)):
	if f2[w] == "x":
		mf20 += str(iv[0])
		mf21 += str(iv[1])
	else:
		mf20 += f2[w]
		mf21 += f2[w]

mf20 = round(eval(mf20),3)
mf21 = round(eval(mf21),3)

if mf20 < 0:
	mf20 = mf20 * -1

if mf21 < 0:
	mf21 = mf21 * -1

if mf21 > mf20:
	mf2 = mf21
else:
	mf2 = mf20

# Subdivisões
hP = (iv[1] - iv[0])
if hP < 0:
	hP = hP * -1

subd = ((hP**3 / (12 * eo)) * mf2)**(1/2)

subd1 = round(subd, 4)
subd0 = round(subd+.5)

# Resultado da integral:
ir0, ir1 = ["", ""]
for i in range(len(lf)):
	if lf[i] == "x":
		ir0 += str(iv[0])
		ir1 += str(iv[1])
	else:
		ir0 += lf[i]
		ir1 += lf[i]
ir = eval(ir1) - eval(ir0)

print("-------------------------------------------------------------------------------\n")

print("O número de subdivisões para o erro informado é: {} = {}".format(subd1,subd0), "\n")

print("n = (({}^3 / (12 * {})) * {})^(1/2) = {}".format(hP,eo,mf2,subd), "\n")

print("-------------------------------------------------------------------------------\n")

print("O valor da integral será:", ir, "\n")

print("-------------------------------------------------------------------------------\n")

i = 1

for k in range(n):

	# Altura
	h = (iv[1] - iv[0]) / i
	h = round(h,3)
	print("O número de subintervalos será:", i, "\n")
	print("h = ({} - {}) / {} = {}".format(iv[1], iv[0], i, h), "\n")

        # Erro
	erro = (hP**3 / (12 * i**2)) * mf2
	print("O cálculo do erro será:", erro, "\n")
	print("E = ({}^3 / (12 * {}^2)) * {} = {}".format(hP, i, mf2, erro), "\n")

	# Valores de x
	x = []
	x_s = iv[0]
	for i in range(i+1):
		x.append(round(x_s,3))
		x_s += h

	print("x =", x, "\n")

	# Valores de y
	y = []
	for j in range(len(x)):
		fr = ""
		for k in range(len(fc)):
			if fc[k] == "x":
				fr += str(x[j])
			else:
				fr += fc[k]		
		y.append(round(eval(fr),3))
		print("f(" + str(x[j]) + ") = " + str(fr + " = " + str(round(eval(fr),3))))
	print()
	print("y =", y, "\n")

	# Resultado
	s = 0
	er = 0
	for j in range(len(x)):
		if j == 0:
			s += (h / 2) * y[0]
			print("Aproximação = ({} / 2) * {} + ".format(h, y[0]), end="")
		elif (j == (len(x) - 1)):
			s += (h / 2) * y[len(x) - 1]
			print("({} / 2) * {} = {}".format(h, y[len(x) - 1], s), "\n")
		else:
			s += h * (y[j])
			print("({} / 2) * 2 * {} + ".format(h, y[j]), end="")

	er = round(100 * (ir - s / ir),3)

	if er < 0:
			er *= -1

	print("O valor da aproximação será de {} e o erro será de {}%.".format(round(s,5), er))
	print()
	print("-------------------------------------------------------------------------------\n")

	i += 1
