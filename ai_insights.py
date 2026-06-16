def generate_insights(report):

    insights = []

    missing = sum(report["Missing Values"].values())

    if missing > 0:
        insights.append(f"{missing} missing values found")
    else:
        insights.append("No missing values")

    if report["Duplicate Rows"] > 0:
        insights.append("Duplicates detected")
    else:
        insights.append("No duplicates")

    if report["Outliers"] > 0:
        insights.append("Outliers detected")
    else:
        insights.append("No outliers")

    if report["Invalid Emails"] > 0:
        insights.append("Invalid emails found")
    else:
        insights.append("Emails are valid")

    return insights


def calculate_health_score(report):

    score = 100

    missing = sum(report["Missing Values"].values())

    score -= missing * 5
    score -= report["Duplicate Rows"] * 10
    score -= report["Outliers"] * 5
    score -= report["Invalid Emails"] * 10

    if score < 0:
        score = 0

    return score