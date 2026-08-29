def assign_priority(fit_score: int) -> str:
    if fit_score >= 90:
        return "APPLY NOW"
    if fit_score >= 80:
        return "HIGH"
    if fit_score >= 70:
        return "CONSIDER"
    if fit_score >= 60:
        return "STRETCH"
    return "SKIP"


def is_alert_worthy(fit_score: int, minimum_score: int = 75) -> bool:
    return fit_score >= minimum_score
