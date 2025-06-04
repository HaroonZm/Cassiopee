# Solution complète au problème "Distorted Love"
# Le programme lit plusieurs jeux de données, pour chacun il simule un navigateur avec une gestion d'historique,
# des boutons cliquables sur chaque page qui redirigent vers d'autres pages, ainsi que les touches 'back' et 'forward'.
# Pour chaque opération 'show' il affiche le nom de la page courante.

def main():
    import sys
    input = sys.stdin.readline

    while True:
        n = int(input())
        if n == 0:
            break

        W, H = map(int, input().split())

        # Stockage des pages:
        # pages = {
        #    nom_page: [ (x1,y1,x2,y2, nom_page_dest), ... boutons ]
        # }
        pages = {}

        # Lecture des pages
        for _ in range(n):
            line = input().strip().split()
            page_name = line[0]
            b_i = int(line[1])
            buttons = []
            for __ in range(b_i):
                x1, y1, x2, y2, dest = input().strip().split()
                x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))
                buttons.append( (x1, y1, x2, y2, dest) )
            pages[page_name] = buttons

        # Initialisation du buffer d'historique et du pointeur
        history = []
        # Le premier page donnée est la page initiale
        page_names = list(pages.keys())
        current_idx = 0
        history.append(page_names[0])

        m = int(input())

        for _ in range(m):
            operation = input().strip().split()
            cmd = operation[0]

            if cmd == "click":
                x, y = int(operation[1]), int(operation[2])
                current_page = history[current_idx]
                buttons = pages[current_page]
                clicked_page = None
                # Recherche du bouton contenant le point (x,y)
                for (x1, y1, x2, y2, dest) in buttons:
                    if x1 <= x <= x2 and y1 <= y <= y2:
                        clicked_page = dest
                        break
                # Si un bouton a été cliqué
                if clicked_page is not None:
                    # Supprimer toutes les pages à droite du pointeur dans l'historique
                    history = history[:current_idx+1]
                    # Ajouter la nouvelle page à la fin
                    history.append(clicked_page)
                    current_idx += 1
                # Sinon rien à faire

            elif cmd == "back":
                # Aller à gauche si possible
                if current_idx > 0:
                    current_idx -= 1

            elif cmd == "forward":
                # Aller à droite si possible
                if current_idx < len(history) - 1:
                    current_idx += 1

            elif cmd == "show":
                # Afficher la page courante
                print(history[current_idx])

if __name__ == "__main__":
    main()