nombre_de_cartes = input()

score_taro = 0
score_hanako = 0

for index_carte in range(nombre_de_cartes):
    carte_taro, carte_hanako = raw_input().split()

    if carte_taro > carte_hanako:
        score_taro += 3

    elif carte_taro < carte_hanako:
        score_hanako += 3

    else:
        score_taro += 1
        score_hanako += 1

print score_taro, score_hanako