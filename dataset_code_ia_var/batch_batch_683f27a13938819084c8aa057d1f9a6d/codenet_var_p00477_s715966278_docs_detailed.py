def read_and_sum_times(count=4):
    """
    Lis `count` valeurs entières depuis l'entrée standard, chacune correspondant à une durée en secondes,
    les additionne, et retourne le total.
    
    Args:
        count (int): Le nombre de valeurs à lire. Par défaut à 4.
        
    Returns:
        int: La somme totale des durées lues en secondes.
    """
    total_time = 0  # Variable pour stocker la somme totale des durées
    for i in range(count):
        # Lecture de la durée à ajouter (en secondes) sur chaque itération
        value = int(input())
        total_time += value  # Ajout de la durée à la somme totale
    return total_time

def convert_seconds_to_minutes_and_seconds(total_seconds):
    """
    Convertit une durée exprimée en secondes en minutes et secondes.
    
    Args:
        total_seconds (int): Le temps total à convertir, en secondes.
    
    Returns:
        tuple: Un tuple contenant d'abord le nombre de minutes, puis le nombre de secondes restantes (minutes, secondes).
    """
    minutes = total_seconds // 60  # Nombre de minutes pleines dans la durée totale
    seconds = total_seconds % 60   # Nombre de secondes restantes après conversion en minutes
    return minutes, seconds

def main():
    """
    Fonction principale du script : lit des entrées utilisateur, calcule la somme totale, convertir en minutes/secondes
    et affiche le résultat sur deux lignes.
    """
    # Calcule la somme des temps entrés par l'utilisateur
    total_time = read_and_sum_times()
    
    # Convertit la somme totale de secondes en minutes et secondes
    minutes, seconds = convert_seconds_to_minutes_and_seconds(total_time)
    
    # Affiche le résultat : les minutes sur la première ligne, les secondes sur la deuxième
    print(minutes)
    print(seconds)

if __name__ == "__main__":
    main()