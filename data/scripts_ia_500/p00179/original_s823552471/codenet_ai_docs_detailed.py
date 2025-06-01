import Queue

# Dictionnaire de transformation des paires de caractères en une nouvelle paire
dic = {
    'rg': 'bb', 'gr': 'bb',
    'gb': 'rr', 'bg': 'rr',
    'br': 'gg', 'rb': 'gg',
}

def min_transformations_to_uniform(s):
    """
    Calcule le nombre minimum de transformations nécessaires pour rendre une chaîne
    composée uniquement des lettres 'r', 'g', et 'b' uniforme (tous les caractères identiques).
    
    Chaque transformation consiste à prendre deux caractères adjacents différents dans la chaîne
    et à les remplacer par une paire spécifique, définie par le dictionnaire de transformations.
    
    La fonction utilise une recherche en largeur avec priorité (Dijkstra) pour trouver
    le chemin de transformations avec le coût minimal.
    
    Paramètres:
    -----------
    s : str
        La chaîne de caractères initiale à transformer.
        
    Retourne:
    ---------
    int
        Le nombre minimum de transformations nécessaires pour obtenir une chaîne uniforme.
        Retourne -1 si ce n'est pas possible.
    """
    # Import local pour éviter redondance si appelée plusieurs fois
    import Queue
    
    # Longueur de la chaîne initiale
    l = len(s)
    
    # File de priorité pour les états à explorer (la prioridad est le coût)
    que = Queue.PriorityQueue()
    
    # Dictionnaire pour mémoriser le coût minimal d'atteindre chaque état (chaîne)
    cost = {s: 0}
    
    # Ajouter l'état initial à la file avec un coût de 0
    que.put((0, s))
    
    # États finaux possibles : chaînes uniformes composées uniquement d'un seul caractère
    target_states = ['r' * l, 'g' * l, 'b' * l]
    
    # Variable de résultat initialisée à -1 pour indiquer pas de solution trouvée
    ans = -1
    
    # Boucle principale pour explorer les états jusqu'à ce que la file soit vide
    while not que.empty():
        # Extraire l'état avec le coût minimal
        current_cost, current_state = que.get()
        
        # Si on a atteint un état final uniforme, on peut retourner le coût
        if current_state in target_states:
            ans = current_cost
            break
        
        # Ignorer cette exploration si on a déjà une meilleure solution pour cet état
        if cost[current_state] < current_cost:
            continue
        
        # Parcourir toutes les paires adjacentes dans la chaîne actuelle
        for i in xrange(l - 1):
            pair = current_state[i:i+2]
            
            # Vérifier que les deux caractères de la paire sont différents
            if pair[0] != pair[1]:
                # Générer la nouvelle chaîne en remplaçant la paire par la valeur de transformation
                new_state = current_state[:i] + dic[pair] + current_state[i+2:]
                
                # Calculer le nouveau coût (un pas de plus)
                new_cost = current_cost + 1
                
                # Si cette nouvelle chaîne n'a pas encore été visitée ou si on trouve un coût meilleur
                if new_state not in cost or new_cost < cost[new_state]:
                    cost[new_state] = new_cost
                    que.put((new_cost, new_state))
    
    return ans

def main():
    """
    Fonction principale qui lit les entrées utilisateur jusqu'à l'entrée '0' et affiche pour
    chaque chaîne le nombre minimum de transformations nécessaires ou 'NA' si impossible.
    """
    while True:
        # Lecture de la chaîne d'entrée
        s = raw_input()
        
        # Si l'entrée est '0', terminer la boucle
        if s == '0':
            break
        
        # Calculer la réponse pour la chaîne donnée
        result = min_transformations_to_uniform(s)
        
        # Afficher le résultat : 'NA' si pas de solution, sinon le nombre de transformations
        if result < 0:
            print "NA"
        else:
            print result

if __name__ == "__main__":
    main()