resultat = []
for machine in dict_machines:
    if machine['Index'] in [1, 2, 7, 8, 11, 14, 19]:
        nouveau = {
            "Index": machine['Index'],
            "InBudget": "Yes" if machine['Cost'] < 1000 else "No",
            "ValidService": machine["InService"] or machine["InService"] % 2 == 0
        }
        resultat.append(nouveau)