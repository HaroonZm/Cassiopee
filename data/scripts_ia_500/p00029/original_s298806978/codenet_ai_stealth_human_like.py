words = input().split()  # je récupère la liste des mots ici
# bon, on cherche le mot le plus fréquent et le plus long
most_common = max(words, key=words.count)  # pas forcément efficace mais ça fait le taf
longest_word = max(words, key=len)
print(most_common, longest_word)