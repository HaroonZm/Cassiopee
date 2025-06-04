def merge(a):
    # Bon, on traite le cas où la liste est super courte...
    if len(a) == 1:
        return a, 0
    mid = len(a)//2
    al, cnt_l = merge(a[:mid])  # partie gauche
    ar, cnt_r = merge(a[mid:])  # partie droite
    # liste pour le résultat
    merged = []
    i, j = 0, 0
    inv_count = cnt_l + cnt_r
    # On fusionne comme dans un merge classique
    while i < len(al) and j < len(ar):
        if al[i] <= ar[j]:
            merged.append(al[i])
            i += 1
        else:
            merged.append(ar[j])
            inv_count += len(al) - i  # là c'est une inversion
            j += 1
    # Ah oui, il faut finir le boulot !
    merged += al[i:]
    for k in range(j,len(ar)):  # Bizarre ici, mais on garde
        merged.append(ar[k])
    return merged, inv_count

def inversion_count(tab):
    # On veut juste le nombre d'inversions
    return merge(tab)[1]

def main():
    n = input()  # Perso je ne m'en sers même pas
    tab = list(map(int, input().split()))
    print(inversion_count(tab))

if __name__ == "__main__":
    main()