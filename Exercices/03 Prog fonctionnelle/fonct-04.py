client_ids = ["C-101", "C-102", "C-103", "C-104"]
purchase_amounts = [250.0, 80.0, 120.0, 310.0]
discount_rates = [0.10, 0.05, 0.20, 0.15]


def is_eligible(row):
	return row[1] >= 100


def build_report_row(row):
	return {
		"client": row[0],
		"montant_initial": row[1],
		"remise": row[2],
		"montant_final": round(row[1] * (1 - row[2]), 2)
	}

grouped = zip(client_ids, purchase_amounts, discount_rates)
eligible = filter(is_eligible, grouped)

final_report = list(map(build_report_row, eligible))

print(final_report)