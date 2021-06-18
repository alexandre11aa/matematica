import sympy as sym

#Descobrindo Matriz

while True:
    t_c = input("Gostaria de Testar, Calcular, Achar Função? [T/C/F] ")

    print("")

    if t_c == "T":
        grau, v_x, v_y, psç, pts = [9,[1,2,3,4,5,6,7,8,9,10],[0.3,5,21,32,55,71,133,169,270,305],[0,1,2,3,4,5,6,7,8,9],[4,7,10]]
    else:        
        grau = int(input("Informe o grau de P(x): "))
        print("")
        v_x = list(map(float,input("Informe os valores de x: ").split()))
        v_y = list(map(float,input("Informe os valores de y: ").split()))
        print("")
        psç = list(map(int,input("Informe as %i posições dos valores aproximados de P(x): " % (grau+1)).split()))
        if t_c == "C":
            pts = list(map(float,input("Informe os pontos da função que você quer descobrir: ").split()))
            print("")
        else:
            pts = [sym.Symbol('x')]
            print("")

    l_x = []
    l_y = []

    for i in range(len(psç)):
        l_x.append(v_x[psç[i]])
        l_y.append(v_y[psç[i]])

    m_i = []

    for i in range(grau+1):
            m_i.append([])
            for j in range(grau,-1,-1):
                    m_i[i].append(l_x[i]**j)
            m_i[i].append(l_y[i])

    #Descobrindo Função

    m_x, m_d, z, l = [[],[],0,grau+1]

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
    
    for i in range(len(pts)):
        r = 0
        exp = grau
        for j in range(len(m_x) - 1):
            r += (pts[i]**exp * m_x[j])
            exp -= 1

        r += m_x[len(m_x)-1]

        if t_c == "F":
            print("A função resumida será:", sym.expand(r))
        else:
            print("O valor de P(%.2f) = %.2f" % (pts[i], r))

    print("")
    v = input("Deseja continuar? [S/N] ")
    print("")

    if v == "N":
         break
