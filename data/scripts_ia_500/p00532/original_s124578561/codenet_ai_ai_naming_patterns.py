nombre_eleves = int(input())
nombre_questions = int(input())
reponses_etudiantes = list(map(int, input().split()))
score_questions = [0] * nombre_eleves
for question_index in range(nombre_questions):
    reponses_correctes = list(map(int, input().split()))
    for eleve_index in range(nombre_eleves):
        if reponses_etudiantes[question_index] == reponses_correctes[eleve_index]:
            score_questions[eleve_index] += 1
        else:
            score_questions[reponses_etudiantes[question_index] - 1] += 1
print(*score_questions)