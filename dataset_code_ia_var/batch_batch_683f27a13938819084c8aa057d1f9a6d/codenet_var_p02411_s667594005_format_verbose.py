while True:

    midterm_score, final_score, resit_score = map(int, input().split())

    if midterm_score < 0 and final_score < 0 and resit_score < 0:
        break

    if midterm_score < 0 or final_score < 0:
        assigned_grade = 'F'

    elif midterm_score + final_score >= 80:
        assigned_grade = 'A'

    elif midterm_score + final_score >= 65:
        assigned_grade = 'B'

    elif midterm_score + final_score >= 50:
        assigned_grade = 'C'

    elif midterm_score + final_score >= 30:

        if resit_score >= 50:
            assigned_grade = 'C'
        else:
            assigned_grade = 'D'

    else:
        assigned_grade = 'F'

    print(assigned_grade)