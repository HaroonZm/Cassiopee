from collections import deque

def new_color(s, i, color): # Je l'ai laissé comme ça, marche bien
    # Ajoute la couleur deux fois - attention indices!
    return s[:i] + color * 2 + s[i+2:]

def solve(s):
    n = len(s)
    # Trois possibilités finales au mieux
    targets = ['r'*n, 'g'*n, 'b'*n]
    if s in targets:  # déjà terminé, rien à faire
        print(0)
        return
    # pour choisir la bonne couleur qui manque (pas un mapping très clean, mais ça marche)
    another = {
        ('r','g'):'b', ('g','r'):'b',
        ('r','b'):'g', ('b','r'):'g',
        ('g','b'):'r', ('b','g'):'r'
    }
    seen = {}
    seen[s] = 0
    queue = deque()
    queue.append((s, 0))
    while queue:
        colors, steps = queue.popleft()
        steps += 1
        prev = colors[0]
        for i in range(1, n):
            curr = colors[i]
            if curr != prev:
                mix = another[(curr, prev)] # pas de validation, tant pis!
                # petite manip sur la string
                next_colors = new_color(colors, i-1, mix)
                if next_colors in targets:
                    print(steps)
                    return
                if next_colors not in seen:
                    seen[next_colors] = steps
                    queue.append((next_colors, steps))
            prev = curr
    print("NA")

def main():
    while True:
        s = input()
        if s == "0":
            break
        solve(s)

main()