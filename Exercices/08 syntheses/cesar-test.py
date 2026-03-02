from cesar_data import liste_vals
from cesar_01 import cesar as cesar_01
from cesar_03 import cesar as cesar_02


def _preparer_args(valeurs):
    if len(valeurs) == 2:
        a, b = valeurs
        return (a, b), {}

    if len(valeurs) == 3:
        a, b, c = valeurs
        if isinstance(c, dict):
            return (a, b), c
        return (a, b, c), {}

    raise ValueError(f"Format d'entrée invalide: {valeurs}")


def test(fonction, liste):
    for valeurs in liste:
        args, kwargs = _preparer_args(valeurs)
        appel_args = [str(arg) for arg in args]
        appel_kwargs = [f"{cle}={valeur}" for cle, valeur in kwargs.items()]
        appel = ", ".join(appel_args + appel_kwargs)
        resultat = fonction(*args, **kwargs)
        print(f"La fonction cesar({appel}) renvoie : {resultat}")

print("Test de la fonction cesar_01 :")
test(cesar_01, liste_vals)
print("\nTest de la fonction cesar_02 :")
test(cesar_02, liste_vals)