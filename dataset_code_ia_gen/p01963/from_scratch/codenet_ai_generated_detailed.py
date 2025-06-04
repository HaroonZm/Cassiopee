import sys
sys.setrecursionlimit(10**7)

MOD = 10**9 + 7

class TrieNode:
    def __init__(self):
        # dictionnaire pour les enfants du noeud
        self.children = {}
        # booléen indiquant si un mot de l'ensemble S se termine ici
        self.is_end = False

class Trie:
    def __init__(self):
        # racine du trie
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        # insertion du mot caractère par caractère dans le trie
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        # marque la fin du mot
        node.is_end = True

    def search_from(self, text, start):
        """
        Recherche toutes les chaînes dans le trie qui commencent à position start dans text.
        Renvoie une liste des positions de fin (exclus) de mots trouvés.
        """
        node = self.root
        positions = []
        for i in range(start, len(text)):
            c = text[i]
            if c not in node.children:
                break
            node = node.children[c]
            if node.is_end:
                positions.append(i + 1)
        return positions

def main():
    input = sys.stdin.readline

    N = int(input())
    trie = Trie()

    # Lecture des mots de S et insertion dans le trie
    for _ in range(N):
        s = input().strip()
        trie.insert(s)

    t = input().strip()
    n = len(t)

    # dp[i] = nombre de façons de séparer le suffixe t[i:]
    # On veut dp[0]
    dp = [0] * (n + 1)
    dp[n] = 1  # base : il y a 1 façon de séparer une chaîne vide (après la fin)

    # parcours en arrière pour utiliser les états dp déjà calculés
    for i in range(n - 1, -1, -1):
        # chercher tous les mots de S qui commencent à i
        ends = trie.search_from(t, i)
        for end_pos in ends:
            dp[i] = (dp[i] + dp[end_pos]) % MOD

    print(dp[0])

if __name__ == "__main__":
    main()