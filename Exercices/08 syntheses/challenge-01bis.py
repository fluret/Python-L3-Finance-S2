resultat_comp = [{"Index": machine['Index'],"InBudget": "Yes" if machine['Cost'] < 1000 else "No","ValidService": machine["InService"] or machine["Index"] % 2 == 0}for machine in dict_machines if machine['Index'] in target_indexes]
#L'écriture suivante est plus lisible :
resultat_comp = [
    {
        "Index": machine['Index'],
        "InBudget": "Yes" if machine['Cost'] < 1000 else "No",
        "ValidService": machine["InService"] or machine["Index"] % 2 == 0
    }
    for machine in dict_machines
    if machine['Index'] in target_indexes
]

print(resultat_comp)