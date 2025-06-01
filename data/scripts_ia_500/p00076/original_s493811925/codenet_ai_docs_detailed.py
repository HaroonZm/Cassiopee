import sys

def process_input():
    """
    Lit les lignes depuis l'entrée standard (sys.stdin) jusqu'à ce que la ligne '-1' soit rencontrée.
    Pour chaque ligne lue (représentant un entier n), calcule un nombre complexe z selon une règle spécifique,
    puis affiche la partie réelle et imaginaire de ce nombre complexe.
    
    La règle de calcul est la suivante :
    - Initialiser z à 1 (nombre complexe)
    - Répéter (n-1) fois la mise à jour de z en ajoutant (z * 1j) / |z * 1j|,
      où 1j est l'unité imaginaire en Python, et |.| est le module (valeur absolue) du nombre complexe.
    
    Lorsque la ligne '-1' est rencontrée, la fonction s'arrête.
    """
    for e in sys.stdin:
        # Vérifie si la ligne lue est '-1' suivi d'un saut de ligne, dans ce cas arrêt de la boucle
        if e == '-1\n':
            break
        
        # Convertit la ligne en entier pour le nombre d'itérations
        n = int(e)
        
        # Initialise z à 1 (nombre complexe 1 + 0j)
        z = 1
        
        # Effectue (n-1) itérations
        # Utilisation de [0]*~-n pour créer une liste itérable de taille n-1
        for _ in [0] * (n - 1):
            # Calcule d = z * 1j, ce qui correspond à une rotation de z de 90 degrés dans le plan complexe
            d = z * 1j
            
            # Normalise d en le divisant par sa norme (valeur absolue) pour avoir un vecteur unitaire
            d /= abs(d)
            
            # Met à jour z en ajoutant le vecteur unitaire d
            z += d
        
        # Affiche la partie réelle de z
        print(z.real)
        # Affiche la partie imaginaire de z
        print(z.imag)

if __name__ == "__main__":
    process_input()