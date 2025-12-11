"""Max Min Avg"""
import json
def calculate_stats(score_list):
    """Start"""
    if not score_list:
        return (0.0, 0.0, 0.0)

    highest = score_list[0]
    lowest = score_list[0]
    total_score = 0
    count = 0

    for score in score_list:
        if score > highest:
            highest = score

        if score < lowest:
            lowest = score

        total_score += score
        count += 1

    average = total_score / count
    return (round(highest, 2), round(lowest, 2), round(average, 2))
data = json.loads(input())
print(calculate_stats(data))
