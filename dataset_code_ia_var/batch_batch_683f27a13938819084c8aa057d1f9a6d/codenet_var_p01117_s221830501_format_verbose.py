import sys

def compute_highest_total_score(number_of_students, number_of_subjects):

    subject_scores_list = []

    for subject_index in range(number_of_subjects):

        scores_for_subject = [int(score) for score in input().split()]
        subject_scores_list.append(scores_for_subject)

    total_scores_per_student = [sum(scores) for scores in zip(*subject_scores_list)]

    highest_total_score_among_students = max(total_scores_per_student)

    return highest_total_score_among_students

def process_results(arguments):

    while True:

        input_line = input()
        number_of_students, number_of_subjects = map(int, input_line.split())

        if number_of_students == 0 and number_of_subjects == 0:
            break

        maximum_total_score = compute_highest_total_score(number_of_students, number_of_subjects)

        print(maximum_total_score)

if __name__ == '__main__':

    process_results(sys.argv[1:])