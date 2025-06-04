def next_mayor():
    while True:
        # Lire le nombre de candidats (n) et le nombre initial de cailloux (p)
        line = input().strip()
        if line == '0 0':
            break
        n, p = map(int, line.split())
        
        # Initialiser la distribution des cailloux en main pour chaque candidat à 0
        kept = [0] * n
        
        # Initialiser le nombre de cailloux dans le bol
        bowl = p
        
        # Position du candidat courant (le maire initial est 0)
        current = 0
        
        # Compteur d'étapes pour éviter une boucle infinie dans un cas anormal
        steps = 0
        max_steps = 1000000
        
        while steps < max_steps:
            steps += 1
            
            if bowl > 0:
                # Le candidat prend un caillou dans le bol et le garde
                bowl -= 1
                kept[current] += 1
                
                # Condition de fin : ce candidat a pris le dernier caillou et
                # aucun autre candidat ne garde de caillou
                if bowl == 0 and sum(kept) == kept[current]:
                    print(current)
                    break
            else:
                # Le bol est vide, le candidat remet ses cailloux dans le bol
                bowl = kept[current]
                kept[current] = 0
            
            # Passer au candidat suivant à droite (ordre décroissant modulo n)
            current = (current - 1) % n

# Appel de la fonction principale
next_mayor()