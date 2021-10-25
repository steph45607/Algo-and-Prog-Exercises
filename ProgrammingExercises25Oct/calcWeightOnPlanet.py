def calcWeightOnPlanet(w, g=23.1):
    m = w/9.8 #convert earth weight to mass by dividing with earth gravity
    print(m*g) #will multiply mass with gravity assigned, default jupiter

calcWeightOnPlanet(120,9.8)
calcWeightOnPlanet(120)
calcWeightOnPlanet(120,23.1)