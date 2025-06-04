for iteration_count in range(110):

    student_count, subject_count = map(int, input().split())  # student_count: 生徒, subject_count: 科目

    if student_count == 0 and subject_count == 0:
        break

    else:
        total_scores_per_student = [0] * student_count

        for subject_index in range(subject_count):
            subject_scores = list(map(int, input().split()))

            for student_index in range(student_count):
                total_scores_per_student[student_index] += subject_scores[student_index]

        highest_total_score = max(total_scores_per_student)

        print(highest_total_score)