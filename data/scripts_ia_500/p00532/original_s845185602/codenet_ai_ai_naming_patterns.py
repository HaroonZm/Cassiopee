nombre_de_candidats = int(input())
nombre_de_evaluations = int(input())

reponses_attendues = list(map(int, input().split()))
predictions = [list(map(int, input().split())) for _ in range(nombre_de_evaluations)]

scores = [0 for _ in range(nombre_de_candidats)]
for indice_evaluation in range(nombre_de_evaluations):
    nb_erreurs = 0
    for indice_candidat in range(nombre_de_candidats):
        if reponses_attendues[indice_candidat] == predictions[indice_evaluation][indice_candidat]:
            scores[indice_candidat] += 1
        else:
            nb_erreurs += 1
    scores[reponses_attendues[indice_evaluation] - 1] += nb_erreurs

for score in scores:
    print(score)