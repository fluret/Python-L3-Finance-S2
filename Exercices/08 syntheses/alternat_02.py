def aplatir(conteneurs):
    return [element for conteneur in conteneurs for element in conteneur]

def alternat(c1, c2):
    return aplatir(zip(c1, c2))
