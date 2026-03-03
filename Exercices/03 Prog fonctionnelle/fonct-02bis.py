student_ids = ["ETU-101", "ETU-102", "ETU-103"]
continuous_scores = [13.5, 15.0, 11.0]
final_scores = [14.0, 12.5, 16.0]

report = {
	sid: {
		"continu": cc,
		"examen": exam,
		"moyenne": round(cc * 0.4 + exam * 0.6, 2)
	}
	for sid, cc, exam in zip(student_ids, continuous_scores, final_scores)
}

print(report)