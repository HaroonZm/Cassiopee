while True:
    user_input = input()
    midterm_score_str, final_score_str, re_exam_score_str = user_input.split()
    midterm_score = int(midterm_score_str)
    final_score = int(final_score_str)
    re_exam_score = int(re_exam_score_str)

    if midterm_score == -1 and final_score == -1 and re_exam_score == -1:
        break

    total_exam_score = midterm_score + final_score

    if midterm_score == -1 or final_score == -1 or total_exam_score < 30:
        print('F')
    elif total_exam_score < 50 and re_exam_score < 50:
        print('D')
    elif total_exam_score < 65:
        print('C')
    elif total_exam_score < 80:
        print('B')
    else:
        print('A')