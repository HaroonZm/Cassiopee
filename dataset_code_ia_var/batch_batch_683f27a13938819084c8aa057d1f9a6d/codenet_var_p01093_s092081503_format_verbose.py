while True:

    number_of_students = int(input())

    if number_of_students == 0:
        break

    student_scores = sorted(list(map(int, input().strip().split())))

    minimum_score_difference = 1000000

    for index in range(number_of_students - 1):

        current_difference = abs(student_scores[index] - student_scores[index + 1])

        if current_difference < minimum_score_difference:
            minimum_score_difference = current_difference

    print(minimum_score_difference)