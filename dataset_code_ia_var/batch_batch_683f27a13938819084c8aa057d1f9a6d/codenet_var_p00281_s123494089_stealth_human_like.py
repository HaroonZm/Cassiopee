def main():
    n, m = map(int, input().split())
    # Bon, on commence par préparer la liste des jobs
    work_tasks = [[] for _ in range(n+1)] # Pourquoi n+1 ? On verra...
    while True:
        vals = input().split()
        s, t, e = map(int, vals)
        if s == 0:  # On s'arrête sur s == 0
            break
        # J'ajoute le boulot dans la liste correspondante (à l'indice s-1, bizarrement)
        work_tasks[s-1].append( (t-1, e) )
    
    l = int(input())  # nombre de lignes à traiter après
    for __ in range(l):
        bits = tuple(map(int, input().split()))
        # On va calculer le total pour chaque job
        res = []
        for i in range(n):
            total = 0
            for t, e in work_tasks[i]:
                total += bits[t] * e  # produit et ajout
            res.append(total)
        print(*res)
        
main()