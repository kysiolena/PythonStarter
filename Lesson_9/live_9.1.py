def check_scores(passing_score: int, passing_score_budget: int, list_scores: list = []):
    result = {
        'students passing': 0,
        'students passing in budget': 0,
        'students not passing': 0
    }

    for student_score in list_scores:
        if student_score >= passing_score_budget:
            result['students passing in budget'] += 1
        elif student_score >= passing_score:
            result['students passing'] += 1
        else:
            result['students not passing'] += 1

    return result


print(check_scores(75, 90, [50, 90, 75, 80, 30, 40, 95, 100, 40, 78, 91]))
print(check_scores(90, 100, [50, 90, 75, 80, 30, 40, 95, 100, 40, 78, 91]))
print(check_scores(50, 70, [50, 90, 75, 80, 30, 40, 95, 100, 40, 78, 91]))
print(check_scores(40, 60, [50, 90, 75, 80, 30, 40, 95, 100, 40, 78, 91]))
print(check_scores(80, 95, [50, 90, 75, 80, 30, 40, 95, 100, 40, 78, 91]))
