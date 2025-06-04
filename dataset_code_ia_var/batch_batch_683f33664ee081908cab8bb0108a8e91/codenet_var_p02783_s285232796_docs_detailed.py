import sys
import socket

# Récupère le nom d'hôte (hostname) de la machine locale
hostname = socket.gethostname()

# Si le programme s'exécute sur une machine spécifique, redirige l'entrée standard depuis le fichier 'a1.in'.
if hostname == 'F451C':
    sys.stdin = open('a1.in')

def read_int_list():
    """
    Lit une ligne de l'entrée standard, la sépare par les espaces, 
    convertit chaque élément en entier et retourne la liste des entiers lus.

    Returns:
        list of int: Liste des entiers obtenus depuis l'entrée.
    """
    return list(map(int, input().split()))

def read_str_list():
    """
    Lit une ligne de l'entrée standard, la sépare par les espaces 
    et retourne la liste des chaînes obtenues.

    Returns:
        list of str: Liste des chaînes lues depuis l'entrée.
    """
    return input().split()

def read_int():
    """
    Lit une ligne de l'entrée standard et la convertit en entier.

    Returns:
        int: L'entier lu depuis l'entrée.
    """
    return int(input())

def read_str():
    """
    Lit une ligne de l'entrée standard et la retourne telle quelle (chaîne de caractères).

    Returns:
        str: La chaîne lue depuis l'entrée.
    """
    return input()

def main():
    """
    Fonction principale du programme.
    Lit deux entiers H et A depuis l'entrée,
    puis calcule le nombre minimal d'opérations nécessaires pour réduire
    H à un nombre inférieur ou égal à zéro en soustrayant A à chaque étape.
    Affiche ensuite le nombre d'opérations réalisées.
    """
    # Lit les valeurs de H (santé) et A (attaque) depuis l'entrée
    H, A = read_int_list()
    res = 0  # Initialise le compteur d'opérations à zéro
    
    # Répète l'opération de soustraction de A à H jusqu'à ce que H soit inférieur ou égal à zéro
    for i in range(10001):
        H = H - A  # Soustrait A à la valeur courante de H
        res += 1   # Incrémente le compteur d'opérations
        if H <= 0:
            break  # Termine la boucle si H est inférieur ou égal à zéro
    
    # Affiche le nombre total d'opérations effectuées
    print(res)

# Exécute la fonction principale lorsque le script est lancé
main()