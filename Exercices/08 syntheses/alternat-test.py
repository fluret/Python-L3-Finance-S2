from alternat_data import liste_vals
from alternat_01 import alternat
from alternat_02 import alternat as alternat_02

def test(fonction, liste):
    resultats = []
    for l in liste:
        a, b = l
        resultats.append((a, b, fonction(a, b)))

    largeur_appel = max(len(f"alternat({a}, {b})") for a, b, _ in resultats)
    largeur_retour = max(len(str(retour)) for _, _, retour in resultats)

    for a, b, retour in resultats:
        appel = f"alternat({a}, {b})"
        print(f"La fonction {appel:<{largeur_appel}} renvoie -> {str(retour):>{largeur_retour}}")

print("Test de la fonction alternat_01 :")
test(alternat, liste_vals)
print("\nTest de la fonction alternat_02 :")
test(alternat_02, liste_vals)
