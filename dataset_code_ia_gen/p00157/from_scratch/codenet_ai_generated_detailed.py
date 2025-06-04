import sys

# Fonction pour calculer la plus longue chaîne imbriquée (Longest Increasing Subsequence respectant les contraintes)
def longest_nesting(dolls):
    # On trie les poupées par hauteur et en cas d'égalité par rayon (croissant)
    dolls.sort(key=lambda x: (x[0], x[1]))

    n = len(dolls)
    dp = [1] * n  # dp[i] sera la longueur max de l'enchainement se terminant par la poupée i

    for i in range(n):
        for j in range(i):
            # Une poupée j peut contenir la poupée i si hauteur[j] > hauteur[i] et rayon[j] > rayon[i]
            # Ici on veut une chaîne décroit grande -> petite poupée
            if dolls[j][0] > dolls[i][0] and dolls[j][1] > dolls[i][1]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
    return max(dp) if dp else 0

def main():
    input = sys.stdin.readline
    while True:
        n_line = input().strip()
        if n_line == "0":
            break
        n = int(n_line)
        ichiro_dolls = [tuple(map(int, input().split())) for _ in range(n)]
        m = int(input())
        jiro_dolls = [tuple(map(int, input().split())) for _ in range(m)]

        # Combiner les deux listes de poupées
        all_dolls = ichiro_dolls + jiro_dolls

        # Calculer la plus longue chaîne imbriquée possible avec toutes les poupées
        k = longest_nesting(all_dolls)

        # Afficher le résultat
        print(k)

if __name__ == "__main__":
    main()