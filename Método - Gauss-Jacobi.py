def sinal(nmr):
    if nmr >= 0:
        nmr = "+%.5f" % nmr
    else:
        nmr = "%.5f" % nmr

    return nmr

print("O programa só irá funcionar se o número de colunas"
      "for uma unidade maior que o número de linhas, além"
      "da matriz passar pelas condições de convergência !")
print("")

mi_t, m1_a = [[],[]]

l = int(input("Número de linhas: "))
it = int(input("Número máximo de iterações: "))
ve = float(input("Porcentagem de erro: "))
print("")

for i in range(l):
    mi_t.append(list(map(float,input("Informe a linha %.i: " % (i + 1)).split())))
print("")
print(" |    I |", end="")

for i in range(l):
    print("       x%.i |" % (i + 1), end="")

print("        e |")

for i in range(l):
    m1_a.append(mi_t[i][l]/mi_t[i][i])

c = 0

while True:
    m1_p, m1_f = [[],[]]

    for i in range(l):
        nm_x = mi_t[i][l]/mi_t[i][i]
        for j in range(l):
            if j != i:
                nm_x += mi_t[i][j] * m1_a[j] * -1 / mi_t[i][i]

        m1_p.append(nm_x)

    for i in range(l):
        m1_f.append(m1_p[i] - m1_a[i])

        if m1_f[i] < 0:
            m1_f[i] *= -1

    x_m1, x_m2 = [0,0]

    for i in range(l):
        if m1_p[i] > x_m1:
            x_m1 = m1_p[i]

        if m1_f[i] > x_m2:
            x_m2 = m1_f[i]

    for i in range(l):
        m1_a[i] = m1_p[i]

    c += 1

    print(" | " + "%4i" % c, end="")

    for i in range(l):
        print(" | " + sinal(m1_p[i]), end="")

    print(" | " + sinal(x_m2 / x_m1) + " | ")

    if (x_m2 / x_m1 < ve) or it == c:
        break
