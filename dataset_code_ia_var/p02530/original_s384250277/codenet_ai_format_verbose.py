nombre_de_manches = int(raw_input())

score_hanako = 0
score_taro = 0

for numero_manche in range(nombre_de_manches):
    carte_taro, carte_hanako = raw_input().split()
    
    if carte_hanako == carte_taro:
        score_hanako += 1
        score_taro += 1
    elif carte_hanako < carte_taro:
        score_taro += 3
    else:
        score_hanako += 3

print " ".join(map(str, [score_taro, score_hanako]))