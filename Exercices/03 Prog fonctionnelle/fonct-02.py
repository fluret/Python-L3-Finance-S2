student_ids = ["ETU-101", "ETU-102", "ETU-103"]
continuous_scores = [13.5, 15.0, 11.0]
final_scores = [14.0, 12.5, 16.0]


def calculate_average(ids, cc, exam):
    report_temp = {}
    for sid, c, e in zip(ids, cc, exam):
        report_temp[sid] = {
            "continu": c,
            "examen": e,
            "moyenne": round(c * 0.4 + e * 0.6, 2),
        }
    return report_temp


report = calculate_average(student_ids, continuous_scores, final_scores)

print(report["ETU-102"]["moyenne"])
print(report)
