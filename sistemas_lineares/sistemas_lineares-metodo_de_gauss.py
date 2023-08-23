def sinal(nmr):
    if nmr >= 0:
        nmr = "+%3.5f" % nmr
    else:
        nmr = "%3.5f" % nmr

    return nmr

l = int(input("Informe o número de linhas: "))
print("")

m_i, m_x, m_d, z = [[],[],[],0]

for i in range(l):
    m_i.append(list(map(float,input("Insira a linha %.i da matriz: " % i).split())))
print("")

if m_i[0][0] == 0:
    for i in range(l-1,-1,-1):
        print(i)
        if m_i[i][0] != 0:
            z = i

    m_i[0], m_i[z] = m_i[z], m_i[0]

c1, c2 = [1,0]

for k in range(l-1):
    for i in range(c1,l):
        n_m = (m_i[i][k] * -1 / m_i[c2][k])
        for j in range(l+1):
            m_i[i][j] += n_m * m_i[c2][j]

    c1 += 1
    c2 += 1

for i in range(l):
    m_x.append(m_i[i][l])
    for j in range(l):
        if i == j:
            m_d.append(m_i[i][j])

c1 = l
c2 = 0

for i in range(l-1,-1,-1):
    for j in range(c2):
        m_x[i] -= m_i[i][l - 1 - j] * m_x[l - 1 - j]

    m_x[i] /= m_d[i]

    c1 -= 1
    c2 += 1

print(" |       x0 |", end="")
for i in range(1,l):
    print("       x%.f |" % i, end="")

print("")

print(" | " + sinal(m_x[0]) + " |", end="")
for i in range(1,l):
    print(" " + sinal(m_x[i]) + " |", end="")
