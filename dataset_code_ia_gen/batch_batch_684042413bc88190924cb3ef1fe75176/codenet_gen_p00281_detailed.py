import sys

def main():
    input = sys.stdin.readline
    
    # Lecture du nombre de職人 (N) et工事の種類 (M)
    N, M = map(int, input().split())
    
    # Structure pour stocker le nombre de fois que chaque職人 a fait chaque種別の工事
    # Comme N et M peuvent être grands mais e_i au total <= 50000, on utilise une liste de dictionnaires
    work_counts = [{} for _ in range(N)]
    
    # Lecture des記録 (職人番号 s, 工事種類 t, 回数 e)
    while True:
        s, t, e = map(int, input().split())
        if s == 0 and t == 0 and e == 0:
            break
        # Stocker la donnée, indices 0-based
        work_counts[s-1][t-1] = e
    
    # Lecture du nombre de算出回数 (L)
    L = int(input())
    
    # Pour chaque算出回数, lire la liste des単価 b pour chaque種別の工事
    # Puis calculer la給料 pour chaque職人
    for _ in range(L):
        prices = list(map(int, input().split()))
        
        # Calcul des給料 pour chaque職人
        # c[i] = sum of a[i][j] * b[j]
        salaries = [0]*N
        for i in range(N):
            total = 0
            # Pour chaque工事種別 j travaillé par職人 i
            for j, count in work_counts[i].items():
                total += count * prices[j]
            salaries[i] = total
        
        # Affichage des給料, séparés par un espace
        print(' '.join(map(str, salaries)))
        
if __name__ == "__main__":
    main()