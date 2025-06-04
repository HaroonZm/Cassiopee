# Solution complète pour le problème "Largest Rectangle in a Histogram"
# Utilisation d'une approche basée sur une pile pour garantir une complexité O(N)
# Chaque barre est traitée une fois pour trouver la plus grande aire possible.

def largest_rectangle_histogram(heights):
    # Initialisation d'une pile pour stocker les indices des barres
    stack = []
    max_area = 0
    n = len(heights)

    # On parcourt chaque barre du diagramme
    for i in range(n):
        # Tant que la barre courante est plus petite que la barre au sommet de la pile,
        # cela signifie que la barre au sommet de la pile ne peut pas s'étendre plus loin à droite.
        # On calcule alors l'aire du rectangle avec la barre du sommet de la pile comme hauteur
        while stack and heights[i] < heights[stack[-1]]:
            top = stack.pop()  # Indice de la barre
            # Largeur dépend de la pile:
            # Si la pile est vide, la largeur s'étend depuis le début jusqu'à i
            # Sinon, c'est entre l'élément au sommet de la pile et i
            left_index = stack[-1] if stack else -1
            width = i - left_index - 1
            area = heights[top] * width
            if area > max_area:
                max_area = area
        # On empile l'indice courant
        stack.append(i)

    # Après avoir traité toutes les barres, on traite celles restant dans la pile
    # Ces barres s'étendent jusqu'à la fin du tableau
    while stack:
        top = stack.pop()
        left_index = stack[-1] if stack else -1
        width = n - left_index - 1
        area = heights[top] * width
        if area > max_area:
            max_area = area

    return max_area

def main():
    # Lecture des entrées
    n = int(input())
    heights = list(map(int, input().split()))
    # Calcul et affichage de la plus grande aire
    print(largest_rectangle_histogram(heights))

if __name__ == "__main__":
    main()