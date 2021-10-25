def numAtoms(g,w = 196.97): #g is the grams, w will be the weight
    m = g /w #since w = g/m, m (moles) = g/w
    a = m * (6.022*(10**23)) #since avogadro = a/m, a(atoms) = avogadro*m
    print(a)

numAtoms(10)
numAtoms(10,12.001)
numAtoms(10,1.008)