def lire_dimensions():
    return map(int, input().split())

def lire_nuage(h):
    return [[char for char in input()] for _ in range(h)]

def est_derniere_colonne(j, w):
    return j == w - 1

def traiter_case_dernier_colonne(cloud_char, flag, cnt):
    if cloud_char == 'c':
        flag = 1
        cnt = 0
        print(0, end='')
    elif flag == 0 and cloud_char == '.':
        print(-1, end='')
    elif cloud_char == '.':
        cnt += 1
        print(cnt, end='')
    else:
        cnt += 1
        print(cnt, end='')
    return flag, cnt

def traiter_case_non_derniere_colonne(cloud_char, flag, cnt):
    if cloud_char == 'c':
        flag = 1
        cnt = 0
        print(0, end=' ')
    elif flag == 0 and cloud_char == '.':
        print(-1, end=' ')
    else:
        cnt += 1
        print(cnt, end=' ')
    return flag, cnt

def traiter_ligne(cloud_ligne, w):
    flag = 0
    cnt = 0
    for j in range(w):
        if est_derniere_colonne(j, w):
            flag, cnt = traiter_case_dernier_colonne(cloud_ligne[j], flag, cnt)
        else:
            flag, cnt = traiter_case_non_derniere_colonne(cloud_ligne[j], flag, cnt)
    print()

def main():
    h, w = lire_dimensions()
    cloud = lire_nuage(h)
    for i in range(h):
        traiter_ligne(cloud[i], w)

main()