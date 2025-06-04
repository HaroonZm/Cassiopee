import sys
import bisect

def main():
    input = sys.stdin.readline
    
    # Nombre de liquides préparés
    N = int(input())
    
    # Dictionnaire qui associe chaque couleur à la liste triée de ses densités disponibles
    color_to_densities = {}
    
    for _ in range(N):
        c, d = input().split()
        d = int(d)
        if c not in color_to_densities:
            color_to_densities[c] = []
        color_to_densities[c].append(d)
    
    # Tri des densités pour chaque couleur afin de faire des recherches binaires plus tard
    for c in color_to_densities:
        color_to_densities[c].sort()
    
    # Nombre de couches demandées dans la boisson
    M = int(input())
    
    # Lecture des couleurs demandées de la boisson, de la couche la plus haute à la plus basse
    requested_colors = [input().strip() for _ in range(M)]
    
    # On doit construire la boisson du haut vers le bas :
    # Chaque couche a une densité STRICTEMENT inférieure à celle en dessous
    # On va donc, couche par couche, chercher une densité disponible inférieure à la précédente sélectionnée
    # initialement, on n'a aucune contrainte donc on peut prendre n'importe quelle densité valide pour la première couche
    
    # On stocke la densité de la couche en dessous pour la prochaine recherche
    prev_density = float('inf')
    
    for color in requested_colors:
        # Si la couleur n'existe pas dans les liquides préparés, on ne peut pas servir la boisson
        if color not in color_to_densities:
            print("No")
            return
        
        densities = color_to_densities[color]
        
        # On cherche la densité maximale strictement inférieure à prev_density
        # grâce à bisect_left : l'indice où prev_density pourrait être inséré
        pos = bisect.bisect_left(densities, prev_density)
        
        # pos est l'indice où on pourrait insérer prev_density à gauche.
        # donc l'élément à pos-1 est la densité la plus grande strictement inférieure à prev_density (si pos > 0)
        if pos == 0:
            # Pas de densité strictement inférieure à prev_density -> impossible
            print("No")
            return
        
        # On prend donc densities[pos-1] comme densité choisie pour cette couche
        chosen_density = densities[pos-1]
        
        # Mettre à jour la contrainte pour la prochaine couche
        prev_density = chosen_density
    
    # Si on arrive ici, cela signifie qu'on a trouvé une densité valide pour chaque couche dans l'ordre demandé
    print("Yes")

if __name__ == "__main__":
    main()