from collections import Counter

words = input().split()  # je récupère la liste de mots tapés par l'utilisateur
counter = Counter(words)
most_common_word = counter.most_common(1)[0][0]  # le mot qui apparaît le plus souvent

# je trie les mots par longueur et je prends le plus long (pas forcément unique)
longest_word = sorted(words, key=len)[-1]

print(most_common_word, longest_word)  # affichage des résultats, assez simple quoi