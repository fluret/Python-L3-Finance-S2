from carre_data import liste
from carre_01 import carre
from carre_02 import carre as carre_02
from carre_03 import carre as carre_03

def test(liste, ma_fonction):
    for l in liste:
        print(f"Chaine à traiter : |{l}|\n"
                f"donne le résultat : {ma_fonction(l)!r:>50} \n"
                f"{20*'*'}"
                )

test(liste, carre)
print(40*"-")
test(liste, carre_02)
print(40*"-")
test(liste, carre_03)