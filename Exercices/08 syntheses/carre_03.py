def carre(ligne):
    liste_valeurs = [t.strip() for t in ligne.split(";")]
    return ":".join(str(int(entier)**2) for entier in liste_valeurs if entier)
